# Cyber Guardians CTI & SOAR Platform

An early-stage development scaffold for a cyber threat intelligence (CTI) and
security orchestration, automation, and response (SOAR) platform. The planned
system brings together threat-feed ingestion, STIX 2.1 data, asynchronous
playbooks, and risk reporting.

> **Project status:** This repository currently contains a FastAPI health-check
> API, a starter Streamlit dashboard, and local development configuration.
> Threat ingestion, STIX conversion, database persistence, and SOAR workflows
> are planned capabilities and are not implemented yet.

## Planned capabilities

- Ingest MISP JSON, STIX/TAXII 2.1 feeds, and other threat-intelligence data.
- Normalize and validate threat data with Pydantic and represent it with STIX 2.1.
- Orchestrate asynchronous feed collection and response playbooks with Celery.
- Explore threat relationships using Neo4j and persist application data in PostgreSQL.
- Build a Streamlit dashboard for intelligence review and risk reporting.

## Technology

| Area | Technology |
| --- | --- |
| API | Python 3.11+, FastAPI, Uvicorn |
| Data validation and CTI formats | Pydantic v2, `stix2`, `taxii2-client` |
| Relational storage and migrations | PostgreSQL, SQLAlchemy, Alembic |
| Threat graph | Neo4j |
| Background work and broker | Celery, Redis |
| Dashboard | Streamlit |
| Tests and quality | pytest, Ruff, mypy |

## Requirements

- Python 3.11 or newer
- Docker Desktop with Docker Compose

## Local development (Windows PowerShell)

From the repository root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
Copy-Item .env.example .env
docker compose up -d
```

If PowerShell blocks virtual-environment activation, either adjust the
PowerShell execution policy for your user or run the environment's Python
directly as `.\.venv\Scripts\python.exe`.

The Compose stack starts PostgreSQL, Neo4j, and Redis. Local connection settings
are provided in `.env.example`; `.env` is ignored by Git. The credentials in
these files are **development-only defaults**. Do not expose these services to
untrusted networks or reuse these credentials outside local development.

## Run the API and dashboard

Open two PowerShell terminals, activate `.venv` in each, and run:

```powershell
uvicorn app.main:app --reload
```

```powershell
streamlit run app/dashboard.py
```

| Service | Local address |
| --- | --- |
| FastAPI | <http://127.0.0.1:8000> |
| API documentation | <http://127.0.0.1:8000/docs> |
| Health check | <http://127.0.0.1:8000/health> |
| Streamlit dashboard | <http://localhost:8501> |
| Neo4j browser | <http://localhost:7474> |

The health endpoint currently returns `{"status":"ok"}`. It is a basic
application check and does not verify connections to the data services.

## Run checks

With the development dependencies installed:

```powershell
pytest
ruff check .
mypy app
```

## Stop local services

```powershell
docker compose down
```

This preserves named volumes. To delete local database data as well, run
`docker compose down -v` only when you intentionally want to reset the
development databases.

## Repository guide

- `app/main.py` — FastAPI application and health endpoint.
- `app/core/config.py` — environment-based application settings.
- `app/dashboard.py` — Streamlit dashboard starter.
- `tests/` — automated tests.
- `docker-compose.yml` — local PostgreSQL, Neo4j, and Redis services.
- `visual_studio_copilot_system_prompt.md` — original product and architecture brief.

## Contributing

This is an active development scaffold. Before contributing, open an issue to
discuss substantial feature changes. Keep changes focused, add tests for
behavior, and run the checks above before submitting a pull request.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE).
