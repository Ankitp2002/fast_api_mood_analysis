from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    DB_DRIVER: str = "mysql"
    DB_HOST: str = "localhost"
    DB_PORT: str = "3306"
    DB_NAME: str = "test"
    DB_USER: str = "root"
    DB_PASW: str = "root"

    @property
    def DB_URL(self) -> str:
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASW}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"


def get_settings() -> Setting:
    return Setting()
