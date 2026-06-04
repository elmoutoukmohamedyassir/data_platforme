from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP
from app.database.db import Base


class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True,nullable=False)
    hashed_password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP)
    is_active = Column(Boolean)
    




