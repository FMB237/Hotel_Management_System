# Principal Fastapi File
from fastapi import FastAPI
from database import engine,Base
from models.user import User

# Let import all the models for our application 

import models.user
import models.room
import models.complaint

# Let import our routes 
from routes.auth import router as auth_router
from routes.room import router as room_router
from routes.complaint import router as complaint_router



app=FastAPI(title="Hotel_Management_System",version="1.0.0")


Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(room_router)
app.include_router(complaint_router)

@app.get("/")
def home():
    return {
        "message":"Hotel_management_system"
    }