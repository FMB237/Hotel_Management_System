# Let do the notice routes 
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models.notice import Notice
from schemas.notice import NoticeCreate, NoticeResponse, NoticeUpdate
from database import get_db
from models.user import User
from utils.jwt import get_current_user

router = APIRouter(prefix="/notices", tags=['Notices & Announcements'])

# Let create the notice only for the admin 
@router.post('/', response_model=NoticeResponse, status_code=201)
def create_notice(notice: NoticeCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Now let check for the RBAC """ 
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not Authorized admin only")
    
    # FIXED: changed user.id to current_user.id
    new_notice = Notice(**notice.model_dump(), author_id=current_user.id)
    db.add(new_notice)
    db.commit()
    db.refresh(new_notice)
    return new_notice

# Let get active notices for each student 
# FIXED: Changed path from "/{notice_id}" to "/" because we are fetching ALL active notices for the board
@router.get("/", response_model=list[NoticeResponse])
def get_notices(db: Session = Depends(get_db)):
     return db.query(Notice).filter(Notice.is_active == True).order_by(Notice.is_pinned.desc(), Notice.created_at.desc()).all()

# Update the notice only for admin 
# FIXED: Typo in function name (upate -> update)
@router.put("/{notice_id}", response_model=NoticeResponse)
def update_notice(notice_id: int, notice_update: NoticeUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not Authorized admin only")
        
    notice = db.query(Notice).filter(Notice.id == notice_id).first()
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")

    # Only update the fields that were actually sent
    update_data = notice_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(notice, key, value)    

    db.commit()
    db.refresh(notice)
    return notice   

# Delete Notice (Admin Only)
@router.delete("/{notice_id}")
def delete_notice(
    notice_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized. Admins only.")

    notice = db.query(Notice).filter(Notice.id == notice_id).first()
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")

    db.delete(notice)
    db.commit()
    return {"message": "Notice deleted successfully"}