from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_KEY')

if not DATABASE_URL:
    DATABASE_URL = 'sqlite:///database.db'

connect_args = {'check_same_thread': False}
engine = create_engine(DATABASE_URL, connect_args=connect_args, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine) 


    