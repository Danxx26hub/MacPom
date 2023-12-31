from pydantic_settings import BaseSettings
from functools import lru_cache


class prodSettings(BaseSettings):
    message: str = "Time's up!"
    title: str = "Pomodoro Timer"
    run_time: int = 1
    log_level: str = "INFO"
    sound: str = "Glass"

    class Config:
        """config class for local secrets"""

        env_file: str = ".prodenv"


class devSettings(BaseSettings):
    message: str = "Time's up!"
    title: str = "Pomodoro Timer"
    run_time: int = 1
    log_level: str = "DEBUG"
    sound: str = "Glass"

    class Config:
        """config class for local secrets"""

        env_file: str = ".devenv"


@lru_cache
def get_settings(env):
    if env == "dev":
        settings = devSettings()

    else:
        settings = prodSettings()
    return settings
