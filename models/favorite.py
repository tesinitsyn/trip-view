from pydantic import BaseModel
from typing import Dict, Set

# In-memory база избранного
favorites_db: Dict[str, Set[int]] = {}

class Favorite(BaseModel):
    place_id: int
    username: str
