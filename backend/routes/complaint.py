# Routes for Complaint 
from fastapi import FastAPI,APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.complaint import Complaint,ComplaintStatus,PriorityLevel
from schemas.complaint import ComplaintCreate,ComplaintUpdate,ComplaintResponse,ComplaintStatus
from utils.jwt import get_current_user
from models.user import User

router = APIRouter(prefix="/compaints",tags=["Complaints"])

# Let create a Complaint 

@router.post("/",response_model=ComplaintResponse,status_code=201)
def create_complaint(complaint:ComplaintCreate,db: Session =Depends(get_db),current_user: User = Depends(get_current_user)):
    new_complaint = Complaint(**complaint.model_dump(), user_id = current_user.id)
    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)
    return new_complaint


# Let get all the complaints 

@router.get("/",response_model=list[ComplaintResponse])
def get_complaint(db:Session = Depends(get_db)):
    return db.query(Complaint).all()

# let also update this complaints

router.patch("/{complaint_id}",response_model=ComplaintResponse)
def update_complaint(complaint_id:int, update_date:ComplaintUpdate, db:Session = Depends(get_db)):
    
    complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()
    if not complaint:
        raise HTTPException(status_code=404,detail="Complaint not found")


    # Let update the fields
    complaint.status = update_date.status
    complaint.priority = update_date.priority 

    db.commit()
    db.refresh(complaint)
    return complaint   