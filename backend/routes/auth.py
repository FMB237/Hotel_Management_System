# Let used this to handle authentification 
# 1. let start with all the imports 
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserCreate,UserLogin,UserReponse
from utils.security import hash_password,verify_password

# 2. Let define the API router 

router = APIRouter(prefix="/auth",tags=["Authentification"])


@router.post("/register",response_model=UserReponse)
def register(user_data:UserCreate,db: Session = Depends(get_db)):
    # Let check if user already exist 
    existing_user= db.query(User).filter(User.email==user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Email already register")

    # Hash password before saving it 
    hash_pw = hash_password(user_data.password)

    # Create the user object 
    new_user=User(
        full_name= user_data.full_name,
        email= user_data.email,
        password_hash= hash_pw,
        role = user_data.role
    )
    # Save user to db 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)    

    return new_user


# Now let handle the login path 

@router.post("/login")
def login(user_data:UserLogin,response_model=UserLogin, db: Session= Depends(get_db)):
    user = db.query(User).filter(User.email == user_data.email).first()
    if not user:
        raise HTTPException(status_code=401,detail="Invalid email and password")

    # 2. Verify password 
    if not verify_password(user_data.password,user.password_hash):
        raise HTTPException(status_code=401,detail="Invlaid email and password")

    return{
        "message":"Login Successful",
        "user_id":user.id,
        "role":user.role
    }    
    
