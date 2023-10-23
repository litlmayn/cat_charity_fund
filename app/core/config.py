from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'sochetaniesimvolov'

    class Config:
        env_file = '.env'


settings = Settings()
