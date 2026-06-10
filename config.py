from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # App
    APP_NAME: str = "NexusIQ AI Service"
    APP_ENV: str = "development"
    DEBUG: bool = True
    PORT: int = 8000
    HOST: str = "0.0.0.0"

    # PostgreSQL
    PG_DSN: str = "postgresql+asyncpg://postgres:password@localhost:5432/nexusiq"

    # MongoDB
    MONGO_URI: str = "mongodb://localhost:27017/nexusiq"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # AWS
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_REGION: str = "us-east-1"
    AWS_S3_BUCKET: str = "nexusiq-documents"

    # OpenAI
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4-turbo-preview"
    EMBEDDING_MODEL: str = "text-embedding-ada-002"

    # ChromaDB
    CHROMA_HOST: str = "localhost"
    CHROMA_PORT: int = 8001
    CHROMA_COLLECTION: str = "nexusiq_docs"

    # ML
    DEFAULT_FORECAST_MODEL: str = "auto"
    MAX_FORECAST_HORIZON: int = 365
    CHURN_THRESHOLD: float = 0.5
    RISK_SENSITIVITY: str = "medium"

    # Security
    SECRET_KEY: str = "dev_secret_key"
    BACKEND_SERVICE_KEY: str = "nexusiq_internal_key"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
