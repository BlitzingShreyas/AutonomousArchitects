import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from sqlalchemy import select
from backend.database import Base, engine, SessionLocal
from backend.models import Task, Stage, Event
from backend.schemas import TaskCreate, TaskView, EventView
from backend.supervisor import AGENTS, claim, execute, fail


def create_app(db_engine=engine, factory=SessionLocal) -> FastAPI:
    jobs: set[asyncio.Task] = set()

    @asynccontextmanager
    async def lifespan(app):
        Base.metadata.create_all(db_engine)
        with factory() as db:
            interrupted = list(db.scalars(select(Task.id).where(Task.status == 'RUNNING')))
        for task_id in interrupted:
            fail(factory, task_id, None, 'Interrupted execution detected on startup; create a new task')
        yield
        for job in list(jobs):
            job.cancel()
        await asyncio.gather(*jobs, return_exceptions=True)

    app = FastAPI(title='AgentBailout', version='0.1.0', lifespan=lifespan)

    def get_task(task_id: str) -> TaskView:
        with factory() as db:
            task = db.get(Task, task_id)
            if task is None:
                raise HTTPException(404, 'Task not found')
            return TaskView.model_validate(task)

    @app.get('/health')
    def health():
        with factory() as db:
            db.execute(select(1))
        return {'status': 'ok', 'phase': 1}

    @app.post('/tasks', response_model=TaskView, status_code=201)
    def create_task(body: TaskCreate):
        if not body.prompt.strip():
            raise HTTPException(422, 'Prompt must contain text')
        with factory.begin() as db:
            task = Task(prompt=body.prompt.strip())
            task.stages = [Stage(name=name, position=i) for i, (name, _) in enumerate(AGENTS)]
            db.add(task)
            db.flush()
            db.add(Event(task_id=task.id, type='TASK_CREATED', message='Task persisted'))
            result = TaskView.model_validate(task)
        return result

    @app.get('/tasks', response_model=list[TaskView])
    def list_tasks():
        with factory() as db:
            return [TaskView.model_validate(t) for t in db.scalars(select(Task).order_by(Task.created_at.desc()).limit(100))]

    @app.get('/tasks/{task_id}', response_model=TaskView)
    def detail(task_id: str):
        return get_task(task_id)

    @app.post('/tasks/{task_id}/start', status_code=202)
    async def start(task_id: str):
        get_task(task_id)
        if not claim(factory, task_id):
            raise HTTPException(409, 'Only a CREATED task can be started')
        job = asyncio.create_task(execute(factory, task_id))
        jobs.add(job)
        job.add_done_callback(jobs.discard)
        return {'task_id': task_id, 'status': 'RUNNING'}

    @app.get('/tasks/{task_id}/events', response_model=list[EventView])
    def events(task_id: str):
        get_task(task_id)
        with factory() as db:
            return [EventView.model_validate(e) for e in db.scalars(select(Event).where(Event.task_id == task_id).order_by(Event.id))]

    return app


app = create_app()
