import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    REDIS_URL: str
    
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.getcwd(), ".env"),
        extra="ignore"
    )

    def get_bot_token(self):
        return self.BOT_TOKEN
    
    def get_redis_url(self):
        return self.REDIS_URL

settings = Settings()
