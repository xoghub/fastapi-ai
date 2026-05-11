from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Set

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    PROJECT_NAME: str = "FAST-AI ABSA"
    API_STR: str = "/api"
    ENVIRONMENT: str = "local"
    
    # Auth
    JWT_SECRET: str = "supersecretkey" # In prod, change this!
    JWT_ALG: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db" # Default for local dev
    
    SHOW_DOCS_IN: Set[str] = {"local", "staging"}

settings = Settings()
