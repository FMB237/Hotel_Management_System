# Principal Fastapi File
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine,Base
from models.user import User

# Let import all the models for our application 

import models.user
import models.room
import models.complaint
import models.notice

# Let import our routes 
from routes.auth import router as auth_router
from routes.room import router as room_router
from routes.complaint import router as complaint_router
from routes.users import router as user_router
from routes.notice import router as notice_router
from routes.dashboard import router as dashboard_router


app=FastAPI(title="Hotel_Management_System",version="1.0.0")

# Let add this simple cors block 
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])


Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(room_router)
app.include_router(complaint_router)
app.include_router(user_router)
app.include_router(notice_router)
app.include_router(dashboard_router)

@app.get("/")
def home():
    return {
        "message":"Hotel_management_system"
    }