from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from sqlalchemy.orm import Session

import app.crud as crud
import app.schemas as schemas
from app.database import get_db

router = APIRouter()

#ROOT
@router.get('/', tags=['ROOT'], status_code=status.HTTP_200_OK)
def route_get_root():
    return {'message': 'Welcome to Blog API'}


#USERS
@router.get('/users/', tags=['USERS'], status_code=status.HTTP_200_OK, response_model=list[schemas.UserOut])
def route_get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)

@router.post('/users/', tags=['USERS'], status_code=status.HTTP_201_CREATED)
def route_create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(user=user, db=db)

@router.put('/users/{user_id}', tags=['USERS'], status_code=status.HTTP_202_ACCEPTED)
def route_update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(user_id=user_id, user=user, db=db)

@router.delete('/users/{user_id}', tags=['USERS'], status_code=status.HTTP_204_NO_CONTENT)
def route_delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(user_id=user_id, db=db)



#POSTS
@router.get('/posts/', tags=['POSTS'], status_code=status.HTTP_200_OK, response_model=list[schemas.PostOut])
def route_get_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db=db)
    
@router.post('/posts/', tags=['POSTS'], status_code=status.HTTP_201_CREATED, response_model=schemas.PostOut)
def route_create_post(post: schemas.PostOut, db: Session = Depends(get_db)):
    return crud.create_post(post=post, db=db)
    

@router.put('/posts/{user_id}', tags=['POSTS'], status_code=status.HTTP_200_OK, response_model=schemas.Post)
def route_update_post(post_id: int, post: schemas.Post, db: Session = Depends(get_db)):
    return crud.update_post(post_id=post_id, post=post, db=db)

@router.delete('/posts/{post_id}', tags=['POSTS'], status_code=status.HTTP_204_NO_CONTENT)
def route_delete_post(post_id: int, db: Session = Depends(get_db)):
    return crud.delete_post(post_id=post_id, db=db)