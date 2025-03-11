from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
import datetime
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from passlib.context import CryptContext
from app.core.config import settings

# Настройка безопасности
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Функция для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Хеширование пароля
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# Проверка пароля
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Создание JWT-токена
def create_access_token(username: str) -> str:
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode(
        {"sub": username, "exp": expiration},
        settings.SECRET_KEY,  # Используем ключ из конфигурации
        algorithm=settings.ALGORITHM  # Используем алгоритм из конфигурации
    )
    return token


# Проверка токена и получение пользователя из базы
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")

        return user
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
