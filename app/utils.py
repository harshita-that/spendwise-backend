import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import User

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

security = HTTPBearer()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
    except:
        raise HTTPException(status_code=401, detail="invalid token")

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=401, detail="user not found")

    return user