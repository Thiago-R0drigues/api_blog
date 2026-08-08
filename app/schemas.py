from pydantic import BaseModel, EmailStr

class Base(BaseModel):
    pass

class Post(Base):
    post_title: str
    post_description: str

class User(Base):
    name: str
    email: EmailStr
    password: str