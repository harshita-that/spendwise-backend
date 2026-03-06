from jose import jwt
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from .database import get_db
from . import models

SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

security = HTTPBearer()


def create_access_token(data: dict):
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


def get_current_user(token=Depends(security), db: Session = Depends(get_db)):

    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        user = db.query(models.User).filter(models.User.id == user_id).first()

        if user is None:
            raise HTTPException(status_code=401, detail="user not found")

        return user

    except:
        raise HTTPException(status_code=401, detail="invalid token")