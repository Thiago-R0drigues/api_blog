from sqlalchemy import select
from sqlalchemy.orm import Session

import app.schemas as schemas
import app.models as models


#CRUD USER
def get_users(db:Session):
    stmt = select(models.User)
    users = db.execute(stmt).scalars().all()
    return users


def create_user(user: schemas.UserCreate, db:Session):
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return f'User {user.user_name} has been created successfully'

def update_user(user_id: int, user: schemas.UserUpdate, db: Session):
    stmt = select(models.User).where(models.User.user_id == user_id)
    user_to_update = db.execute(stmt).scalar()

    if user_to_update:
        user_updated = user.model_dump(exclude_unset=True)

        for key, value in user_updated.items():
            setattr(user_to_update, key, value)

        db.commit()
        db.refresh(user_to_update)

def delete_user(user_id: int, db: Session):
    stmt = select(models.User).where(models.User.user_id == user_id)
    post_to_delete = db.execute(stmt).scalar()
    db.delete(post_to_delete)
    db.commit()

#CRUD POSTS

def get_posts(db: Session):
    stmt = select(models.Post)
    posts = db.execute(stmt).scalars().all()
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
    

    

      