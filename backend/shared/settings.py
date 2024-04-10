import multiprocessing as mp

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    pg_database: str = "db_main"
    pg_host: str = "localhost"
    pg_port: int = 5432
    pg_username: str = "db_main"
    pg_password: str = "db_main"

    redis_host: str = "localhost"
    redis_port: int = 6379

    uvicorn_host: str = "localhost"
    uvicorn_port: int = 8000
    uvicorn_workers: int = mp.cpu_count()
    uvicorn_log_level: str = "WARNING"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="_")


app_settings = AppSettings()
