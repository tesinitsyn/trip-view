from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    location = Column(String)
    image_url = Column(String)
