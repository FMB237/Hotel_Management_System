# Hotel Management System - Backend

> TechSkillHub Internship Project by Bruce Fouenang Miguel
> FastAPI backend for hotel/hostel management with RBAC, JWT auth, rooms, complaints, notices and dashboard.

## Overview

This is the backend service for the Hotel Management System built during TechSkillHub Internship. It provides authentication, user profiles, room management, complaint ticketing, notices/announcements with Role-Based Access Control, and a dashboard API.

The project started as a simple FastAPI + SQLite setup and evolved into a modular backend with:
- JWT OAuth2 authentication
- Password hashing with Passlib/Bcrypt
- SQLAlchemy 2.0 ORM
- Pydantic schemas
- File handling for profile uploads
- Modular routers: auth, users, room, complaint, notice, dashboard

## Tech Stack

- **Framework**: FastAPI 0.139+
- **Database**: SQLite `hostel.db` via SQLAlchemy
- **Auth**: JWT HS256 with `python-jose`, OAuth2 Password Flow
- **Security**: Passlib[bcrypt]
- **Validation**: Pydantic
- **Server**: Uvicorn
- **Templates**: Jinja2
- **File Uploads**: python-multipart, aiofiles
- **Env**: python-dotenv

## Project Structure

```
backend/
├── database.py          # SQLAlchemy engine & SessionLocal
├── main.py              # FastAPI app entry, router inclusion
├── requirements.txt
├── Procfile             # Render/Heroku deploy command
├── hostel.db            # SQLite database
├── models/
│   ├── user.py
│   ├── room.py
│   ├── complaint.py
│   └── notice.py
├── schemas/
│   ├── user.py
│   ├── room.py
│   ├── complaint.py
│   ├── notice.py
│   └── dashboard.py
├── routes/
│   ├── auth.py          # login, register, secure routes
│   ├── users.py         # user profile management
│   ├── room.py          # room CRUD
│   ├── complaint.py     # ticketing system
│   ├── notice.py        # announcements with RBAC
│   └── dashboard.py     # aggregated data
└── utils/
    ├── security.py      # password hashing
    ├── jwt.py           # token creation/validation
    ├── jwt_oauth2.py    # OAuth2 scheme
    └── file_handler.py  # profile uploads
```

## Setup Instructions

Based on the original development notes from `Personal.md`:

1. Create virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` from example
   ```bash
   cp ../.env.example .env
   # Edit SECRET_KEY and DATABASE_URL
   ```

4. Run the server
   ```bash
   uvicorn main:app --reload --port 8000
   ```

5. API docs available at `http://localhost:8000/docs`

## Environment Variables

Create `.env` at project root:
```
SECRET_KEY=your-super-secret-random-string-here
DATABASE_URL=sqlite:///./hostel.db
```

`.env` is gitignored.

## Features

### Authentication
- Register / Login with JWT
- Password hashing with bcrypt
- Secure routes with OAuth2 dependency
- httpOnly cookie support

### Users
- User profiles with avatar upload to `uploads/profiles/`
- Role-based access: Admin, Staff, Guest

### Rooms
- CRUD for rooms
- Availability tracking
- Booking constraints

### Complaints
- Ticketing system for guests
- Status workflow

### Notices
- Admin-only create/read/update/delete
- RBAC enforced

### Dashboard
- Aggregated stats for admin overview

## API Routes

- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`
- `GET /users/`
- `POST /rooms/`
- `GET /rooms/`
- `POST /complaints/`
- `GET /notices/`
- `POST /notices/` [Admin only]
- `GET /dashboard/stats`

See `/docs` for full OpenAPI spec.

## Development Notes

From Personal.md timeline:
- Started with FastAPI + SQLite setup
- Added models, schemas, routes modularization
- Implemented JWT + security utils
- Added file handling for profiles
- Added RBAC for notices
- Dashboard module added last
- Deployment prep: requirements minimalized, Procfile added, backend folder as service root for Render

## Deployment

Procfile:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

Deploy backend folder as root on Render/Railway. Database is SQLite for now; switch `DATABASE_URL` to Postgres for production.

## License

Personal project for TechSkillHub Internship.

---
Built with FastAPI in my heart ❤️
