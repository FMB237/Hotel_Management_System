# File for handling jwt tokens 

# 1. The imports 
from datetime import datetime,timedelta,timezone
from jose import jwt,JWTError
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


from database  import get_db
from models.user import User



# Let set up our variables 

SECRET_KEY= "SECRET_KEY"# I will change is in prodcution
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60*24 # Means token expire in 24 hours



# Let start the jwt token generation 

oauth2_scheme =  OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(data:dict,expires_delta: timedelta |None = None):
    """Create the jwt_token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def get_current_user(token:str = Depends(oauth2_scheme),db: Session = Depends(get_db)):
    """Dependency to extract and verify the user token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not valid credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        # Let Decode the token 
        payload= jwt.decode(token,SECRET_KEY,algorithms=["ALGORITHM"])
        email : str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception


    user = db.query(User).filter(User.email == email).first()
    if User is None:
        raise credentials_exception
    return user    