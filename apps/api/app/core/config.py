from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ForgeAI API"
    environment: str = "dev"
    database_url: str = "postgresql+psycopg://forgeai:forgeai@localhost:5432/forgeai"
    jwt_secret: str = "change-me"
    jwt_refresh_secret: str = "change-me-refresh"
    access_token_minutes: int = 30
    refresh_token_days: int = 7
    cors_origins: str = "http://localhost:3000"
    ai_provider: str = "mock"
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
