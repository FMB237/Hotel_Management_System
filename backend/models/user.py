# Ler define our user model 
from sqlalchemy import Column,Integer,String,Boolean,DateTime,func
from database import Base


# Let defined the  user class that is mainly it tables

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,unique=True,index=True,primary_key=True)
    full_name = Column(String,nullable=False)
    email = Column(String,unique=True,nullable=False)
    password_hash = Column(String,nullable=False)
    role = Column(String,default="student")
    profile_picture = Column(String,nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now())