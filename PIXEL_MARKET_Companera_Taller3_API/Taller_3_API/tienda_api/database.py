# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.
"""Conexion SQLite mediante SQLModel. Compartida por los routers."""
from sqlmodel import SQLModel, Session, create_engine
from tienda_api.config import settings

connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine = create_engine(settings.database_url, connect_args=connect_args)

def create_db_and_tables():
    """Crear las tablas al iniciar el servidor."""
    from tienda_api import models  # noqa: F401
    SQLModel.metadata.create_all(engine)

def get_session():
    """Proporcionar una sesion y cerrarla al terminar la solicitud."""
    with Session(engine) as session:
        yield session
