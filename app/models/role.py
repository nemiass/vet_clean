from sqlalchemy import Column, Integer, String, DateTime, Boolean

from ..core.database import Base

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))

    def __repr__(self):
        return f"Role(name={self.name}, description={self.description})"
