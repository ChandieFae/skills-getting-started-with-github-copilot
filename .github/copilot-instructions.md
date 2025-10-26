## Purpose
This file gives concise, actionable guidance to AI coding agents working in this repository so they can be immediately productive.

## Big picture
- This is a minimal FastAPI application located at `src/app.py` that serves two API endpoints and a static single-page UI under `src/static/`.
- Data is stored in-memory in the `activities` dict (see `src/app.py`) — no database is present. Changes are ephemeral and reset when the process restarts.

## Key files and what they do
- `src/app.py` — FastAPI app. Mounts static files at `/static` and exposes:
  - `GET /activities` — returns the full `activities` dict.
  - `POST /activities/{activity_name}/signup?email=...` — appends the email to the activity's `participants` list.
  - `/` redirects to `/static/index.html` (the UI).
- `src/static/index.html`, `src/static/app.js`, `src/static/styles.css` — frontend UI that consumes the API.
- `requirements.txt` — lists `fastapi` and `uvicorn` used in development.

## How to run locally (developer workflow)
1. Create a Python environment and install deps:
   - `pip install -r requirements.txt`
2. Run the dev server (recommended):
   - `uvicorn src.app:app --reload --port 8000`
   Note: the repository README suggests `python app.py`, but `src/app.py` does not start a server itself — use `uvicorn` to run the FastAPI app.
3. Open API docs: `http://localhost:8000/docs` and UI: `http://localhost:8000/static/index.html`

## Common, concrete edits and examples
- To add a new activity: modify the `activities` dict in `src/app.py` (or implement persistent storage).
- To change the API shape, update `src/app.py` handlers and update the UI calls in `src/static/app.js` accordingly.

Example curl calls (use these when testing or writing integration snippets):

```
curl http://localhost:8000/activities

curl -X POST "http://localhost:8000/activities/Chess%20Club/signup?email=student@example.com"
```

## Project-specific conventions & patterns
- Activity identifier: activity names are used as keys in the in-memory store (e.g., "Chess Club"). Keep API consumers aware: spaces are allowed and should be URL-encoded.
- Student identifier: email strings are used as the stable identifier for participants.
- No persistence: assume all data is volatile unless you add a DB file and wire it up. When adding persistence, keep the external API compatible (same response shapes) unless explicitly versioning the API.

## Integration & external dependencies
- Only FastAPI and Uvicorn are required. No external services or environment variables are currently used.

## Debugging notes
- When verifying behavior, check `http://localhost:8000/docs` for expected request/response models.
- Static UI resources are served at `/static/*` — open `/static/index.html` to exercise the frontend.

## When changing behavior
- Update `src/README.md` with new developer instructions if you change how the app is run (for example, adding Docker or a database).
- Add small, focused tests when you introduce non-trivial logic (there are no tests in the repo now).

## Where to look next
- Start with `src/app.py`, the single source of truth for API behavior and `src/static/app.js` for frontend integration points.

---
If anything here is unclear or you'd like the instructions to include CI, Docker, or a recommended test harness, tell me which one and I will add it.
