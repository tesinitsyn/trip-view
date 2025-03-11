from fastapi import FastAPI
from app.routers import users, places, favorites
from app.core.database import engine
from app.models import Base  # Импортируем все модели через __init__.py
from app.core.database import engine, Base


app = FastAPI()

# Создаём таблицы, если их нет
Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(places.router, prefix="/places", tags=["Places"])
app.include_router(favorites.router, prefix="/favorites", tags=["Favorites"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    Base.metadata.create_all(bind=engine)