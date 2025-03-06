from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
import datetime
from models.user import users_db, pwd_context, UserInDB
from core.config import settings  # Импортируем конфиг

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

# Проверка токена
def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None or username not in users_db:
            raise HTTPException(status_code=401, detail="Invalid token")
        return users_db[username]
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
