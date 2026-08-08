from sqlalchemy import select
from sqlalchemy.orm import Session

import app.schemas as schemas
import app.models as models

def get_posts(db: Session):
    statement = select(models.Post)
    posts = db.execute(statement).scalars().all()
    return posts

def create_post(post: schemas.Post, db: Session):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def update_post(post_id: int, post:schemas.Post, db: Session):
    #preciso ir na sessão, pegar o post e pegar as propriedades dele
    stmt = select(models.Post).where(models.Post.post_id == post_id)
    post_to_update = db.execute(stmt).scalar()

    if post_to_update:
        post_updated = post.model_dump(exclude_unset=True)

        for key, value in post_updated.items():
            setattr(post_to_update, key, value)

        db.commit()
        db.refresh(post_to_update)    
        
    return post_to_update

def delete_post(post_id: int, db: Session):
    stmt = select(models.Post).where(models.Post.post_id == post_id)
    post_to_delete = db.execute(stmt).scalar()

    if post_to_delete:
        db.delete(post_to_delete)
        db.commit()
    

    

      