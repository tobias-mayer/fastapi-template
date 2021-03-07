from pydantic import BaseSettings, PostgresDsn, validator
from typing import Optional, Dict, Any
import secrets


class AppSettings(BaseSettings):
    PROJECT_NAME: str

    SECRET_KEY = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 20

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    SQLALCHEMY_DB_URI: Optional[PostgresDsn] = None

    @validator('SQLALCHEMY_DB_URI', pre=True)
    def build_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme='postgresql',
            user=values.get('POSTGRES_USER'),
            password=values.get('POSTGRES_PASSWORD'),
            host=values.get('POSTGRES_SERVER'),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )


app_settings = AppSettings()
