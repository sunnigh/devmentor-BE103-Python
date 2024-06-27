from sqlalchemy.orm import Session
from fastapi import HTTPException

from database.post import Post
from schema.database.post import PostCreate,PostUpdate


def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()


def create(db: Session, post: PostCreate):
    db_user = Post(title=post.title, content=post.content)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get(db: Session, id: int):
    return db.query(Post).filter(Post.id == id).first()

def update(db: Session, id: int,post_update: PostUpdate):
    db_post = get(db, id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db_post.title = post_update.title
    db_post.content = post_update.content
    db.commit()
    return db_post

def delete(db: Session, id: int):
    db_post = get(db, id)
    if db_post:
        db.delete(db_post)
        db.commit()
        return {"message": "post deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")