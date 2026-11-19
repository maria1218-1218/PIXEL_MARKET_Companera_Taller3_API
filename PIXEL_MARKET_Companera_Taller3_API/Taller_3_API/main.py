# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.
"""Punto de entrada de PIXEL MARKET: REST API y portada de presentacion."""
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from sqlmodel import Session
from tienda_api.config import settings
from tienda_api.database import create_db_and_tables, engine
from tienda_api.routers import usuarios, juegos, favoritos

# El contexto lifespan crea las tablas antes de aceptar consultas.
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Crear esquema SQLite al iniciar la API."""
    create_db_and_tables()
    yield

# Se configura la documentacion OpenAPI de la API.
app = FastAPI(
    title=settings.app_name,
    description='API RESTful para usuarios, videojuegos y listas de favoritos. Proyecto academico LPA2.',
    version=settings.app_version,
    contact={'name': 'Proyecto academico LPA2'},
    license_info={'name': 'Uso educativo'},
    lifespan=lifespan,
)

# Permitir el consumo del frontend local del Taller 4.
app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.include_router(usuarios.router)
app.include_router(juegos.router)
app.include_router(favoritos.router)

# Servir estilos locales de la pagina de introduccion.
app.mount('/static', StaticFiles(directory=Path(__file__).parent / 'static'), name='static')

@app.get('/', include_in_schema=False)
def portada():
    """Mostrar una portada visual; el REST API permanece bajo /api."""
    return FileResponse(Path(__file__).parent / 'static' / 'index.html')

@app.get('/api', tags=['Estado'])
def informacion():
    """Resumen JSON de recursos disponibles para integraciones externas."""
    return {'nombre': settings.app_name, 'version': settings.app_version, 'recursos': ['/api/usuarios', '/api/juegos', '/api/favoritos'], 'docs': '/docs'}

# El endpoint de salud permite confirmar que SQLite responde.
@app.get('/health', tags=['Estado'])
def salud():
    """Verificar conexion activa con la base de datos."""
    try:
        with Session(engine) as session:
            session.execute(text('SELECT 1')).first()
        return {'status': 'healthy', 'database': 'connected'}
    except Exception:
        from fastapi import HTTPException
        raise HTTPException(status_code=503, detail='Base de datos no disponible')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
