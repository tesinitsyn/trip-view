from pydantic import BaseModel
from typing import List

# In-memory база мест
places_db: List["Place"] = []

class Place(BaseModel):
    id: int
    name: str
    description: str
    location: str
    image_url: str
