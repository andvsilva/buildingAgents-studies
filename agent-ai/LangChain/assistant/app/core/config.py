from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    # App
    APP_NAME: str = "AI Business Intelligence Assistant"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    # OpenAI
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    OPENAI_MODEL: str = "gpt-4o-mini"

    # Database
    DATABASE_URL: str = Field(
        default="postgresql://admin:password@localhost:5432/company"
    )

    # Vector DB
    VECTOR_PATH: str = "data/vectorstore"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()