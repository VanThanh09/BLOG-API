import cloudinary
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
import logging
import redis

# env
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    app_name: str = "BLOG-API"
    database_url: str
    secret_key: str
    mail_username: str
    mail_password: str
    mail_from: str
    mail_port: int
    mail_server: str
    cloud_name: str
    api_cloud_key: str
    api_cloud_secret: str
    redis_host: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",

        extra = 'ignore'
    )

settings = Settings()

#logger
logger = logging.getLogger(__name__)

#redis
redis_client = redis.Redis(
    host=settings.redis_host,
    port=6379,
    db=0,
    decode_responses=True
)

#cloudinary
cloudinary.config(
    cloud_name=settings.cloud_name,
    api_key=settings.api_cloud_key,
    api_secret=settings.api_cloud_secret
)