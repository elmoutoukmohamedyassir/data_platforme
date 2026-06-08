from pydantic import BaseModel
from datetime import datetime
class UserCreate(BaseModel):
    name: str
    email: str
    password: str   # <-- plain password from user

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    is_active: bool

class UserLogin(BaseModel):
    email:str
    password:str



    
    
