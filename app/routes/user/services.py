from sqlalchemy.orm import Session
import schemas
from app import models
from app.core.security import get_password_hash

def create_user(db: Session, user: schemas.SUser):
    paswword_hasshed = get_password_hash(user.password)
    user.password = paswword_hasshed
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_nro_document(db: Session, nro_document: str):
    return db.query(models.User).filter(models.User.nro_document == nro_document).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# get users by pagination
def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
