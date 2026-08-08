from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
import schemas
import models

def get_posts(db: Session):
    statement = select(models.Post)
    posts = db.execute(statement).scalars().all()
    return posts

def create_post(post: schemas.Post, db: Session):
        novo_post = models.Post(**post.model_dump())
        db.add(novo_post)
        db.commit()
        db.refresh(novo_post)
        return novo_post