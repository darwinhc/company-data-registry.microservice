# Company Data Registry Microservice

Production-style backend microservice for managing structured company data with schema validation, audit logging, and optimized read access.

## Why this project exists

This project demonstrates how to build a maintainable backend service using Clean Architecture, metadata-driven use cases, and infrastructure adapters. It is designed as a portfolio-grade example of backend engineering practices used in real-world distributed systems.

## Key features

- REST API for company data management
- Metadata-driven use case registration
- Audit logging for traceability
- Schema validation for structured data
- Repository/adapters separation
- Unit tests with Pytest
- Docker-ready local setup
- CI workflow with automated checks

## Architecture

```text
API / Handler
   ↓
Use Case Layer
   ↓
Ports
   ↓
Adapters: Database, Audit Log, Cache, Publisher
```

## Tech stack

Python · FastAPI/Flask · MongoDB/PostgreSQL · Redis · Docker · Pytest · Clean Architecture

How to run

```bash
git clone ...
cd company-data-registry.microservice
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```


## What this demonstrates
- Backend architecture design
- Separation of business logic from infrastructure
- Testing strategy
- Maintainable service boundaries
- Production-oriented thinking

