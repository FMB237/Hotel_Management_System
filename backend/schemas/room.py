# Schemas of the room.py file 
from pydantic import BaseModel,ConfigDict
from typing import Optional

# Let Create our hostel
class HostelCreate(BaseModel):
    name: str
    location: str
    gender : str

# Move to HostelResponse

class HostelResponse(HostelCreate):
    id: int
    
    model_config= ConfigDict(from_attributes=True)
# Let moveto the Room Schemas

class RoomCreate(BaseModel):
    room_number: int
    capacity: int
    hostel_id: int

class RoomResponse(RoomCreate):
    id:int
    current_occupancy: int
    is_available:bool

    model_config = ConfigDict(from_attributes=True)
