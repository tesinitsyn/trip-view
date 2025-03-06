from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.favorite import favorites_db
from models.place import places_db, Place
from core.security import get_current_user
from models.user import User

router = APIRouter()

@router.post("/")
def add_favorite(place_id: int, user: User = Depends(get_current_user)):
    username = user.username
    if username not in favorites_db:
        favorites_db[username] = set()
    favorites_db[username].add(place_id)
    return {"message": "Place added to favorites"}

@router.get("/", response_model=List[Place])
def get_favorites(user: User = Depends(get_current_user)):
    username = user.username
    favorite_places = [
        place for place in places_db if place.id in favorites_db.get(username, set())
    ]
    return favorite_places

@router.delete("/{place_id}")
def remove_favorite(place_id: int, user: User = Depends(get_current_user)):
    username = user.username
    if username in favorites_db and place_id in favorites_db[username]:
        favorites_db[username].remove(place_id)
        return {"message": "Place removed from favorites"}
    raise HTTPException(status_code=404, detail="Place not found in favorites")
