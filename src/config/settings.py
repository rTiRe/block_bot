from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str


    @property
    def db_url(self) -> str:
        protocol='postgresql+asyncpg'
        user_data = f'{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}'
        server_data = f'{self.POSTGRES_HOST}:{self.POSTGRES_PORT}'
        return f'{protocol}://{user_data}@{server_data}/{self.POSTGRES_DB}'

    class Config:
        env_file = 'src/config/.env'


settings = Settings()

CHANNEL_ID = -1002416384562
CHANNEL_URL = 'https://t.me/+TcvCQT1TPzdiMWFi'

START_DEMOLITION_BUTTON = 'Начать снос'
PROFILE_BUTTON = 'Профиль'
SUPPORT_BUTTON = 'Тех. Поддержка'
RULES_BUTTON = 'Правила'
