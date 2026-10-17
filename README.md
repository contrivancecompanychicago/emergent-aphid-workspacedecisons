# Emergent APHID — Backend (version 0)

This repository has been converted from a static SwaggerHub-based API documentation site into a FastAPI backend scaffold for the Emergent APHID Health Employees onboarding project.

Version: 0

Quickstart

1. Create a Python virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the app (development):

```bash
uvicorn app.main:app --reload
```

3. The OpenAPI docs will be available at http://127.0.0.1:8000/docs

What I changed

- Removed SwaggerHub templating from README and index.html (the site previously contained embedded Swagger templates).
- Added a FastAPI scaffold in `app/` with a simple onboarding model and CRUD endpoints.
- Added SQLite default DB configuration (data/db.sqlite) and database helper.
- Added tests, Dockerfile, and requirements.txt.

Notes

- Database: by default the app uses SQLite for quick local development. For production, switch DATABASE_URL in the environment to a Postgres instance and update the engine URL accordingly.
- If you want me to close or comment on the existing issues/PRs referencing Swagger/SwaggerHub, tell me and I will close them with a short note saying the integration was removed.
