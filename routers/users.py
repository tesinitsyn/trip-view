from fastapi import APIRouter, HTTPException
from models.user import users_db, User, UserInDB
from core.security import get_password_hash, create_access_token, verify_password

router = APIRouter()

@router.post("/register")
def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    users_db[user.username] = UserInDB(username=user.username, hashed_password=hashed_password)
    token = create_access_token(user.username)
    return {"access_token": token, "token_type": "bearer"}

@router.post("/token")
def login(user: User):
    user_in_db = users_db.get(user.username)
    if not user_in_db or not verify_password(user.password, user_in_db.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token(user.username)
    return {"access_token": token, "token_type": "bearer"}
