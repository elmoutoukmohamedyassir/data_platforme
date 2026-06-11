from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.core.security import hash_password, verify_password

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(new_user: UserCreate, db: Session = Depends(get_db)):

    # 1. hash password
    hashed_pw = hash_password(new_user.password)

    # 2. create DB user
    user = User(
        name=new_user.name,
        email=new_user.email,
        hashed_password=hashed_pw
    )

    # 3. save
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

@router.post("/login")
def login(user_login:UserLogin,db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user_login.email).first()
    if not db_user : 
        raise HTTPException(statue_code = 404, detail ="User not found")
    if not verify_password(user_login.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {"message": "Login successful"}

