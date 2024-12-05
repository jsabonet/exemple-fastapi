from pydantic import BaseModel, EmailStr
from datetime import datetime
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

from pydantic.types import  conint

Base = declarative_base()

class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True



class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    owner_id: int
    created_at: datetime
    owner: UserOut

    class Config:
        from_attributes = True


class PostOut(BaseModel):
    Post: Post
    votes:int

class UserCreate(BaseModel):
    email:EmailStr
    password:str

    class Config:
        from_attributes = True

class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True 


class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token: str
    token_type:str


class TokenData(BaseModel):
    id: int



class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)