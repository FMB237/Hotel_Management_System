# Principal Fastapi File

from fastapi import FastAPI
from database import engine,Base
from models.user import User


app=FastAPI(title="Hotel_Management_System",version="1.0.0")


Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message":"Hotel_management_system"
    }