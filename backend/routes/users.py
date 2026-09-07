# For handling user profiles 
from fastapi import FastAPI,APIRouter,HTTPException,File,UploadFile,Depends
from sqlalchemy.orm import Session
from models.user import User
from database import get_db
from schemas.user import UserResponse
from utils.jwt import get_current_user
from utils.file_handler import save_upload_file


router = APIRouter(prefix="/users",tags=["User Profile"])

# Let now get our current user 
@router.get('/profile',response_model=UserResponse)
def get_profile(current_user : User = Depends(get_current_user)):
    return current_user

# Let also upload profile-pictures 

@router.post("/profile-pictueres")
def upload_profile_picture(file : UploadFile = File(...),db: Session= Depends(get_db),current_user:User = Depends(get_current_user)):
    file_path = save_upload_file(file,folder="profiles")

    current_user.profile_picture= file_path
    db.commit()
    db.refresh(current_user)

    return {"message":"Profile picture updated successfully","image_path":file_path}
