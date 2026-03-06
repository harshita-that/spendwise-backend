from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import jwt

from ..database import SessionLocal
from ..models import User
from ..schemas import UserCreate, UserLogin

router = APIRouter()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="email already exists")

    new_user = User(
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "user created",
        "user_id": new_user.id
    }


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="invalid email")

    if db_user.password != user.password:
        raise HTTPException(status_code=400, detail="invalid password")

    token = jwt.encode(
        {"user_id": db_user.id},
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }