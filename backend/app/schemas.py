from pydantic import BaseModel, EmailStr
from datetime import datetime

class Base(BaseModel):
    pass

#POSTS SCHEMAS

class Post(Base):
    post_title: str
    post_description: str

class PostOut(Post):
    post_id: int | None = None


#USERS SCHEMAS

class UserBase(Base):
    user_name: str
    user_email: EmailStr

class UserCreate(UserBase):
    user_password: str

class UserOut(UserBase):
    user_id: int

class UserUpdate(Base):
    user_name: str | None = None
    user_email: EmailStr | None = None
    user_password: str | None = None
