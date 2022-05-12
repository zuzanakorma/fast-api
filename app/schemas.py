from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime

from app.models import User


# create model for received data in Post, automatically perform validation!!! for schema
class PostBase(BaseModel):
    title: str
    content:str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    # to convert it ro dictionary, use Config
    class Config:
        orm_mode = True


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    
    class Config:
        orm_mode = True

# does not work (same issue as join operation )
class PostOut(BaseModel):
    Post: PostResponse
    votes: int
   
    class Config:
        orm_mode = True

        
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    