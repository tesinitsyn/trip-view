from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "your_secret_key"
    ALGORITHM: str = "HS256"

settings = Settings()

