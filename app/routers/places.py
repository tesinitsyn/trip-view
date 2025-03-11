from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
from app.models.place import Place
from app.schemas.place import PlaceSchema  # Используем Pydantic-модель

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

@router.post("/", response_model=PlaceSchema)  # Используем Pydantic
def add_place(place_data: PlaceSchema, db: Session = Depends(get_db)):
    new_place = Place(**place_data.dict())  # Преобразуем в SQLAlchemy-модель
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