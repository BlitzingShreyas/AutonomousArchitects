# Actual progress

## Phase 1 — complete and verified

Implemented: SQLite models, three deterministic agents, ordered supervisor, atomic start claim, input/output persistence, UTC events, health/create/list/detail/start/events API, initial pipeline/API tests, Windows demo and Ubuntu scripts.

Initial environment: Windows PowerShell; Git 2.53.0. `python` resolves to an unusable Windows Store alias. No `py` or `uv` found. Initial Python download failed DNS resolution in the sandbox; an escalated download was requested. Runtime test results will be recorded after execution.

Verification: Python 3.12.10 installed locally; dependencies installed in `.venv`. `python -m pytest -q --basetemp=.verified-tests` passed all 4 tests in 1.81 seconds outside the sandbox. One upstream Starlette warning advises migrating its test client from httpx to httpx2; current tests pass. An earlier test run raced dependency installation and failed collection; rerun after installation passed. Sandbox runs stalled or denied sockets; local HTTP verification required escalation.

Backend startup succeeded on 127.0.0.1:8000. Live `/health` returned ok. `scripts/demo.ps1` created task `c7396d2b-7c73-4686-8535-291519dc6106`, started it, observed RUNNING then COMPLETED, and retrieved final output and all nine ordered events. All three stages completed in approximately 1.6 seconds. Temporary database tests verified persistence by disposing and reopening the database. Invalid inputs returned 422, unknown tasks 404, duplicate starts 409. Database and installer are excluded from Git.

No Phase 2 functionality has been claimed or implemented. Dashboard, watchdog, recovery, solvency and ledger remain future work. Ubuntu scripts are supplied but unverified on Linux. Phase 1 checkpoint: await CONTINUE PHASE 2.
