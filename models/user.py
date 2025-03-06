from pydantic import BaseModel
from passlib.context import CryptContext
from typing import Dict

# In-memory база пользователей
users_db: Dict[str, "UserInDB"] = {}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    username: str
    password: str

class UserInDB(User):
    hashed_password: str
