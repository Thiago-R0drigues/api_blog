from fastapi import FastAPI, APIRouter, status, Depends
from schemas import Post
import models
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select

VERSION = 'ALPHA'

app = FastAPI(version=VERSION)

router = APIRouter()

app.include_router(router)

@router.get('/posts/', tags=['POSTS'], response_model=list[Post])
def route_get_posts(db: Session = Depends(get_db)):
    """É A MESMA COISA QUE O DESCRIPTION"""
    statement = select(models.Post)
    posts = db.execute(statement).scalars().all()
    return posts
    

@router.post('/posts/', tags=['POSTS'], status_code=status.HTTP_201_CREATED, response_model=Post)
def route_create_post(post: Post, db: Session = Depends(get_db)):
    """AQUI POSSO COLOCAR A DESCRICAO PARA MELHORAR A DOCUMENTACAO"""
    novo_post = models.Post(**post.model_dump())
    db.add(novo_post)
    db.commit()
    db.refresh(novo_post)
    return novo_post

@router.put('/posts/{user_id}', tags=['POSTS'], status_code=status.HTTP_200_OK)
def route_update_post(post: Post):
    pass

@router.delete('/posts/{user_id}', tags=['POSTS'], status_code=status.HTTP_204_NO_CONTENT)
def route_delete_post(post: Post):
    pass