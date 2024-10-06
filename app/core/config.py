from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Setting(BaseSettings):
    # database
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    # jwt
    secret_key: str
    refresh_secret_key : str
    algorithm: str
    timeout: int
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    REFRESH_TOKEN_EXPIRE_MINUTES : int

    # internal env
    adminapikey: str

    SERVER: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8",
    )

settings = Setting()
