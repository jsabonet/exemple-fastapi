from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

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

# class PostOut(BaseModel):
#     Post: Post
#     votes: int


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    owner_id: int
    owner: UserOut
    votes: int = 0

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int

class Vote(BaseModel):
    post_id: int
    dir: int

    @validator('dir')
    def check_dir(cls, v):
        if not (0 <= v <= 1):
            raise ValueError('dir must be 0 or 1')
        return v
