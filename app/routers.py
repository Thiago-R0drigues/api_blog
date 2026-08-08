from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter()

@router.get('/posts/', tags=['POSTS'], response_model=list[schemas.Post])
def route_get_posts(db: Session = Depends(get_db)):
    """É A MESMA COISA QUE O DESCRIPTION"""
    return crud.get_posts(db=db)
    
@router.post('/posts/', tags=['POSTS'], status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def route_create_post(post: schemas.Post, db: Session = Depends(get_db)):
    """AQUI POSSO COLOCAR A DESCRICAO PARA MELHORAR A DOCUMENTACAO"""
    return crud.create_post(post=post, db=db)
    

@router.put('/posts/{user_id}', tags=['POSTS'], status_code=status.HTTP_200_OK, response_model=schemas.Post)
def route_update_post():
    pass

@router.delete('/posts/{user_id}', tags=['POSTS'], status_code=status.HTTP_204_NO_CONTENT)
def route_delete_post():
    pass