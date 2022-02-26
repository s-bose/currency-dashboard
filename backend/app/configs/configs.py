from typing import Optional, Dict, Any
from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = 'FutureMsg'
    API_STR: str = '/api'
    VERSION: str = '1.0.0'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7      # 7 days

    PY_DATETIME_FORMAT: str = '%d/%m/%Y %H:%M:%S'

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int

    DATABASE_URI: Optional[PostgresDsn] = None
    # if DATABASE_URI not available in env, build it below

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, str]) -> Any:

        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=f"{values.get('POSTGRES_PORT')}",
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    SECRET_KEY: str

    class Config:
        case_sensitive: bool = True
        env_file: str = '.env'
        env_file_encoding: str = 'utf-8'


settings = Settings()


