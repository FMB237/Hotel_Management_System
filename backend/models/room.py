# Login for handling user rooms into our app
from sqlalchemy import Column,Integer,String,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from database import Base

# Now let design our hostels class
class Hostel(Base):
    __tablename__= "hostels"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False,unique=True)
    location = Column(String,nullable=False)
    gender = Column(String,nullable=False)


    # Let define the relationship between hostels an rooms 

    rooms = relationship("Room",back_populates="hostel")

# Let now move to the room class
class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer,primary_key=True,index=True)
    room_number = Column(String,nullable=False)
    capacity = Column(String,nullable=False)
    current_occupancy = Column(Integer,default=0)
    is_available = Column(Boolean,default=True)

    # Now let link our rooms and to a specific hostel 

    hostel_id = Column(Integer,ForeignKey("hostels.id"),nullable=False)

    hostel = relationship("Hostel",back_populates="rooms")