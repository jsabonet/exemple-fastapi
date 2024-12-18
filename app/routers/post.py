
from .. import models, schemas, oauth2
from fastapi import HTTPException, Response, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)



@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit:int =10, skip:int =0, search:Optional[str] =""):

    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()



    return posts


@router.post("/", status_code =status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post= models.Post(title=post.title, content=post.content, published=post.published, owner_id=current_user.id)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post


@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db),  current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} was not found",
        )

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform action")

    return  post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} does not exist",
        )

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform action")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # Consulta o banco para encontrar o post com o ID especificado
    post_query = db.query(models.Post).filter(models.Post.id == id)
    existing_post = post_query.first()

    # Verifica se o post existe
    if not existing_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} does not exist",
        )
    
    if existing_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail="Not authorized to perform action")

    # Cria um dicionário com os dados a serem atualizados
    update_data = post.dict(exclude_unset=True)

    if update_data:
        post_query.update(update_data, synchronize_session=False)
        db.commit()

    # Retorna o post atualizado
    updated_post = post_query.first()
    return updated_post
