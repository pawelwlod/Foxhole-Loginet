# config.py
'''Config Loader for LogiNet'''

from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    '''Loginet Config'''
    
    # DB Settings
    DB_DRIVER_NAME: str | None = "postgresql+asyncpg"
    DB_USERNAME: str | None = "loginet"
    DB_PASSWORD: str | None = "loginet"
    DB_HOST: str | None = "localhost"
    DB: str | None = "loginet"

    # Redis
    REDIS_HOST: str | None = "localhost"
    REDIS_PORT: str | None = "6379"

    # Discord OAuth
    DISCORD_CLIENT_ID: str | None = None
    DISCORD_CLIENT_SECRET: str | None = None
    DISCORD_REDIRECT_URI: str | None  = None

    FASTAPI_ENV: str | None = "prod"
    DEBUG: bool | None = False

    class Config:
        env_file = ".env"
        case_sensitive = False
        extra    = "ignore"
    
    @property
    def db_url(self) -> str:
        return f"{self.DB_DRIVER_NAME}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB}"

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
