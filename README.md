# Digital Literacy Bridge Package

This package provides an accessible web platform for digital literacy education.

## Overview

The Digital Literacy Bridge is a FastAPI-based application with a SQLAlchemy backend and an accessibility-first frontend. It supports:

- Multi-language course content via YAML
- Anonymous user progress tracking
- RESTful API
- Accessible SPA frontend

## Getting Started

From the repository root:

```bash
uv sync
uv run python -m digital_literacy_bridge.cli
```

Or:

```bash
uv run uvicorn digital_literacy_bridge.api.app:app --reload
```

Then open http://localhost:8080 (or 8000).

## Package Structure

- `api/` – FastAPI routes and models
- `config/` – settings and database configuration
- `database/` – ORM models
- `utils/` – content loader
- `frontend/` – static assets and SPA
- `content/` – YAML course files (must be created manually)

## Documentation

For full documentation, see the top-level **README-dlb.md** in the repository root.

## Development

Run tests:

```bash
uv run pytest
```

Lint and format:

```bash
uv run ruff format
uv run ruff check
uv run ty check
```

## Notes

- The `dlb` script entry point requires package installation; if not available, run the module directly as shown above.
- Database tables are created automatically on startup.
- Add course YAML files under `content/courses/` before courses appear.
