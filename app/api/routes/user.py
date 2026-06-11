from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.core.security import hash_password, verify_password, create_access_token

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
def login(user_login: UserLogin, db: Session = Depends(get_db)):

    # 1. find user in DB
    user = db.query(User).filter(User.email == user_login.email).first()

    # 2. check if user exists
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    # 3. verify password
    if not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    # 4. create token
    token = create_access_token(
        data={"sub": str(user.id)}  # user id inside token
    )

    # 5. return token
    return {
        "access_token": token,
        "token_type": "bearer"
    }

