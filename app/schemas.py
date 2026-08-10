from pydantic import BaseModel, EmailStr

class Base(BaseModel):
    pass

class Post(Base):
    post_title: str
    post_description: str

class User(Base):
    user_name: str
    user_email: EmailStr
    user_password: str