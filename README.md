# 🛟 AgentBailout
### The Self-Healing Control Plane for AI Agents

**Detect. Diagnose. Decide. Repair. Replace. Recover.**

AgentBailout is a fault-tolerant orchestration and recovery platform designed to make AI agent workflows more reliable, resilient, and economically governed.

When an agent fails during workflow execution, AgentBailout detects the failure, evaluates recovery eligibility, identifies a compatible replacement agent, and attempts to resume execution without unnecessarily restarting the entire workflow.

Rather than treating agent failure as the end of a task, AgentBailout introduces a systematic approach to failure detection, intelligent replacement, execution continuity, and economic recovery management.

---

## 🚀 Overview

Modern AI applications increasingly depend on multiple agents working together to complete complex tasks. However, these workflows can be interrupted by agent crashes, timeouts, heartbeat loss, invalid outputs, or other execution failures.

Traditional workflows may require manual intervention or restarting the entire process when an individual agent fails.

**AgentBailout addresses this reliability challenge.**

It introduces a centralized control plane that manages agent registration, workflow execution, failure monitoring, compatible replacement selection, recovery attempts, and simulated financial settlement.

The system also incorporates economic governance, ensuring that recovery decisions respect configured budgets and execution constraints.

### Core idea

> An AI workflow should not necessarily stop just because one of its agents fails. It should be able to detect the failure, evaluate recovery options, replace the failed agent when possible, and continue from where it left off.

---

## ✨ Key Features

### 1. Agent Registry and Version Management

Maintain a centralized registry of available agents.

- Register new agents and agent versions.
- Track agent capabilities and supported operations.
- Maintain provider and model configuration.
- Support version-specific agent assignments.
- Discover compatible agents for workflow execution.

### 2. Workflow Orchestration

Create and execute structured multi-agent workflows.

Three predefined workflow templates are provided:

| Workflow | Execution stages |
|---|---|
| Research Workflow | Research → Format → Summarize |
| Development Workflow | Plan → Code → Validate |
| Data Workflow | Extract → Transform → Review |

Users can configure ordered workflow stages and assign suitable agents to individual operations.

### 3. Intelligent Failure Detection

Monitor workflow execution and identify controlled failure conditions.

Supported failure scenarios include:

- Agent crashes.
- Heartbeat loss.
- Runtime timeouts.
- Invalid outputs.
- Tool failures.
- Backup agent failures.
- Shared failures.
- Recovery exhaustion.
- Insufficient recovery budget.
- Unavailable compatible replacements.

### 4. Compatible Agent Replacement

When an agent fails, AgentBailout evaluates whether another registered agent can perform the required operation.

The recovery mechanism considers:

- Required operation.
- Agent capabilities.
- Compatibility requirements.
- Recovery pool configuration.
- Maximum recovery attempts.
- Available recovery budget.

If an eligible replacement is available, the system attempts to continue the failed workflow stage using that agent.

### 5. Bounded Recovery and Fault Tolerance

Recovery should not continue indefinitely.

AgentBailout incorporates:

- Configurable recovery attempt limits.
- Failure tracking.
- Circuit-breaking mechanisms.
- Cancellation fencing.
- Persistent recovery attempts.
- Safe handling of interrupted executions.

These mechanisms help prevent repeated unsuccessful recovery operations and protect execution consistency.

### 6. Economic Governance

AgentBailout introduces an economic decision layer to control recovery expenditure.

Before attempting recovery, the system evaluates the configured recovery budget and applicable execution constraints.

Features include:

- Simulated recovery budgets.
- Recovery cost tracking.
- Budget enforcement.
- Idempotent settlement.
- Refund handling.
- Double-entry ledger.
- Execution and recovery metrics.

The financial ledger is a simulation used to demonstrate economic governance. It does not process actual payments.

### 7. Baseline vs Protected Execution

One of the central features of AgentBailout is its ability to compare execution with and without recovery protection.

**Baseline execution:**
- Recovery protection disabled.
- Controlled failure introduced.
- Execution stops when the failure cannot be handled.

**Protected execution:**
- AgentBailout protection enabled.
- Failure detection activated.
- Compatible replacement evaluated.
- Recovery attempted within configured constraints.

The Comparison Lab provides a way to examine the differences between these execution modes under controlled fault scenarios.

### 8. Interactive Monitoring Dashboard

A Streamlit-based dashboard provides visibility into the entire execution lifecycle.

The dashboard includes:

| Section | Functionality |
|---|---|
| Live Execution | Create tasks, configure failures, and monitor execution |
| Workflow Builder | Configure ordered workflow stages |
| Agent Registry | View and manage registered agents |
| Recovery Pool | Inspect available replacement agents |
| Comparison Lab | Compare baseline and protected execution |

Additional monitoring includes execution events, recovery information, economic decisions, ledger entries, metrics, and final task outputs.

---

## 🏗️ System Architecture

AgentBailout follows a modular backend architecture with a centralized execution and recovery control layer.

### High-level architecture

```text
                    USER
                     |
                     v
             STREAMLIT DASHBOARD
                     |
                     v
                FASTAPI
                BACKEND
                     |
                     v
             TASK MANAGEMENT
                     |
                     v
             WORKFLOW ENGINE
                     |
                     v
              AGENT REGISTRY
                     |
                     v
             EXECUTION ENGINE
                     |
                     v
              AGENT SUPERVISOR
                     |
              +------+------+
              |             |
              v             v
         EXECUTION       FAILURE
          SUCCESS       DETECTION
              |             |
              |             v
              |       RECOVERY ENGINE
              |             |
              |             v
              |      COMPATIBILITY CHECK
              |             |
              |             v
              |       RECOVERY POOL
              |             |
              |             v
              |      ECONOMIC DECISION
              |             |
              |             v
              |      AGENT REPLACEMENT
              |             |
              +------+------+
                     |
                     v
              TASK CONTINUATION
                     |
                     v
              LEDGER SETTLEMENT
                     |
                     v
                FINAL OUTPUT
```

### Main backend components

| Component | Responsibility |
|---|---|
| `backend/main.py` | FastAPI application and API endpoints |
| `backend/supervisor.py` | Task supervision and execution coordination |
| `backend/execution_engine.py` | Workflow execution operations |
| `backend/registry.py` | Agent and workflow registry |
| `backend/workflows.py` | Workflow creation and configuration |
| `backend/recovery.py` | Recovery-related functionality |
| `backend/solvency.py` | Economic and budget constraints |
| `backend/ledger.py` | Simulated financial transactions |
| `backend/database.py` | Database engine and session management |
| `backend/migrations.py` | Database migration handling |
| `backend/models.py` | Database models |
| `backend/schemas.py` | Request and response schemas |
| `backend/watchdog.py` | Runtime monitoring functionality |
| `backend/providers.py` | Agent provider integrations |

The architecture separates task management, execution, recovery, agent registration, and economic governance to keep the system modular and extensible.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11+ | Core application development |
| FastAPI | Backend REST API |
| Uvicorn | ASGI application server |
| Streamlit | Interactive frontend dashboard |
| SQLAlchemy | Database ORM |
| SQLite | Persistent local database |
| Pydantic | Data validation and schemas |
| HTTPX | HTTP communication |
| Plotly | Data visualization |
| Pytest | Automated testing |
| JSON Schema | Structured output validation |

---

## 📂 Project Structure

```text
AgentBailout/
│
├── backend/
│   ├── agents/
│   │   ├── formatter.py
│   │   ├── research.py
│   │   └── synthesis.py
│   │
│   ├── config.py
│   ├── contracts.py
│   ├── database.py
│   ├── execution_engine.py
│   ├── ledger.py
│   ├── main.py
│   ├── migrations.py
│   ├── models.py
│   ├── providers.py
│   ├── recovery.py
│   ├── registry.py
│   ├── schemas.py
│   ├── solvency.py
│   ├── supervisor.py
│   ├── watchdog.py
│   └── workflows.py
│
├── dashboard/
│   └── app.py
│
├── scripts/
│   ├── demo_phase4.py
│   ├── verify_dashboard.py
│   └── verify_phase4_dashboard.py
│
├── tests/
│   ├── test_api.py
│   ├── test_ledger.py
│   ├── test_phase4.py
│   ├── test_pipeline.py
│   └── test_recovery.py
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── ECONOMIC_MODEL.md
│   ├── HACKATHON_PROGRESS.md
│   ├── INSTALLATION.md
│   ├── PHASE2.md
│   ├── PHASE3.md
│   ├── PHASE4.md
│   └── PHASE4_TEST_REPORT.md
│
├── .env.example
├── .gitignore
├── requirements.txt
├── requirements-lock.txt
└── README.md
```

---

## 💻 Installation and Setup

### Prerequisites

Before installing AgentBailout, ensure that you have:

- Python 3.11 or newer.
- Git.
- Visual Studio Code (recommended).
- Internet connectivity for initial dependency installation.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AgentBailout.git
```

Navigate to the project directory:

```bash
cd AgentBailout
```

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the database

The project uses SQLite for local persistence.

**macOS / Linux**

```bash
export AGENTBAILOUT_DATABASE_URL="sqlite:///./agentbailout.db"
```

**Windows PowerShell**

```powershell
$env:AGENTBAILOUT_DATABASE_URL="sqlite:///./agentbailout.db"
```

The database and required schema are initialized during backend startup.

---

## ▶️ Running the Application

AgentBailout consists of two main processes:

1. FastAPI backend.
2. Streamlit dashboard.

Both must be running simultaneously.

### Terminal 1: Start the backend

Make sure your virtual environment is activated.

```bash
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8003
```

Expected output:

```text
INFO: Started server process
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8003
```

### Terminal 2: Start the dashboard

Open another terminal in the same project directory.

Activate the virtual environment.

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

Configure the backend address:

**macOS / Linux**

```bash
export AGENTBAILOUT_BACKEND_URL="http://127.0.0.1:8003"
```

**Windows PowerShell**

```powershell
$env:AGENTBAILOUT_BACKEND_URL="http://127.0.0.1:8003"
```

Start Streamlit:

```bash
python -m streamlit run dashboard/app.py --server.port 8501 --server.address 127.0.0.1
```

### 5. Open AgentBailout

Once both processes are running, access:

| Service | URL |
|---|---|
| AgentBailout Dashboard | http://localhost:8501 |
| FastAPI Backend | http://127.0.0.1:8003 |
| Interactive API Documentation | http://127.0.0.1:8003/docs |
| Backend Health Check | http://127.0.0.1:8003/health |

---

## 🧪 How to Use AgentBailout

### Step 1: Open Live Execution

Navigate to the Live Execution section of the dashboard.

Enter a task prompt.

Example:

```text
Plan a community garden with a measurable pilot.
```

### Step 2: Select a workflow template

Choose one of the available templates:

- Research → Format → Summarize
- Plan → Code → Validate
- Extract → Transform → Review

### Step 3: Configure the agents

Expand the ordered stages and agents section.

Select the agent responsible for each workflow stage.

### Step 4: Configure failure scenarios

Choose a controlled failure scenario.

For example:

```text
Failure scenario: crash
Fault stage: 2
```

This configures a controlled crash at the second workflow stage.

### Step 5: Enable AgentBailout protection

Turn on the AgentBailout protection toggle.

Configure:

- Recovery pool.
- Maximum recovery attempts.
- Recovery budget.
- Stage timeout.

### Step 6: Create and execute the task

Click **Create Task**.

Select the created task from Task History.

Click **Start Task** to begin execution.

### Step 7: Observe recovery

Monitor the execution status, failure events, recovery attempts, economic decisions, and final task output.

### Step 8: Compare execution modes

Navigate to the Comparison Lab to evaluate baseline and protected execution under controlled fault scenarios.

---

## 🔌 API Documentation

AgentBailout exposes REST API endpoints through FastAPI.

The interactive Swagger documentation is available at:

```text
http://127.0.0.1:8003/docs
```

### Main API capabilities

| Endpoint | Method | Purpose |
|---|---|---|
| `/health` | GET | Check backend health |
| `/tasks` | GET | Retrieve tasks |
| `/tasks` | POST | Create a task |
| `/tasks/{task_id}` | GET | Retrieve task details |
| `/tasks/{task_id}/start` | POST | Start task execution |
| `/tasks/{task_id}/events` | GET | Retrieve execution events |
| `/tasks/{task_id}/inject-failure` | POST | Inject a controlled failure |
| `/tasks/{task_id}/ledger` | GET | Retrieve ledger information |
| `/metrics` | GET | Retrieve execution metrics |
| `/agents` | GET / POST | Retrieve and register agents |
| `/workflows` | GET / POST | Retrieve and create workflows |
| `/comparisons` | GET / POST | Retrieve and create comparisons |
| `/tasks/{task_id}/execution` | GET | Retrieve execution details |

For complete request and response schemas, refer to the Swagger documentation.

---

## 🧾 Economic Model

A distinguishing feature of AgentBailout is its economically governed recovery mechanism.

Instead of assuming that every failure should automatically trigger replacement, the system evaluates recovery against configured financial constraints.

The simulated ledger demonstrates:

- Financial allocations.
- Recovery-related expenditure.
- Debit and credit entries.
- Refund handling.
- Settlement.
- Idempotent transaction processing.

### Why is this important?

In real-world AI systems, replacing an agent may involve additional API calls, computational resources, and execution time.

An effective recovery mechanism should consider whether the expected recovery is financially justified.

**Note:** The current ledger is simulated. It does not represent real-world payments, actual provider billing, or verified monetary savings.

---

## 🧪 Testing

AgentBailout includes automated tests for important backend and execution components.

Run the complete test suite:

```bash
python -m pytest -q --basetemp=.test-tmp
```

The tests cover areas including:

- API behavior.
- Agent execution.
- Workflow pipeline.
- Recovery logic.
- Ledger operations.
- Phase 4 functionality.

Additional verification scripts are available.

Run these with the backend running on port 8003:

```bash
python scripts/demo_phase4.py
```

```bash
python scripts/verify_dashboard.py
```

```bash
python scripts/verify_phase4_dashboard.py
```

The test suite uses temporary databases for its automated tests.

---

## 📊 Current Implementation Status

AgentBailout has reached its Phase 4 implementation checkpoint.

| Capability | Status |
|---|---|
| Agent registry | Implemented |
| Agent version management | Implemented |
| Workflow templates | Implemented |
| Ordered workflow execution | Implemented |
| AgentBailout protection ON/OFF | Implemented |
| Controlled failure injection | Implemented |
| Failure monitoring | Implemented |
| Compatibility-based recovery | Implemented |
| Bounded recovery attempts | Implemented |
| Circuit-breaking mechanisms | Implemented |
| Cancellation fencing | Implemented |
| Persistent execution tracking | Implemented |
| Simulated double-entry ledger | Implemented |
| Budget enforcement | Implemented |
| Baseline vs protected comparison | Implemented |
| Streamlit dashboard | Implemented |
| Live provider execution verification | Not yet established |

The current system is designed as a local, single-process execution engine with sequential workflow execution.

Offline deterministic simulations allow the core functionality to be demonstrated without depending on paid external services.

---

## ⚠️ Limitations

AgentBailout is an active development project, and several areas require further improvement before production deployment.

Current limitations include:

- Local, single-process architecture.
- Sequential workflow execution rather than distributed parallel execution.
- No production-grade authentication or authorization.
- No distributed task queue.
- No arbitrary DAG-based workflow execution.
- Limited semantic validation of generated content.
- Simulated rather than real financial settlement.
- No guarantee that a replacement agent will always be available.
- External provider execution requires appropriate configuration and validation.

Schema validation ensures that outputs follow expected structures; it does not guarantee factual correctness.

The system should be treated as a development and demonstration platform rather than a production-ready distributed orchestration service.

---

## 🔮 Future Roadmap

The long-term vision is to evolve AgentBailout into a scalable, intelligent, and economically optimized control plane for autonomous agent ecosystems.

### Phase 5 – Intelligent Recovery and Optimization

- Cost-optimized execution strategies.
- Time-optimized execution strategies.
- Balanced recovery decisions.
- Verified agent repairs.
- Recovery memory.
- Improved replacement selection.

### Phase 6 – Dashboard Redesign

- Improved user experience.
- Advanced execution visualization.
- More detailed recovery analytics.
- Enhanced workflow monitoring.

### Phase 7 – Documentation and Presentation

- Complete architecture documentation.
- Improved technical documentation.
- Demonstration workflows.
- Developer guides.

### Phase 8 – Validation and Release

- Comprehensive regression testing.
- Performance evaluation.
- Reliability validation.
- Final release preparation.

---

## 💡 Why AgentBailout Matters

As AI agent systems become more complex, their reliability becomes increasingly important.

A workflow that can perform complex tasks but cannot handle individual component failures is difficult to trust in critical applications.

AgentBailout explores a different approach:

**Do not simply execute agents. Manage their reliability.**

By combining execution monitoring, compatible agent replacement, bounded recovery, and economic governance, AgentBailout aims to make multi-agent workflows more resilient and operationally sustainable.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Add or update tests.
5. Submit a pull request.

Please ensure existing functionality and regression tests remain intact.

---

## 👨‍💻 Project Information

**Project:** AgentBailout

**Category:** AI Agent Orchestration / Fault Tolerance / Intelligent Recovery

**Current checkpoint:** Phase 4

**Primary language:** Python

**Interface:** Streamlit

**Backend:** FastAPI

**Database:** SQLite

---

## 📜 License

A license has not yet been specified.

Before making this repository public, choose and add an appropriate open-source license if you intend to permit reuse, modification, and redistribution.

---

### AgentBailout

**Detect. Diagnose. Decide. Repair. Replace. Recover.**

*Building more resilient and economically governed AI agent workflows.*
