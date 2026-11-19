# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.
"""Configuracion obtenida de variables de entorno."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Parametros de la aplicacion."""
    app_name: str = "PIXEL MARKET | API de videojuegos"
    app_version: str = "1.0.0"
    database_url: str = "sqlite:///./videojuegos.db"
    cors_origins: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:8000", "http://127.0.0.1:8000"]
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
