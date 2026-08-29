# The routes for our rooms 
from fastapi import FastAPI,APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from database import get_db
from models.room import Room,Hostel
from schemas.room import RoomCreate,RoomResponse,HostelCreate,HostelResponse


router = APIRouter(prefix="/hostels", tags=["Hostels & Rooms"])

# Let create a new Hostel 

@router.post("/",response_model=HostelResponse,status_code=201)
def create_hostel(hostel:HostelCreate,db: Session = Depends(get_db)):
    new_hostel = Hostel(**hostel.model_dump())
    db.add(new_hostel)
    db.commit()
    db.refresh(new_hostel)
    return new_hostel

# Get all the hostels
@router.get("/",response_model=list[HostelResponse])
def get_hostel(db:Session = Depends(get_db)):
    return db.query(Hostel).all()

#Let create a new room

@router.post("/rooms",response_model=RoomResponse,status_code=201)
def create_room(room:RoomCreate,db:Session = Depends(get_db)):
    hostel = db.query(Hostel).filter(Hostel.id == room.hostel_id).first()
    if not hostel:
        raise HTTPException(status_code=404,detail="Hostel not found")
    new_room = Room(**room.model_dump())
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

# Let get all the rooms 

@router.get("/rooms",response_model=list[RoomResponse])
def get_room(db:Session = Depends(get_db)):
    return db.query(Room).all()