from pydantic import BaseModel

class PlaceSchema(BaseModel):
    id: int
    name: str
    description: str
    location: str
    image_url: str

    class Config:
        from_attributes = True  # Позволяет работать с SQLAlchemy
