# Hotel Management System

TechSkillHub Internship Project by Bruce Fouenang Miguel

A full-stack hotel/hostel management system with FastAPI backend and frontend. Built with modular architecture, JWT authentication, RBAC, and SQLite.

## Structure

```
Hotel_Management_System/
├── backend/          # FastAPI backend
│   ├── main.py
│   ├── database.py
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   └── utils/
├── frontend/         # Frontend app
└── Personal.md       # Development notes
```

## Quick Start

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env
uvicorn main:app --reload
```

API docs: http://localhost:8000/docs

See `backend/README.md` for full backend documentation.

## Features
- JWT OAuth2 authentication
- User profiles with avatar upload
- Room management
- Complaint ticketing
- Notices with RBAC
- Dashboard analytics

## Tech Stack
FastAPI, SQLAlchemy, SQLite, Pydantic, Passlib, python-jose, Jinja2

## Development Notes
See `Personal.md` for step-by-step build history.

---
Built for TechSkillHub Internship
