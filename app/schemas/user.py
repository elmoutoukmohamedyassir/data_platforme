from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: Optional[datetime] = None
    is_active: Optional[bool] = None

    class Config:
        from_attributes = True  # needed for SQLAlchemy → Pydantic mapping

class UserLogin(BaseModel):
    email: str
    password: str