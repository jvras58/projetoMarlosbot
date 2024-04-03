from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Classe que representa as configurações setadas no .env da aplicação.
    """

    model_config = SettingsConfigDict(env_file='.env', env_file_encode='utf-8')

    # Configurações do bot
    DISCORD_TOKEN: str
    DB_URL: str
    AUTHORIZATION_IDS: str
    # TODO: add configurações para adicionar os membros do servidor no banco de dados
    YOUR_GUILD_ID: str

    # Configurações de imagem de alguns comandos
    AVATAR_SIZE: tuple = (250, 250)
    BACKGROUND_SIZE: tuple = (500, 280)
    BACKGROUND_COLOR: tuple = (56, 56, 56)
    RECTANGLE_COLOR: tuple = (207, 13, 48)
    RECTANGLE_RADIUS: int = 5
    FONT_SIZE: int = 20


@lru_cache
def get_settings() -> Settings:
    return Settings()
