from app.schemas.user import UserCreate, UserResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.user import User
from app.core.security import hash_password

router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user(new_user: UserCreate, db: Session = Depends(get_db)):

    # 1. hash the plain password
    hashed_pw = hash_password(new_user.password)

    # 2. create DB user object
    user = User(
        name=new_user.name,
        email=new_user.email,
        hashed_password=hashed_pw
    )

    # 3. save to DB
    db.add(user)
    db.commit()
    db.refresh(user)

    return user