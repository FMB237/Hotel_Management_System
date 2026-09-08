from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func # Import func for SQL aggregations
from database import get_db
from models.user import User
from models.room import Room
from models.complaint import Complaint
from schemas.dashboard import DashboardStats, ChartData
from utils.jwt import get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard & Analytics"])

# 1. Get the raw numbers for the metric cards
@router.get("/stats", response_model=DashboardStats)
def get_dashboard_stats(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    # RBAC: Only admins should see the full dashboard stats
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    total_students = db.query(User).filter(User.role == "student").count()
    total_rooms = db.query(Room).count()
    
    # A room is "occupied" if it has at least 1 person
    occupied_rooms = db.query(Room).filter(Room.current_occupancy > 0).count()
    
    # A room is "available" if the is_available flag is True
    available_rooms = db.query(Room).filter(Room.is_available == True).count()
    
    pending_complaints = db.query(Complaint).filter(Complaint.status == "Pending").count()
    total_complaints = db.query(Complaint).count()

    return {
        "total_students": total_students,
        "total_rooms": total_rooms,
        "occupied_rooms": occupied_rooms,
        "available_rooms": available_rooms,
        "pending_complaints": pending_complaints,
        "total_complaints": total_complaints
    }

# 2. Get the formatted data for Chart.js
@router.get("/charts", response_model=ChartData)
def get_dashboard_charts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    # --- PIE CHART DATA (Occupancy Ratio) ---
    occupied = db.query(Room).filter(Room.current_occupancy > 0).count()
    available = db.query(Room).filter(Room.is_available == True).count()
    occupancy_ratio = {"occupied": occupied, "available": available}

    # --- BAR CHART DATA (Monthly Complaints) ---
    # We use SQLite's strftime function to group complaints by month
    monthly_data = db.query(
        func.strftime('%Y-%m', Complaint.created_at).label("month"),
        func.count(Complaint.id).label("count")
    ).group_by("month").order_by("month").all()

    # Format the SQL result into a clean list of dictionaries for Chart.js
    monthly_complaints = [{"month": row.month or "Unknown", "count": row.count} for row in monthly_data]

    return {
        "occupancy_ratio": occupancy_ratio,
        "monthly_complaints": monthly_complaints
    }