# config.py
'''Config Loader for LogiNet'''

from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    '''Loginet Config'''
    
    # DB Settings
    db_driver_name: str | None = None
    db_username: str | None = None
    db_password: str | None = None
    db_host: str | None = None
    db: str | None = None

    # Redis
    redis_url: str | None = "redis://localhost:6379"

    # Discord OAuth
    discord_client_id: str | None = None
    discord_client_secret: str | None = None
    discord_redirect_uri: str | None  = None

    env: str | None = None
    debug: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = False
        extra    = "ignore"
    
    @property
    def db_url(self) -> str:
        return f"{self.db_driver_name}://{self.db_username}:{self.db_password}@{self.db_host}/{self.db}"


@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
