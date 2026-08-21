# This is our user schemas which is differcent from the user model
from pydantic import BaseModel,EmailStr,ConfigDict

# Insert the schamas class of a users (What the frontend sends when signing up)
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password : str
    role : str ="student"

# Let do the user login 
class UserLogin(BaseModel):
    email: EmailStr
    password : str

# Let move to user response

class UserReponse(BaseModel):
    id:int
    full_name: str
    email : EmailStr
    role :str

    model_config = ConfigDict(from_attributes=True)