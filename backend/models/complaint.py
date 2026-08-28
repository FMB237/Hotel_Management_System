# File for handling tickets 
# Let Do our imports
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Enum as SAEnum,func,DateTime
from sqlalchemy.orm import relationship
from database import Base
import enum

class ComplaintStatus(str,enum.Enum):
    PENDING = "Pending"
    PROCESSING = "Processing"
    RESOLVED ="Resolved"
    REJECTED = "Rejected"

class  PriorityLevel(str,enum.Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Complaint(Base):
    __tablename__="complaints"

    id= Column(Integer,index=True,primary_key=True)
    title = Column(String,nullable=False)
    description = Column(String,nullable=False)
    status = Column(SAEnum(ComplaintStatus),default=ComplaintStatus.PENDING)
    priority = Column(SAEnum(PriorityLevel),default=PriorityLevel.LOW)
    proof_image = Column(String,nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now())

    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)

    user = relationship("User",backref="complaints")
    