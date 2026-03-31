from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "EXPENSE-TRACKER"
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()