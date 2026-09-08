# notice for handling pydantics 
from pydantic import BaseModel,ConfigDict
from typing import Optional
from datetime import datetime

# let create Notices 

class NoticeCreate(BaseModel):
    title: str
    content : str
    is_pinned: bool = False

class NoticeUpdate(BaseModel):
    title: Optional[str] = None
    content : Optional[str] = None
    is_pinned : Optional[bool] = None
    is_active : Optional[bool] = None

class NoticeResponse(BaseModel):
    id:int
    title : str
    content : str
    is_pinned: bool
    is_active : bool
    created_at : datetime
    author_id : int 

    model_config = ConfigDict(from_attributes=True)