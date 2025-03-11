from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
from app.models import User
from app.models.place import Place
from app.schemas.place import PlaceSchema  # Используем Pydantic-модель
from typing import List, Optional  # <-- Добавляем Optional
from app.core.security import get_current_user  # <-- Добавляем импорт
from app.schemas.place import PlaceCreate, PlaceResponse  # <-- Добавь этот импорт


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[PlaceSchema])  # Используем Pydantic
def get_places(db: Session = Depends(get_db)):
    return db.query(Place).all()

@router.post("/", response_model=PlaceResponse)
def add_place(
    place_data: PlaceCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)  # Получаем текущего пользователя
):
    new_place = Place(
        name=place_data.name,
        description=place_data.description,
        location=place_data.location,
        image_url=place_data.image_url,
        owner_id=user.id  # Указываем владельца
    )
    db.add(new_place)
    db.commit()
    db.refresh(new_place)
    return new_place

@router.get("/{place_id}", response_model=PlaceSchema)  # Новый эндпоинт
def get_place(place_id: int, db: Session = Depends(get_db)):
    place = db.query(Place).filter(Place.id == place_id).first()
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    return place  # FastAPI автоматически сериализует SQLAlchemy-модель в JSON


@router.get("/search/", response_model=List[PlaceSchema])  # <-- Добавляем `/` в конце
def search_places(query: Optional[str] = None, db: Session = Depends(get_db)):
    if not query:  # Если запрос пустой, возвращаем все места
        return db.query(Place).all()

    return db.query(Place).filter(
        Place.name.contains(query) | Place.location.contains(query)
    ).all()

