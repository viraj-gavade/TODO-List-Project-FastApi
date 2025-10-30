# TODO List Project (FastAPI + React)

This is a small Todo List application built with a FastAPI backend and a React + Vite frontend. It was created as a learning project to practice building full-stack applications with Python and modern frontend tooling.

Features
- Backend (FastAPI):
  - REST endpoints for tasks: create, read (all / single), update, delete, and toggle completion.
  - Uses SQLAlchemy models, dependency-injected DB sessions, and simple auth middleware (in the repo).
- Frontend (React + Vite):
  - Functional components with hooks (useState, useEffect).
  - Axios-based API wrapper for all endpoints.
  - TailwindCSS for styling (with PostCSS + Vite).
  - Task list UI: create, update, delete, toggle completion, and human-friendly date display.

This repository is intended for learning and experimentation. It is not production hardened.

## Repository layout

- `Client/` — React frontend built with Vite
  - `src/` — React source files (components, services)
  - `tailwind.config.cjs`, `postcss.config.cjs`, `src/styles.css` — Tailwind setup
- `Server/` — FastAPI backend
  - `main.py` — Application entry (CORS middleware + routers)
  - `routes/`, `controllers/`, `models/`, `schema/`, `DataBase/` — server code

## Quick start (Windows PowerShell)

Prerequisites:
- Node.js + npm (for frontend)
- Python 3.10+ (for backend)

1. Start the backend

```powershell
cd 'D:\FastApi\TODO List Project\Server'
# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# Install backend dependencies. If you don't have a requirements.txt, install core packages:
pip install fastapi uvicorn sqlalchemy pydantic
# Start the backend
uvicorn main:app --reload
```

Notes:
- The backend includes CORS middleware configured for the Vite dev server (ports 5173/5174) so the frontend can call the API during development.

2. Start the frontend

```powershell
cd 'D:\FastApi\TODO List Project\Client'
npm install
npm run dev
```

Open the Vite printed URL in your browser (e.g. `http://localhost:5173` or `http://localhost:5174`). The app will call the backend at `VITE_API_BASE` (defaults to `http://127.0.0.1:8000`). To change it, create a `Client/.env` file with:

```
VITE_API_BASE=http://127.0.0.1:8000
```

## Tailwind & PostCSS

Tailwind is already configured in `Client/tailwind.config.cjs` and the directives are in `Client/src/styles.css`. If you install dependencies and run the frontend dev server, Tailwind will be processed by PostCSS automatically via Vite.

If you see a Tailwind "content" warning, ensure `tailwind.config.cjs` contains correct paths (this repo uses absolute paths via `path.resolve`).

## CORS troubleshooting

- Browsers send an `Origin` header on cross-origin requests; tools like Postman or curl do not. The FastAPI CORS middleware only adds `Access-Control-Allow-Origin` when the request contains an `Origin` header that matches the allowed origins.
- If you get a browser CORS error like `No 'Access-Control-Allow-Origin' header is present`, check that:
  1. The backend is running and configured with `CORSMiddleware`.
 2. The exact origin (including port) is listed in `allow_origins`, or you temporarily set `allow_origins=["*"]` for development.

## Development notes
- This project was built for learning. Things that can be improved:
  - Add automated tests for backend and frontend
  - Add production-ready configuration and proper secret management
  - Harden authentication and validation
  - Replace simple notifications with a toast library for better UX

If you'd like, I can help add tests, improve UI polish (ShadCN integration), or convert the frontend to TypeScript.

---

Thanks for checking out this learning project — have fun exploring and modifying it!
