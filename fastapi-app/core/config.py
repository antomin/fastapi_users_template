from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Run(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000
    workers: int = 1


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class Database(BaseModel):
    name: str
    user: str
    password: str
    host: str
    port: int

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False, env_nested_delimiter="__")

    debug: bool = False
    base_dir: Path = Path(__file__).parent.parent
    run: Run = Run()
    api: ApiPrefix = ApiPrefix()
    db: Database


