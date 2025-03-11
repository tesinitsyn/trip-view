from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
from app.models.user import User
from app.core.security import get_password_hash, create_access_token, verify_password
from pydantic import BaseModel

router = APIRouter()

# Создаём таблицы
User.__table__.create(bind=engine, checkfirst=True)


# Получаем сессию базы
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic модель для запроса
class UserCreate(BaseModel):
    username: str
    password: str


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token(new_user.username)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/token")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token(db_user.username)
    return {"access_token": token, "token_type": "bearer"}
