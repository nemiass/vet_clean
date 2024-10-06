from sqlalchemy.orm import Session
from app.models import User


def get_user_by_id(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
