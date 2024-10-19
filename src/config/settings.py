from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str

    @property
    def db_url(self) -> str:
        return f'sqlite+aiosqlite:///db.sqlite'

    class Config:
        env_file = 'config/.env'


settings = Settings()
