from pydantic import BaseModel


class PlaceSchema(BaseModel):
    id: int
    name: str
    description: str
    location: str
    image_url: str

    class Config:
        from_attributes = True  # Позволяет работать с SQLAlchemy

class PlaceCreate(BaseModel):
    name: str
    description: str
    location: str
    image_url: str

class PlaceResponse(BaseModel):
    id: int
    name: str
    description: str
    location: str
    image_url: str
    owner_id: int  # Теперь возвращаем владельца

    class Config:
        from_attributes = True

