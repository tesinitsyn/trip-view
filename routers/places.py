from fastapi import APIRouter, HTTPException
from typing import List
from models.place import places_db, Place

router = APIRouter()

@router.get("/", response_model=List[Place])
def get_places():
    return places_db

@router.post("/", response_model=Place)
def add_place(place: Place):
    places_db.append(place)
    return place

@router.get("/{place_id}", response_model=Place)
def get_place(place_id: int):
    for place in places_db:
        if place.id == place_id:
            return place
    raise HTTPException(status_code=404, detail="Place not found")

@router.delete("/{place_id}")
def delete_place(place_id: int):
    global places_db
    places_db = [place for place in places_db if place.id != place_id]
    return {"message": "Place deleted"}
