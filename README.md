# 🏠 Smart Hostel & Student Management System

> A full-stack hostel management platform with secure authentication, room allocation, complaint ticketing, announcements, and a real-time analytics dashboard — built with **FastAPI**.

**🌍 Live API:** https://hotel-management-system-pd7b.onrender.com
**📚 Interactive Docs (Swagger):** https://hotel-management-system-pd7b.onrender.com/docs

---

## 📖 About the Project

Developed during my **TechSkillHub Full Stack Development Internship** (02 Aug – 02 Oct 2026, Intern ID: TSH/A759791F), this system solves real-world hostel management problems for both students and administrators.

- **Student Module:** Registration, login, profile & picture upload, complaint filing with proof images, notice board access.
- **Admin Module:** Hostel/room management, complaint handling with priority assignment, notice publication, analytics dashboard.
- **Analytics:** Real-time occupancy metrics, complaint statistics, and Chart.js-ready data endpoints.

---

## 🛠️ Tech Stack

| Layer      | Technologies |
|------------|--------------|
| Backend    | FastAPI, Uvicorn, SQLAlchemy, Pydantic v2 |
| Database   | SQLite |
| Security   | JWT (python-jose), bcrypt (passlib), HTTPBearer, RBAC |
| Files      | python-multipart, aiofiles |
| Deployment | Render, Git/GitHub, Procfile, .env |

---

## ✨ Features

- 🔐 **Authentication & Security** — JWT login, bcrypt password hashing, role-based access control (Admin/Student), protected routes.
- 🏠 **Hostel Management** — Create hostels, add rooms, track capacity and occupancy, availability flags.
- 🎫 **Complaint System** — Students lodge complaints with proof image uploads; admins assign priority (Low/Medium/High) and status (Pending → Processing → Resolved/Rejected).
- 📢 **Notice Board** — Admin-only create/update/delete, pinned notices, active/inactive control.
- 👤 **User Profiles** — Profile viewing and profile picture upload.
- 📊 **Analytics Dashboard** — Total students/rooms, occupied vs available rooms, pending complaints, monthly complaint trends grouped via SQL aggregation.
- 🌐 **RESTful API** — Auto-generated Swagger docs, proper HTTP status codes, JSON responses.

---

## 📁 Project Structure

```
Hotel_Management_System/
├── backend/
│   ├── models/          # SQLAlchemy tables (user, room, complaint, notice)
│   ├── schemas/         # Pydantic validation schemas
│   ├── routes/          # API routers (auth, room, complaint, notice, users, dashboard)
│   ├── utils/           # security.py, jwt.py, file_handler.py
│   ├── uploads/         # Stored profile & complaint images
│   ├── main.py          # FastAPI entry point
│   ├── database.py      # SQLite engine & session
│   ├── requirements.txt # Minimal production dependencies
│   ├── .env             # SECRET_KEY, DATABASE_URL (not committed)
│   └── Procfile         # Render start command
├── frontend/            # UI (HTML/CSS/JS)
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started (Local)

```bash
git clone https://github.com/YOUR_USERNAME/Hotel_Management_System.git
cd Hotel_Management_System/backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
echo "SECRET_KEY=your-secret-key" > .env
echo "DATABASE_URL=sqlite:///./hostel.db" >> .env
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

**Auth:** `POST /auth/register` · `POST /auth/login` · `GET /auth/me`
**Hostels/Rooms:** `POST /hostels/` · `GET /hostels/` · `POST /hostels/rooms` · `GET /hostels/rooms`
**Complaints:** `POST /complaints/` · `GET /complaints/` · `PATCH /complaints/{id}` · `POST /complaints/{id}/upload-proof`
**Notices:** `POST /notices/` · `GET /notices/` · `PUT /notices/{id}` · `DELETE /notices/{id}`
**Users:** `GET /users/profile` · `POST /users/profile-picture`
**Dashboard:** `GET /dashboard/stats` · `GET /dashboard/charts`

---

## 🌍 Deployment (Render)

- **Root Directory:** `backend` (main.py lives inside the backend folder)
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Env Vars:** `SECRET_KEY`, `DATABASE_URL` configured in the Render dashboard.

---

## 🚧 Challenges Faced & How I Solved Them

1. **SQLAlchemy `__tablename__`** — Wrote `tablename = "users"` without double underscores; queries silently failed. Fixed the dunder naming and rebuilt the DB.
2. **Pydantic class typo** — `UserReponse` vs `UserResponse` caused import/validation crashes. Learned to keep schema names consistent everywhere.
3. **`response_model` in the wrong place** — Put it as a function parameter (`def login(user_data: UserLogin, response_model=UserLogin, ...)`) which broke OpenAPI schema generation (`AttributeError: media_type`). It belongs only in the decorator.
4. **Wrong dependency on protected route** — Used `Depends(get_db)` instead of `Depends(get_current_user)` on `/auth/me`, returning 401. Learned the difference between DB sessions and auth dependencies.
5. **OAuth2PasswordBearer vs HTTPBearer** — OAuth2 form-data (`username/password`) clashed with my JSON login (`email/password`). Switched to HTTPBearer, the modern REST/JSON-friendly standard.
6. **Router prefix duplication** — `prefix="/hostels"` + `@router.post("/hostels")` created `/hostels/hostels`, causing 422 errors. Also fixed duplicate `GET /` routes and a `db.add(room)` vs `db.add(new_room)` bug.
7. **Stale SQLite database** — After model changes, the old `hostel.db` kept the broken schema; deleting it and letting `Base.metadata.create_all()` rebuild fixed lingering 401s.
8. **Dashboard schema typo** — `total_compaints` (missing "l") triggered a ResponseValidationError; matched schema fields to response keys.
9. **Deployment structure** — Render failed because `main.py` sits in `backend/`; solved with Render's **Root Directory = backend** setting plus moving `requirements.txt` and `Procfile` inside it.

---

## 🎓 What I Learned

Building this project took me from environment setup → models → schemas → password hashing → JWT auth → CRUD routes → file uploads → RBAC notices → analytics → deployment. I gained hands-on experience with REST API design, database relationships, security best practices, debugging production errors, Git workflow, and cloud deployment.

---

## 👤 Author

**Fouenang Miguel Bruce** — Engineering Student (Level 4), ENSPD
📧 miguelfouenanf@gmail.com · 📱 +677 152 543 · 📍 Douala, Cameroon
Skills: FastAPI, Flask, HTML/CSS/JS, Linux, Bash, Git, Cisco Networking, Virtualization (KVM/QEMU, VirtualBox)

---

## 🙏 Acknowledgments

Special thanks to **TechSkillHub** for the internship opportunity, mentorship, and the structured 8-week action plan that guided this project.
TSH_README_EOF
echo "✅ README.md created!" && ls -la README.md