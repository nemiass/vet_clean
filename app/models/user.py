from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from ..core.database import Base
from app.models import Role


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    type_document = Column(String(255), nullable=True)
    nro_document = Column(String(255), unique=True, nullable=True)
    email = Column(String(255), nullable=True)
    age = Column(Integer, nullable=True)
    phone_number = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)
    gender = Column(String(255), nullable=True)
    url_photo = Column(String(255), nullable=True)
    date_of_account_deleted = Column(DateTime, nullable=True)
    is_root = Column(Boolean, default=False)
    # relationships
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=True)
    role = relationship(Role)

    def __repr__(self):
        return f"<User {self.username}>"
