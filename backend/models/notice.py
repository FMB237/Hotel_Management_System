from sqlalchemy import Column,Integer,String,DateTime,Boolean,ForeignKey,func
from sqlalchemy.orm import relationship
from database import Base

class Notice(Base):
    __tablename__ = "notices"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    is_pinned = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now())

    author_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    author = relationship("User",backref="notices")