# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.
"""Datos aislados: cada prueba crea una base SQLite en memoria."""
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool
from main import app
from tienda_api.database import get_session
from tienda_api import models  # noqa: F401

@pytest.fixture
def session():
    """Crear tablas y abrir sesion independiente por prueba."""
    engine = create_engine('sqlite://', connect_args={'check_same_thread': False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    engine.dispose()

@pytest.fixture
def client(session):
    """Reemplazar la dependencia de SQLite por la sesion de prueba."""
    def get_session_override():
        yield session
    app.dependency_overrides[get_session] = get_session_override
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()

@pytest.fixture
def usuario(client):
    """Crear usuario reutilizable a traves de la API publica."""
    return client.post('/api/usuarios', json={'nombre': 'Cliente Demo', 'correo': 'cliente@example.com'}).json()

@pytest.fixture
def juego(client):
    """Registrar juego ficticio para pruebas."""
    return client.post('/api/juegos', json={
        'titulo': 'Reinos de Neon', 'desarrollador': 'Estudio Demo', 'plataforma': 'PC',
        'genero': 'RPG', 'precio': 54900, 'anio_lanzamiento': 2024,
        'descripcion': 'Juego ficticio para pruebas', 'disponible': True,
    }).json()
