from models.user import users_db
from models.place import places_db
from models.favorite import favorites_db

# Инициализация In-Memory базы (можно сделать предзаполненные данные)
def init_db():
    users_db.clear()
    places_db.clear()
    favorites_db.clear()

    # Пример данных
    places_db.extend([
        {"id": 1, "name": "Eiffel Tower", "description": "Iconic tower in Paris", "location": "Paris, France", "image_url": "https://example.com/eiffel.jpg"},
        {"id": 2, "name": "Colosseum", "description": "Ancient Roman amphitheater", "location": "Rome, Italy", "image_url": "https://example.com/colosseum.jpg"}
    ])

init_db()
