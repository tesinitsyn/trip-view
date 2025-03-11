from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
from app.models.favorite import Favorite
from app.models.user import User
from app.models.place import Place
from app.schemas.place import PlaceSchema  # Используем Pydantic-модель
from app.core.security import get_current_user

router = APIRouter()

# Функция для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[PlaceSchema])  # Используем Pydantic-модель
def get_favorites(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    favorites = db.query(Favorite).filter(Favorite.user_id == user.id).all()
    place_ids = [fav.place_id for fav in favorites]
    places = db.query(Place).filter(Place.id.in_(place_ids)).all()
    return places  # Теперь FastAPI корректно сериализует объекты

@router.post("/")
def add_favorite(place_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_place = db.query(Place).filter(Place.id == place_id).first()
    if not db_place:
        raise HTTPException(status_code=404, detail="Place not found")

    favorite = Favorite(user_id=user.id, place_id=place_id)
    db.add(favorite)
    db.commit()
    return {"message": "Place added to favorites"}

@router.delete("/{place_id}")
def remove_favorite(place_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    favorite = db.query(Favorite).filter(Favorite.user_id == user.id, Favorite.place_id == place_id).first()
    if not favorite:
        raise HTTPException(status_code=404, detail="Place not found in favorites")

    db.delete(favorite)
    db.commit()
    return {"message": "Place removed from favorites"}
