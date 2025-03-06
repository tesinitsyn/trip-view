from fastapi import FastAPI
from routers import users, places, favorites

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(places.router, prefix="/places", tags=["Places"])
app.include_router(favorites.router, prefix="/favorites", tags=["Favorites"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
