# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities

## Getting started (developer)

1. Create a Python environment and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the development server (recommended):

   ```bash
   uvicorn src.app:app --reload --port 8000
   ```

3. Verify the app and UI in your browser:
   - API docs (interactive): http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc
   - Frontend UI: http://localhost:8000/static/index.html

Notes:
- The project mounts static files at `/static` from `src/static/` (see `src/app.py`).
- `src/app.py` is the single source of truth for API behavior — it stores activities in-memory in the `activities` dict. Data is volatile and resets when the process restarts.

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.

## Tests

Run the minimal test suite locally:

```bash
pytest --cov=src --cov-report=term --cov-report=xml
```

The test suite uses FastAPI's TestClient and requires `httpx` (already in `requirements.txt`).

## Debugging & tips

- If you change how the server is launched (for example adding Docker), update this README and `.github/copilot-instructions.md`.
- The static UI (`src/static/index.html` + `src/static/app.js`) calls the API endpoints described above; update both backend and frontend together when changing API shapes.
