# Schemas of the complaint.py file 

from pydantic import BaseModel,ConfigDict
from typing import Optional
from models.complaint import ComplaintStatus,PriorityLevel

# Let create our ComplaintCreation 
class ComplaintCreate(BaseModel):
    title : str
    description: str
    priority : PriorityLevel = PriorityLevel.LOW
    proof_image: Optional[str] = None

class ComplaintUpdate(BaseModel):
    status : ComplaintStatus
    priority : PriorityLevel

# Let do the complaint response 

class ComplaintResponse(BaseModel):
    id:int
    title: str
    description: str
    status : ComplaintStatus
    priority : PriorityLevel
    proof_image : Optional[str] = None
    user_id : int 

    model_config = ConfigDict(from_attributes=True)