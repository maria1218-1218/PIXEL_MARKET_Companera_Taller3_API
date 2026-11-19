# GUIA COMENTARIOS LINEA A LINEA

Proyecto: Taller_3_API - PIXEL MARKET

Esta guia documenta las lineas reales, en orden, y conserva intacta la sintaxis del codigo.
Los archivos JSON, JSX y los fragmentos especiales requieren comentarios externos para no perder validez.
Las lineas se numeran segun los archivos entregados en este paquete.


## `.github/workflows/quality.yml`

Objetivo: archivo .yml integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: consulta la guia de linea por linea.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `name: Verificar calidad y pruebas` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L003** `on:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L004** `push:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L005** `pull_request:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L006** `jobs:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L007** `quality:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L008** `runs-on: ubuntu-latest` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L009** `steps:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L010** `- uses: actions/checkout@v4` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L011** `- uses: actions/setup-python@v5` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L012** `with:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L013** `python-version: '3.12'` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L014** `- name: Instalar dependencias` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L015** `run: pip install -r requirements.txt` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L016** `- name: Revisar estilo` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L017** `run: ruff format . && ruff check .` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L018** `- name: Ejecutar pruebas` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L019** `run: pytest -v` — Asigna, configura o define un valor utilizado por el resto del bloque.

## `.pre-commit-config.yaml`

Objetivo: archivo .yaml integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: consulta la guia de linea por linea.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `repos:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L003** `- repo: https://github.com/astral-sh/ruff-pre-commit` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L004** `rev: v0.9.10` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L005** `hooks:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L006** `- id: ruff` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L007** `- id: ruff-format` — Asigna, configura o define un valor utilizado por el resto del bloque.

## `compose.yaml`

Objetivo: archivo .yaml integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: consulta la guia de linea por linea.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `services:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L003** `api:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L004** `build: .` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L005** `ports:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L006** `- "8000:8000"` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L007** `environment:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L008** `DATABASE_URL: sqlite:////app/data/videojuegos.db` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L009** `volumes:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L010** `- tienda_datos:/app/data` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L011** `volumes:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L012** `tienda_datos:` — Asigna, configura o define un valor utilizado por el resto del bloque.

## `main.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""Punto de entrada de PIXEL MARKET: REST API y portada de presentacion."""` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L003** `from contextlib import asynccontextmanager` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L004** `from pathlib import Path` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L005** `from fastapi import FastAPI` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L006** `from fastapi.middleware.cors import CORSMiddleware` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L007** `from fastapi.responses import FileResponse` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L008** `from fastapi.staticfiles import StaticFiles` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L009** `from sqlalchemy import text` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L010** `from sqlmodel import Session` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L011** `from tienda_api.config import settings` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L012** `from tienda_api.database import create_db_and_tables, engine` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L013** `from tienda_api.routers import usuarios, juegos, favoritos` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L014** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L015** `# El contexto lifespan crea las tablas antes de aceptar consultas.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L016** `@asynccontextmanager` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L017** `async def lifespan(app: FastAPI):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L018** `"""Crear esquema SQLite al iniciar la API."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L019** `create_db_and_tables()` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L020** `yield` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L021** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L022** `# Se configura la documentacion OpenAPI de la API.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L023** `app = FastAPI(` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L024** `title=settings.app_name,` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L025** `description='API RESTful para usuarios, videojuegos y listas de favoritos. Proyecto academico LPA2.',` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L026** `version=settings.app_version,` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L027** `contact={'name': 'Proyecto academico LPA2'},` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L028** `license_info={'name': 'Uso educativo'},` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L029** `lifespan=lifespan,` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L030** `)` — Cierra la estructura abierta anteriormente.
- **L031** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L032** `# Permitir el consumo del frontend local del Taller 4.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L033** `app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*'])` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L034** `app.include_router(usuarios.router)` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L035** `app.include_router(juegos.router)` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L036** `app.include_router(favoritos.router)` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L037** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L038** `# Servir estilos locales de la pagina de introduccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L039** `app.mount('/static', StaticFiles(directory=Path(__file__).parent / 'static'), name='static')` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L040** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L041** `@app.get('/', include_in_schema=False)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L042** `def portada():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L043** `"""Mostrar una portada visual; el REST API permanece bajo /api."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L044** `return FileResponse(Path(__file__).parent / 'static' / 'index.html')` — Devuelve un resultado al llamador, la vista o el servicio.
- **L045** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L046** `@app.get('/api', tags=['Estado'])` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L047** `def informacion():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L048** `"""Resumen JSON de recursos disponibles para integraciones externas."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L049** `return {'nombre': settings.app_name, 'version': settings.app_version, 'recursos': ['/api/usuarios', '/api/juegos', '/api/favoritos'], 'docs': '/docs'}` — Devuelve un resultado al llamador, la vista o el servicio.
- **L050** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L051** `# El endpoint de salud permite confirmar que SQLite responde.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L052** `@app.get('/health', tags=['Estado'])` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L053** `def salud():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L054** `"""Verificar conexion activa con la base de datos."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L055** `try:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L056** `with Session(engine) as session:` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L057** `session.execute(text('SELECT 1')).first()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L058** `return {'status': 'healthy', 'database': 'connected'}` — Devuelve un resultado al llamador, la vista o el servicio.
- **L059** `except Exception:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L060** `from fastapi import HTTPException` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L061** `raise HTTPException(status_code=503, detail='Base de datos no disponible')` — Produce un error explicito para informar una situacion no valida.
- **L062** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L063** `if __name__ == '__main__':` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L064** `import uvicorn` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L065** `uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)` — Asigna, configura o define un valor utilizado por el resto del bloque.

## `pyproject.toml`

Objetivo: archivo .toml integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: consulta la guia de linea por linea.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `# Reglas usadas tanto localmente como en CI.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L003** `[tool.ruff]` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L004** `line-length = 120` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L005** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L006** `[tool.ruff.lint]` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L007** `select = ["E4", "E7", "E9", "F"]` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L008** `ignore = ["E701", "E702"]` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L009** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L010** `[tool.pytest.ini_options]` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L011** `testpaths = ["tests"]` — Asigna, configura o define un valor utilizado por el resto del bloque.

## `sql/datos_dbeaver.sql`

Objetivo: archivo .sql integrante del taller.

- **L001** `-- ARCHIVO DIDACTICO: el SQL se explica paso a paso en la guia.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `-- Datos ficticios para insertar desde DBeaver en una base vacia.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L003** `-- Ejecutar despues de iniciar la API una vez para crear las tablas.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L004** `-- Correos de ejemplo, sin informacion de personas reales.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L005** `INSERT INTO usuario (nombre, correo, fecha_registro) VALUES` — Instruccion SQL que crea, inserta o consulta registros de la base de datos.
- **L006** `('Valeria Torres', 'valeria.demo@example.com', CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L007** `('Mateo Rios', 'mateo.demo@example.com', CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L008** `('Daniela Vega', 'daniela.demo@example.com', CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L009** `('Sebastian Mora', 'sebastian.demo@example.com', CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L010** `('Camila Soto', 'camila.demo@example.com', CURRENT_TIMESTAMP);` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L011** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L012** `-- Catalogo inventado. Los titulos no corresponden a licencias reales.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L013** `INSERT INTO juego (titulo, desarrollador, plataforma, genero, precio, anio_lanzamiento, descripcion, disponible, fecha_creacion) VALUES` — Instruccion SQL que crea, inserta o consulta registros de la base de datos.
- **L014** `('Nebula Rift', 'Pixel Forge', 'PC', 'RPG', 89000, 2025, 'Aventura espacial cooperativa', 1, CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L015** `('Circuit Rush', 'Volt Studio', 'Xbox', 'Carreras', 56000, 2024, 'Competencia futurista en pistas neon', 1, CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L016** `('Frost Kingdom', 'North Byte', 'PC', 'Estrategia', 79000, 2023, 'Construye un reino entre montanas heladas', 1, CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L017** `('Titan Protocol', 'Argon Games', 'Xbox', 'Accion', 110000, 2025, 'Combate tactico con robots gigantes', 1, CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L018** `('Echoes of Terra', 'Wild Pixel', 'PC', 'Aventura', 65000, 2022, 'Explora ecosistemas desconocidos', 1, CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L019** `('Shadow Circuit', 'Neon Works', 'PC', 'Sigilo', 44000, 2024, 'Infiltracion en una metropoli cibernetica', 1, CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L020** `('Ocean Legends', 'Blue Wave', 'Xbox', 'RPG', 93000, 2021, 'Viaje fantastico bajo el oceano', 1, CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L021** `('Skyline Architect', 'Urban Lab', 'PC', 'Simulacion', 33000, 2020, 'Disena la ciudad del futuro', 1, CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L022** `('Iron Arena', 'Steel Dev', 'Xbox', 'Deportes', 48000, 2023, 'Torneo competitivo de robots', 1, CURRENT_TIMESTAMP),` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L023** `('Moon Garden', 'Lunar Indie', 'PC', 'Indie', 24000, 2025, 'Construye un jardin en la luna', 1, CURRENT_TIMESTAMP);` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.

## `static/index.html`

Objetivo: archivo .html integrante del taller.

- **L001** `<!doctype html>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L002** `<!-- ARCHIVO DIDACTICO: etiquetas y atributos explicados en la guia. -->` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L003** `<html lang="es">` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L004** `<head>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L005** `<meta charset="utf-8">` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L006** `<meta name="viewport" content="width=device-width, initial-scale=1">` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L007** `<meta name="description" content="Pixel Market - API RESTful de videojuegos digitales">` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L008** `<title>PIXEL MARKET | API</title>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L009** `<!-- Bootstrap aporta componentes, cuadriculas responsivas y utilidades de espacio. -->` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L010** `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L011** `<!-- La identidad visual vive en un archivo CSS independiente. -->` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L012** `<link href="/static/styles.css" rel="stylesheet">` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L013** `</head>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L014** `<body>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L015** `<!-- Navegacion simple con accesos a la documentacion automatica. -->` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L016** `<nav class="navbar navbar-expand-lg navbar-dark py-3 border-bottom border-secondary-subtle">` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L017** `<div class="container"><a class="navbar-brand brand" href="/">◈ PIXEL<span>GAMES</span></a>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L018** `<div class="d-flex gap-2"><a class="btn btn-outline-info btn-sm" href="/docs">Swagger API</a><a class="btn btn-outline-light btn-sm" href="/redoc">ReDoc</a></div>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L019** `</div>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L020** `</nav>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L021** `<main class="container py-5">` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L022** `<!-- Encabezado de presentacion; la API real se consume por /api. -->` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L023** `<div class="row align-items-center g-5 hero">` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L024** `<div class="col-lg-7"><p class="eyebrow">LPA2 / TALLER 03 / BACKEND</p><h1>Tu espacio de <em>videojuegos</em> empieza aqui.</h1>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L025** `<p class="lead muted mt-4">API de tienda digital inspirada en catalogos de videojuegos. Administra usuarios, juegos y listas de deseos con FastAPI, SQLModel y Pydantic...` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L026** `<div class="d-flex gap-3 flex-wrap mt-4"><a href="/docs" class="btn btn-primary px-4 py-3">Explorar endpoints ↗</a><a href="/api" class="btn btn-outline-light px-4 py-...` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L027** `</div>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L028** `<div class="col-lg-5"><div class="feature p-4"><div class="mini-title">ESTADO DEL SERVICIO</div><div class="status" id="estado"><span class="dot"></span> Consultando A...` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L029** `</div>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L030** `<!-- Tarjetas de recursos gestionados por el backend. -->` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L031** `<section class="mt-5 pt-5"><p class="eyebrow">SERVICIOS PRINCIPALES</p><h2 class="mb-4">Gestion del catalogo</h2>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L032** `<div class="row g-4">` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L033** `<div class="col-md-4"><article class="feature p-4 h-100"><span class="symbol">01</span><h3>Usuarios</h3><p>Registro, consulta, actualizacion y eliminacion de perfiles....` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L034** `<div class="col-md-4"><article class="feature p-4 h-100"><span class="symbol">02</span><h3>Juegos</h3><p>Catalogo con precios, plataformas, generos y busqueda avanzada...` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L035** `<div class="col-md-4"><article class="feature p-4 h-100"><span class="symbol">03</span><h3>Favoritos</h3><p>Listas de deseos de cada usuario sin registros duplicados.<...` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L036** `</div>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L037** `</section>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L038** `<section class="feature p-4 p-md-5 mt-5"><p class="eyebrow">PREPARADO PARA EL TALLER 4</p><h2>API lista para conectar a un frontend</h2><p>Las rutas responden JSON. El...` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L039** `</main>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L040** `<footer class="container py-4 muted border-top border-secondary-subtle">PIXEL MARKET · Proyecto academico · LPA2</footer>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L041** `<!-- Consulta del estado; no modifica el contenido de la base de datos. -->` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L042** `<script>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L043** `fetch('/health').then(res => { if (!res.ok) throw new Error('No disponible'); return res.json(); })` — Devuelve un resultado al llamador, la vista o el servicio.
- **L044** `.then(() => { document.getElementById('estado').innerHTML = '<span class="dot"></span> API operativa'; })` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L045** `.catch(() => { document.getElementById('estado').textContent = 'Servicio no disponible'; });` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L046** `</script>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L047** `</body>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.
- **L048** `</html>` — Estructura visual: renderiza elementos o componentes accesibles de la interfaz.

## `static/styles.css`

Objetivo: archivo .css integrante del taller.

- **L001** `/* ARCHIVO DIDACTICO: cada regla se explica tambien en la guia de codigo. */` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `/* Tema tecnologico oscuro de PIXEL MARKET. Variables faciles de personalizar. */` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L003** `:root { --fondo:#130f18; --panel:#261c2a; --borde:#493344; --texto:#fff3e6; --suave:#c7b5b2; --acento:#ffb454; }` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L004** `/* Tipografia legible, espaciado generoso y fondo con brillos sutiles. */` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L005** `body { color:var(--texto); background:radial-gradient(ellipse at 82% 9%,#493043 0,transparent 31%), var(--fondo); font-family:system-ui,-apple-system,"Segoe UI",sans-s...` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L006** `/* Logotipo de dos tonos. */` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L007** `.brand { font-weight:900;letter-spacing:.09em; }.brand span { color:var(--acento); }` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L008** `/* Hero responsivo que evita textos demasiado largos. */` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L009** `.hero { min-height:420px; } h1 { font-size:clamp(2.8rem,6vw,5rem);font-weight:850;line-height:1.06;letter-spacing:-.055em; } h1 em { color:var(--acento);font-style:nor...` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L010** `/* Texto secundario con buen contraste. */` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L011** `.muted,.feature p,small {color:var(--suave);} .eyebrow,.mini-title {color:var(--acento);font-size:.8rem;font-weight:800;letter-spacing:.18em;}` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L012** `/* Botones con identidad azul turquesa. */` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L013** `.btn-primary {background:var(--acento);border-color:var(--acento);color:#24161c;font-weight:700;} .btn-primary:hover {background:#ffd992;border-color:#ffd992;color:#24...` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L014** `/* Tarjetas para los tres recursos principales del API. */` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L015** `.feature {background:linear-gradient(145deg,rgba(23,44,69,.94),rgba(10,21,37,.96));border:1px solid var(--borde);border-radius:22px;box-shadow:0 12px 42px rgba(0,0,0,....` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L016** `.feature a {color:var(--acento);text-decoration:none;font-weight:600;} .feature a:hover {text-decoration:underline;}.feature .btn {color:var(--acento);} .symbol {displ...` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L017** `/* Indicadores y detalle del estado en tiempo real. */` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L018** `.metric {font-size:3.2rem;font-weight:850;letter-spacing:-.05em;} .status {font-weight:700;font-size:1.3rem;margin-top:1rem;} .dot {display:inline-block;width:10px;hei...` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L019** `/* Presentacion elegante del ejemplo de endpoint. */` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L020** `code {color:#8cddfa;word-break:break-word;} hr {border-color:var(--borde);opacity:1;margin:1.6rem 0;}` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L021** `/* Accesibilidad y ajustes para pantallas estrechas. */` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L022** `@media(max-width:576px){.hero{min-height:auto;}.feature{border-radius:16px;}h1{font-size:2.8rem;}}` — Decorador: configura rutas, validadores o metadatos de ejecucion.

## `tests/conftest.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""Datos aislados: cada prueba crea una base SQLite en memoria."""` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L003** `import pytest` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L004** `from fastapi.testclient import TestClient` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L005** `from sqlmodel import SQLModel, Session, create_engine` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L006** `from sqlmodel.pool import StaticPool` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L007** `from main import app` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L008** `from tienda_api.database import get_session` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L009** `from tienda_api import models  # noqa: F401` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L010** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L011** `@pytest.fixture` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L012** `def session():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L013** `"""Crear tablas y abrir sesion independiente por prueba."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L014** `engine = create_engine('sqlite://', connect_args={'check_same_thread': False}, poolclass=StaticPool)` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L015** `SQLModel.metadata.create_all(engine)` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L016** `with Session(engine) as session:` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L017** `yield session` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L018** `engine.dispose()` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L019** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L020** `@pytest.fixture` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L021** `def client(session):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L022** `"""Reemplazar la dependencia de SQLite por la sesion de prueba."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L023** `def get_session_override():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L024** `yield session` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L025** `app.dependency_overrides[get_session] = get_session_override` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L026** `with TestClient(app) as test_client:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L027** `yield test_client` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L028** `app.dependency_overrides.clear()` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L029** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L030** `@pytest.fixture` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L031** `def usuario(client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L032** `"""Crear usuario reutilizable a traves de la API publica."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L033** `return client.post('/api/usuarios', json={'nombre': 'Cliente Demo', 'correo': 'cliente@example.com'}).json()` — Devuelve un resultado al llamador, la vista o el servicio.
- **L034** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L035** `@pytest.fixture` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L036** `def juego(client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L037** `"""Registrar juego ficticio para pruebas."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L038** `return client.post('/api/juegos', json={` — Devuelve un resultado al llamador, la vista o el servicio.
- **L039** `'titulo': 'Reinos de Neon', 'desarrollador': 'Estudio Demo', 'plataforma': 'PC',` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L040** `'genero': 'RPG', 'precio': 54900, 'anio_lanzamiento': 2024,` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L041** `'descripcion': 'Juego ficticio para pruebas', 'disponible': True,` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L042** `}).json()` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.

## `tests/test_api.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""Pruebas CRUD, validaciones, errores y flujo integrado de tienda."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L003** `class TestEstado:` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L004** `def test_documentacion(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L005** `assert client.get('/openapi.json').status_code == 200` — Asercion automatizada para comprobar el comportamiento esperado.
- **L006** `def test_info(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L007** `assert '/api/juegos' in client.get('/api').json()['recursos']` — Asercion automatizada para comprobar el comportamiento esperado.
- **L008** `def test_portada(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L009** `assert client.get('/').status_code == 200` — Asercion automatizada para comprobar el comportamiento esperado.
- **L010** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L011** `class TestUsuarios:` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L012** `def test_lista_inicial(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L013** `assert client.get('/api/usuarios').json() == []` — Asercion automatizada para comprobar el comportamiento esperado.
- **L014** `def test_crear_y_consultar(self, client, usuario):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L015** `assert client.get(f"/api/usuarios/{usuario['id']}").json()['correo'] == 'cliente@example.com'` — Asercion automatizada para comprobar el comportamiento esperado.
- **L016** `def test_correo_duplicado(self, client, usuario):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L017** `r = client.post('/api/usuarios', json={'nombre': 'Otro Cliente', 'correo': usuario['correo']})` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L018** `assert r.status_code == 409` — Asercion automatizada para comprobar el comportamiento esperado.
- **L019** `def test_correo_invalido(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L020** `assert client.post('/api/usuarios', json={'nombre': 'Prueba', 'correo': 'incorrecto'}).status_code == 422` — Asercion automatizada para comprobar el comportamiento esperado.
- **L021** `def test_nombre_corto(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L022** `assert client.post('/api/usuarios', json={'nombre': 'A', 'correo': 'a@demo.com'}).status_code == 422` — Asercion automatizada para comprobar el comportamiento esperado.
- **L023** `def test_actualizar(self, client, usuario):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L024** `r = client.put(f"/api/usuarios/{usuario['id']}", json={'nombre': 'Nuevo Nombre'})` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L025** `assert r.status_code == 200 and r.json()['nombre'] == 'Nuevo Nombre'` — Asercion automatizada para comprobar el comportamiento esperado.
- **L026** `def test_eliminar(self, client, usuario):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L027** `assert client.delete(f"/api/usuarios/{usuario['id']}").status_code == 204` — Asercion automatizada para comprobar el comportamiento esperado.
- **L028** `assert client.get(f"/api/usuarios/{usuario['id']}").status_code == 404` — Asercion automatizada para comprobar el comportamiento esperado.
- **L029** `def test_no_encontrado(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L030** `assert client.get('/api/usuarios/999').status_code == 404` — Asercion automatizada para comprobar el comportamiento esperado.
- **L031** `def test_paginacion(self, client, usuario):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L032** `assert len(client.get('/api/usuarios?limit=1&offset=0').json()) == 1` — Asercion automatizada para comprobar el comportamiento esperado.
- **L033** `assert client.get('/api/usuarios?limit=1&offset=1').json() == []` — Asercion automatizada para comprobar el comportamiento esperado.
- **L034** `def test_paginacion_invalida(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L035** `assert client.get('/api/usuarios?limit=1000').status_code == 422` — Asercion automatizada para comprobar el comportamiento esperado.
- **L036** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L037** `class TestJuegos:` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L038** `def test_lista_vacia(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L039** `assert client.get('/api/juegos').json() == []` — Asercion automatizada para comprobar el comportamiento esperado.
- **L040** `def test_crear_y_consultar(self, client, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L041** `assert client.get(f"/api/juegos/{juego['id']}").json()['titulo'] == 'Reinos de Neon'` — Asercion automatizada para comprobar el comportamiento esperado.
- **L042** `def test_precio_negativo(self, client, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L043** `datos = {**juego, 'precio': -3}` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L044** `assert client.post('/api/juegos', json=datos).status_code == 422` — Asercion automatizada para comprobar el comportamiento esperado.
- **L045** `def test_anio_invalido(self, client, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L046** `datos = {**juego, 'anio_lanzamiento': 2200}` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L047** `assert client.post('/api/juegos', json=datos).status_code == 422` — Asercion automatizada para comprobar el comportamiento esperado.
- **L048** `def test_campos_obligatorios(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L049** `assert client.post('/api/juegos', json={'titulo': 'Sin Datos'}).status_code == 422` — Asercion automatizada para comprobar el comportamiento esperado.
- **L050** `def test_actualizar_precio(self, client, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L051** `r = client.put(f"/api/juegos/{juego['id']}", json={'precio': 30000})` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L052** `assert r.json()['precio'] == 30000` — Asercion automatizada para comprobar el comportamiento esperado.
- **L053** `def test_busqueda(self, client, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L054** `assert len(client.get('/api/juegos/buscar?titulo=neon&genero=rpg&plataforma=PC&precio_max=60000').json()) == 1` — Asercion automatizada para comprobar el comportamiento esperado.
- **L055** `assert client.get('/api/juegos/buscar?genero=Simulador').json() == []` — Asercion automatizada para comprobar el comportamiento esperado.
- **L056** `def test_paginacion(self, client, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L057** `assert client.get('/api/juegos?offset=1&limit=1').json() == []` — Asercion automatizada para comprobar el comportamiento esperado.
- **L058** `def test_inexistente(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L059** `assert client.get('/api/juegos/999').status_code == 404` — Asercion automatizada para comprobar el comportamiento esperado.
- **L060** `def test_eliminar(self, client, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L061** `assert client.delete(f"/api/juegos/{juego['id']}").status_code == 204` — Asercion automatizada para comprobar el comportamiento esperado.
- **L062** `assert client.get(f"/api/juegos/{juego['id']}").status_code == 404` — Asercion automatizada para comprobar el comportamiento esperado.
- **L063** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L064** `class TestFavoritos:` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L065** `def test_lista_vacia(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L066** `assert client.get('/api/favoritos').json() == []` — Asercion automatizada para comprobar el comportamiento esperado.
- **L067** `def test_crear_y_consultar(self, client, usuario, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L068** `r = client.post('/api/favoritos', json={'id_usuario': usuario['id'], 'id_juego': juego['id']})` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L069** `assert r.status_code == 201` — Asercion automatizada para comprobar el comportamiento esperado.
- **L070** `assert client.get(f"/api/favoritos/{r.json()['id']}").status_code == 200` — Asercion automatizada para comprobar el comportamiento esperado.
- **L071** `def test_duplicado(self, client, usuario, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L072** `datos = {'id_usuario': usuario['id'], 'id_juego': juego['id']}` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L073** `assert client.post('/api/favoritos', json=datos).status_code == 201` — Asercion automatizada para comprobar el comportamiento esperado.
- **L074** `assert client.post('/api/favoritos', json=datos).status_code == 409` — Asercion automatizada para comprobar el comportamiento esperado.
- **L075** `def test_usuario_invalido(self, client, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L076** `assert client.post('/api/favoritos', json={'id_usuario': 999, 'id_juego': juego['id']}).status_code == 404` — Asercion automatizada para comprobar el comportamiento esperado.
- **L077** `def test_juego_invalido(self, client, usuario):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L078** `assert client.post('/api/favoritos', json={'id_usuario': usuario['id'], 'id_juego': 999}).status_code == 404` — Asercion automatizada para comprobar el comportamiento esperado.
- **L079** `def test_favorito_inexistente(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L080** `assert client.get('/api/favoritos/999').status_code == 404` — Asercion automatizada para comprobar el comportamiento esperado.
- **L081** `def test_borrar_favorito(self, client, usuario, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L082** `datos = {'id_usuario': usuario['id'], 'id_juego': juego['id']}` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L083** `fav = client.post('/api/favoritos', json=datos).json()` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L084** `assert client.delete(f"/api/favoritos/{fav['id']}").status_code == 204` — Asercion automatizada para comprobar el comportamiento esperado.
- **L085** `def test_desde_usuario(self, client, usuario, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L086** `ruta = f"/api/usuarios/{usuario['id']}/favoritos/{juego['id']}"` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L087** `assert client.post(ruta).status_code == 201` — Asercion automatizada para comprobar el comportamiento esperado.
- **L088** `assert len(client.get(f"/api/usuarios/{usuario['id']}/favoritos").json()) == 1` — Asercion automatizada para comprobar el comportamiento esperado.
- **L089** `assert client.delete(ruta).status_code == 204` — Asercion automatizada para comprobar el comportamiento esperado.
- **L090** `def test_cascada_logica_juego(self, client, usuario, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L091** `client.post('/api/favoritos', json={'id_usuario': usuario['id'], 'id_juego': juego['id']})` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L092** `client.delete(f"/api/juegos/{juego['id']}")` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L093** `assert client.get('/api/favoritos').json() == []` — Asercion automatizada para comprobar el comportamiento esperado.
- **L094** `def test_cascada_logica_usuario(self, client, usuario, juego):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L095** `client.post('/api/favoritos', json={'id_usuario': usuario['id'], 'id_juego': juego['id']})` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L096** `client.delete(f"/api/usuarios/{usuario['id']}")` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L097** `assert client.get('/api/favoritos').json() == []` — Asercion automatizada para comprobar el comportamiento esperado.
- **L098** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L099** `class TestIntegracion:` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L100** `def test_flujo_completo(self, client):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L101** `usuario = client.post('/api/usuarios', json={'nombre':'Cliente Final', 'correo':'final@example.com'}).json()` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L102** `juego = client.post('/api/juegos', json={'titulo':'Galaxia Infinita', 'desarrollador':'Prueba Studio', 'plataforma':'Xbox', 'genero':'Accion', 'precio':90000, 'anio_la...` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L103** `r = client.post('/api/favoritos', json={'id_usuario':usuario['id'], 'id_juego':juego['id']})` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L104** `assert r.status_code == 201` — Asercion automatizada para comprobar el comportamiento esperado.
- **L105** `assert len(client.get(f"/api/usuarios/{usuario['id']}/favoritos").json()) == 1` — Asercion automatizada para comprobar el comportamiento esperado.
- **L106** `assert client.get('/api/juegos/buscar?plataforma=Xbox').json()[0]['id'] == juego['id']` — Asercion automatizada para comprobar el comportamiento esperado.

## `tests/test_utils.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""Pruebas de funciones auxiliares de la plantilla original."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L003** `import pytest` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L004** `from utils import validar_correo, formatear_duracion, generar_slug, obtener_anio_actual, validar_anio` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L005** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L006** `def test_correos():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L007** `assert validar_correo('persona@correo.com')` — Asercion automatizada para comprobar el comportamiento esperado.
- **L008** `assert not validar_correo('correo-invalido')` — Asercion automatizada para comprobar el comportamiento esperado.
- **L009** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L010** `def test_duracion():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L011** `assert formatear_duracion(125) == '02:05'` — Asercion automatizada para comprobar el comportamiento esperado.
- **L012** `with pytest.raises(ValueError):` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L013** `formatear_duracion(-1)` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L014** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L015** `def test_slug():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L016** `assert generar_slug('Edicion Epica: Accion!') == 'edicion-epica-accion'` — Asercion automatizada para comprobar el comportamiento esperado.
- **L017** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L018** `def test_anio():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L019** `assert validar_anio(2020)` — Asercion automatizada para comprobar el comportamiento esperado.
- **L020** `assert not validar_anio(1800)` — Asercion automatizada para comprobar el comportamiento esperado.
- **L021** `assert obtener_anio_actual() >= 2026` — Asercion automatizada para comprobar el comportamiento esperado.

## `tienda_api/__init__.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""API academica de juegos digitales."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.

## `tienda_api/config.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""Configuracion obtenida de variables de entorno."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L003** `from pydantic_settings import BaseSettings, SettingsConfigDict` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L004** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L005** `class Settings(BaseSettings):` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L006** `"""Parametros de la aplicacion."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L007** `app_name: str = "PIXEL MARKET | API de videojuegos"` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L008** `app_version: str = "1.0.0"` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L009** `database_url: str = "sqlite:///./videojuegos.db"` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L010** `cors_origins: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:8000", "http://127.0.0.1:8000"]` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L011** `model_config = SettingsConfigDict(env_file=".env", extra="ignore")` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L012** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L013** `settings = Settings()` — Asigna, configura o define un valor utilizado por el resto del bloque.

## `tienda_api/database.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""Conexion SQLite mediante SQLModel. Compartida por los routers."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L003** `from sqlmodel import SQLModel, Session, create_engine` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L004** `from tienda_api.config import settings` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L005** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L006** `connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}` — Regla o propiedad de presentacion que define aspecto, espaciado o comportamiento responsive.
- **L007** `engine = create_engine(settings.database_url, connect_args=connect_args)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L008** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L009** `def create_db_and_tables():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L010** `"""Crear las tablas al iniciar el servidor."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L011** `from tienda_api import models  # noqa: F401` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L012** `SQLModel.metadata.create_all(engine)` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L013** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L014** `def get_session():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L015** `"""Proporcionar una sesion y cerrarla al terminar la solicitud."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L016** `with Session(engine) as session:` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L017** `yield session` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.

## `tienda_api/models.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""Modelos de persistencia y esquemas de entrada y salida de la API."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L003** `from datetime import datetime, timezone` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L004** `from typing import Optional` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L005** `from pydantic import EmailStr, Field as PField, field_validator` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L006** `from sqlmodel import SQLModel, Field, UniqueConstraint` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L007** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L008** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L009** `def now_utc():` — Declara una funcion con parametros y comportamiento reutilizable.
- **L010** `"""Generar sello de tiempo UTC sin dependencias externas."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L011** `return datetime.now(timezone.utc)` — Devuelve un resultado al llamador, la vista o el servicio.
- **L012** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L013** `class UsuarioBase(SQLModel):` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L014** `"""Propiedades publicas del usuario."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L015** `nombre: str = PField(min_length=2, max_length=90)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L016** `correo: str = PField(min_length=5, max_length=255)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L017** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L018** `class Usuario(UsuarioBase, table=True):` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L019** `"""Tabla de usuarios con correo unico."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L020** `id: Optional[int] = Field(default=None, primary_key=True)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L021** `correo: str = Field(index=True, unique=True, max_length=255)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L022** `fecha_registro: datetime = Field(default_factory=now_utc)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L023** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L024** `class UsuarioCreate(UsuarioBase):` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L025** `"""Esquema para crear una cuenta con validacion real de email."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L026** `correo: EmailStr` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L027** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L028** `class UsuarioUpdate(SQLModel):` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L029** `"""Esquema para modificar datos de una cuenta."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L030** `nombre: Optional[str] = PField(default=None, min_length=2, max_length=90)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L031** `correo: Optional[EmailStr] = None` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L032** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L033** `class JuegoBase(SQLModel):` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L034** `"""Informacion comercial de un videojuego digital."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L035** `titulo: str = PField(min_length=2, max_length=150)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L036** `desarrollador: str = PField(min_length=2, max_length=120)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L037** `plataforma: str = PField(min_length=2, max_length=40)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L038** `genero: str = PField(min_length=2, max_length=80)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L039** `precio: float = PField(ge=0, le=10000000)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L040** `anio_lanzamiento: int = PField(ge=1970, le=2100)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L041** `descripcion: str = PField(default="", max_length=1000)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L042** `disponible: bool = True` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L043** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L044** `@field_validator('anio_lanzamiento')` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L045** `@classmethod` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L046** `def validar_anio(cls, value):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L047** `"""Evitar juegos con un anio de lanzamiento irrealmente futuro."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L048** `if value > now_utc().year + 3:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L049** `raise ValueError('Anio de lanzamiento demasiado lejano')` — Produce un error explicito para informar una situacion no valida.
- **L050** `return value` — Devuelve un resultado al llamador, la vista o el servicio.
- **L051** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L052** `class Juego(JuegoBase, table=True):` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L053** `"""Tabla de juegos del catalogo."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L054** `id: Optional[int] = Field(default=None, primary_key=True)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L055** `fecha_creacion: datetime = Field(default_factory=now_utc)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L056** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L057** `class JuegoCreate(JuegoBase):` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L058** `"""Datos validados al crear un juego."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L059** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L060** `class JuegoUpdate(SQLModel):` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L061** `"""Datos opcionales al actualizar un juego."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L062** `titulo: Optional[str] = PField(default=None, min_length=2, max_length=150)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L063** `desarrollador: Optional[str] = PField(default=None, min_length=2, max_length=120)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L064** `plataforma: Optional[str] = PField(default=None, min_length=2, max_length=40)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L065** `genero: Optional[str] = PField(default=None, min_length=2, max_length=80)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L066** `precio: Optional[float] = PField(default=None, ge=0, le=10000000)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L067** `anio_lanzamiento: Optional[int] = PField(default=None, ge=1970, le=2100)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L068** `descripcion: Optional[str] = PField(default=None, max_length=1000)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L069** `disponible: Optional[bool] = None` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L070** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L071** `@field_validator('anio_lanzamiento')` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L072** `@classmethod` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L073** `def validar_anio(cls, value):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L074** `if value is not None and value > now_utc().year + 3:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L075** `raise ValueError('Anio de lanzamiento demasiado lejano')` — Produce un error explicito para informar una situacion no valida.
- **L076** `return value` — Devuelve un resultado al llamador, la vista o el servicio.
- **L077** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L078** `class Favorito(SQLModel, table=True):` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L079** `"""Relacion entre un usuario y un juego marcado como favorito."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L080** `__table_args__ = (UniqueConstraint('id_usuario', 'id_juego', name='uq_usuario_juego'),)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L081** `id: Optional[int] = Field(default=None, primary_key=True)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L082** `id_usuario: int = Field(foreign_key='usuario.id')` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L083** `id_juego: int = Field(foreign_key='juego.id')` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L084** `fecha_marcado: datetime = Field(default_factory=now_utc)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L085** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L086** `class FavoritoCreate(SQLModel):` — Declara un tipo o clase, definiendo su estructura y responsabilidades.
- **L087** `"""Identificadores para registrar un favorito."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L088** `id_usuario: int = PField(gt=0)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L089** `id_juego: int = PField(gt=0)` — Asigna, configura o define un valor utilizado por el resto del bloque.

## `tienda_api/routers/__init__.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""Routers del catalogo, usuarios y favoritos."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.

## `tienda_api/routers/favoritos.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""Operaciones sobre la lista de deseos de los clientes."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L003** `from fastapi import APIRouter, Depends, HTTPException, Query, Response` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L004** `from sqlalchemy.exc import IntegrityError` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L005** `from sqlmodel import Session, select` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L006** `from tienda_api.database import get_session` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L007** `from tienda_api.models import Favorito, FavoritoCreate, Usuario, Juego` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L008** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L009** `router = APIRouter(prefix='/api/favoritos', tags=['Favoritos'])` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L010** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L011** `@router.get('', response_model=list[Favorito])` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L012** `def listar_favoritos(offset: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100), session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L013** `"""Listado paginado de favoritos."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L014** `return session.exec(select(Favorito).offset(offset).limit(limit)).all()` — Devuelve un resultado al llamador, la vista o el servicio.
- **L015** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L016** `@router.post('', response_model=Favorito, status_code=201)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L017** `def crear_favorito(payload: FavoritoCreate, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L018** `"""Asociar juego y usuario, evitando referencias invalidas y duplicados."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L019** `if not session.get(Usuario, payload.id_usuario):` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L020** `raise HTTPException(404, 'Usuario no encontrado')` — Produce un error explicito para informar una situacion no valida.
- **L021** `if not session.get(Juego, payload.id_juego):` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L022** `raise HTTPException(404, 'Juego no encontrado')` — Produce un error explicito para informar una situacion no valida.
- **L023** `anterior = session.exec(select(Favorito).where(Favorito.id_usuario == payload.id_usuario, Favorito.id_juego == payload.id_juego)).first()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L024** `if anterior:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L025** `raise HTTPException(409, 'El juego ya esta en favoritos')` — Produce un error explicito para informar una situacion no valida.
- **L026** `favorito = Favorito.model_validate(payload)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L027** `session.add(favorito)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L028** `try:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L029** `session.commit()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L030** `except IntegrityError:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L031** `session.rollback()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L032** `raise HTTPException(409, 'El juego ya esta en favoritos')` — Produce un error explicito para informar una situacion no valida.
- **L033** `session.refresh(favorito)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L034** `return favorito` — Devuelve un resultado al llamador, la vista o el servicio.
- **L035** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L036** `@router.get('/{favorito_id}', response_model=Favorito)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L037** `def obtener_favorito(favorito_id: int, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L038** `"""Consultar una relacion de favoritos."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L039** `favorito = session.get(Favorito, favorito_id)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L040** `if favorito is None:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L041** `raise HTTPException(404, 'Favorito no encontrado')` — Produce un error explicito para informar una situacion no valida.
- **L042** `return favorito` — Devuelve un resultado al llamador, la vista o el servicio.
- **L043** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L044** `@router.delete('/{favorito_id}', status_code=204)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L045** `def eliminar_favorito(favorito_id: int, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L046** `"""Eliminar un favorito existente."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L047** `favorito = obtener_favorito(favorito_id, session)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L048** `session.delete(favorito)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L049** `session.commit()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L050** `return Response(status_code=204)` — Devuelve un resultado al llamador, la vista o el servicio.

## `tienda_api/routers/juegos.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""CRUD y busqueda de juegos digitales."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L003** `from fastapi import APIRouter, Depends, HTTPException, Query, Response` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L004** `from sqlmodel import Session, select` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L005** `from tienda_api.database import get_session` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L006** `from tienda_api.models import Juego, JuegoCreate, JuegoUpdate, Favorito` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L007** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L008** `router = APIRouter(prefix='/api/juegos', tags=['Juegos'])` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L009** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L010** `@router.get('', response_model=list[Juego])` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L011** `def listar_juegos(offset: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100), session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L012** `"""Catalogo paginado de juegos."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L013** `return session.exec(select(Juego).offset(offset).limit(limit)).all()` — Devuelve un resultado al llamador, la vista o el servicio.
- **L014** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L015** `@router.get('/buscar', response_model=list[Juego])` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L016** `def buscar_juegos(titulo: str | None = None, genero: str | None = None, plataforma: str | None = None, precio_max: float | None = Query(None, ge=0), offset: int = Quer...` — Declara una funcion con parametros y comportamiento reutilizable.
- **L017** `"""Filtrar catalogo por titulo, genero, plataforma y precio."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L018** `consulta = select(Juego)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L019** `if titulo:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L020** `consulta = consulta.where(Juego.titulo.ilike(f'%{titulo}%'))` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L021** `if genero:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L022** `consulta = consulta.where(Juego.genero.ilike(f'%{genero}%'))` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L023** `if plataforma:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L024** `consulta = consulta.where(Juego.plataforma.ilike(f'%{plataforma}%'))` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L025** `if precio_max is not None:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L026** `consulta = consulta.where(Juego.precio <= precio_max)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L027** `return session.exec(consulta.offset(offset).limit(limit)).all()` — Devuelve un resultado al llamador, la vista o el servicio.
- **L028** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L029** `@router.post('', response_model=Juego, status_code=201)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L030** `def crear_juego(payload: JuegoCreate, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L031** `"""Registrar videojuego con datos validados por Pydantic."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L032** `juego = Juego.model_validate(payload)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L033** `session.add(juego)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L034** `session.commit()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L035** `session.refresh(juego)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L036** `return juego` — Devuelve un resultado al llamador, la vista o el servicio.
- **L037** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L038** `@router.get('/{juego_id}', response_model=Juego)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L039** `def obtener_juego(juego_id: int, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L040** `"""Consultar un juego por ID."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L041** `juego = session.get(Juego, juego_id)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L042** `if juego is None:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L043** `raise HTTPException(404, 'Juego no encontrado')` — Produce un error explicito para informar una situacion no valida.
- **L044** `return juego` — Devuelve un resultado al llamador, la vista o el servicio.
- **L045** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L046** `@router.put('/{juego_id}', response_model=Juego)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L047** `def actualizar_juego(juego_id: int, payload: JuegoUpdate, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L048** `"""Actualizar uno o mas campos del juego."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L049** `juego = obtener_juego(juego_id, session)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L050** `juego.sqlmodel_update(payload.model_dump(exclude_unset=True))` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L051** `session.add(juego)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L052** `session.commit()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L053** `session.refresh(juego)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L054** `return juego` — Devuelve un resultado al llamador, la vista o el servicio.
- **L055** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L056** `@router.delete('/{juego_id}', status_code=204)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L057** `def eliminar_juego(juego_id: int, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L058** `"""Borrar favoritos asociados y despues el juego."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L059** `juego = obtener_juego(juego_id, session)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L060** `for favorito in session.exec(select(Favorito).where(Favorito.id_juego == juego_id)).all():` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L061** `session.delete(favorito)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L062** `session.delete(juego)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L063** `session.commit()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L064** `return Response(status_code=204)` — Devuelve un resultado al llamador, la vista o el servicio.

## `tienda_api/routers/usuarios.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""CRUD de cuentas de usuario y favoritos asociados."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L003** `from fastapi import APIRouter, Depends, HTTPException, Query, Response` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L004** `from sqlalchemy.exc import IntegrityError` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L005** `from sqlmodel import Session, select` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L006** `from tienda_api.database import get_session` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L007** `from tienda_api.models import Usuario, UsuarioCreate, UsuarioUpdate, Favorito` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L008** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L009** `router = APIRouter(prefix='/api/usuarios', tags=['Usuarios'])` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L010** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L011** `@router.get('', response_model=list[Usuario])` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L012** `def listar_usuarios(offset: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100), session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L013** `"""Listado paginado de usuarios."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L014** `return session.exec(select(Usuario).offset(offset).limit(limit)).all()` — Devuelve un resultado al llamador, la vista o el servicio.
- **L015** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L016** `@router.post('', response_model=Usuario, status_code=201)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L017** `def crear_usuario(payload: UsuarioCreate, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L018** `"""Crear usuario con correo unico."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L019** `usuario = Usuario.model_validate(payload)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L020** `usuario.correo = str(usuario.correo).lower()` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L021** `session.add(usuario)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L022** `try:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L023** `session.commit()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L024** `except IntegrityError:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L025** `session.rollback()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L026** `raise HTTPException(409, 'El correo ya esta registrado')` — Produce un error explicito para informar una situacion no valida.
- **L027** `session.refresh(usuario)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L028** `return usuario` — Devuelve un resultado al llamador, la vista o el servicio.
- **L029** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L030** `@router.get('/{usuario_id}', response_model=Usuario)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L031** `def obtener_usuario(usuario_id: int, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L032** `"""Recuperar un usuario por ID."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L033** `usuario = session.get(Usuario, usuario_id)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L034** `if usuario is None:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L035** `raise HTTPException(404, 'Usuario no encontrado')` — Produce un error explicito para informar una situacion no valida.
- **L036** `return usuario` — Devuelve un resultado al llamador, la vista o el servicio.
- **L037** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L038** `@router.put('/{usuario_id}', response_model=Usuario)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L039** `def actualizar_usuario(usuario_id: int, payload: UsuarioUpdate, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L040** `"""Modificar los campos proporcionados de un usuario."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L041** `usuario = obtener_usuario(usuario_id, session)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L042** `datos = payload.model_dump(exclude_unset=True)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L043** `if 'correo' in datos and datos['correo'] is not None:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L044** `datos['correo'] = str(datos['correo']).lower()` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L045** `usuario.sqlmodel_update(datos)` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L046** `session.add(usuario)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L047** `try:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L048** `session.commit()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L049** `except IntegrityError:` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L050** `session.rollback()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L051** `raise HTTPException(409, 'El correo ya esta registrado')` — Produce un error explicito para informar una situacion no valida.
- **L052** `session.refresh(usuario)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L053** `return usuario` — Devuelve un resultado al llamador, la vista o el servicio.
- **L054** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L055** `@router.delete('/{usuario_id}', status_code=204)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L056** `def eliminar_usuario(usuario_id: int, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L057** `"""Borrar favoritos del usuario antes de eliminar su cuenta."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L058** `usuario = obtener_usuario(usuario_id, session)` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L059** `for fav in session.exec(select(Favorito).where(Favorito.id_usuario == usuario_id)).all():` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L060** `session.delete(fav)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L061** `session.delete(usuario)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L062** `session.commit()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L063** `return Response(status_code=204)` — Devuelve un resultado al llamador, la vista o el servicio.
- **L064** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L065** `@router.get('/{usuario_id}/favoritos', response_model=list[Favorito])` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L066** `def favoritos_usuario(usuario_id: int, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L067** `"""Listar favoritos de una cuenta existente."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L068** `obtener_usuario(usuario_id, session)` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L069** `return session.exec(select(Favorito).where(Favorito.id_usuario == usuario_id)).all()` — Devuelve un resultado al llamador, la vista o el servicio.
- **L070** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L071** `@router.post('/{usuario_id}/favoritos/{juego_id}', response_model=Favorito, status_code=201)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L072** `def marcar_favorito(usuario_id: int, juego_id: int, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L073** `"""Marcar un juego como favorito."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L074** `from tienda_api.routers.favoritos import crear_favorito` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L075** `from tienda_api.models import FavoritoCreate` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L076** `return crear_favorito(FavoritoCreate(id_usuario=usuario_id, id_juego=juego_id), session)` — Devuelve un resultado al llamador, la vista o el servicio.
- **L077** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L078** `@router.delete('/{usuario_id}/favoritos/{juego_id}', status_code=204)` — Decorador: configura rutas, validadores o metadatos de ejecucion.
- **L079** `def quitar_favorito(usuario_id: int, juego_id: int, session: Session = Depends(get_session)):` — Declara una funcion con parametros y comportamiento reutilizable.
- **L080** `"""Quitar un juego de favoritos de un usuario."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L081** `favorito = session.exec(select(Favorito).where(Favorito.id_usuario == usuario_id, Favorito.id_juego == juego_id)).first()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L082** `if favorito is None:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L083** `raise HTTPException(404, 'Favorito no encontrado')` — Produce un error explicito para informar una situacion no valida.
- **L084** `session.delete(favorito)` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L085** `session.commit()` — Operacion de persistencia de datos mediante SQLModel/SQLAlchemy.
- **L086** `return Response(status_code=204)` — Devuelve un resultado al llamador, la vista o el servicio.

## `utils.py`

Objetivo: archivo .py integrante del taller.

- **L001** `# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.` — Comentario de documentacion que describe el proposito del siguiente bloque.
- **L002** `"""Funciones auxiliares de validacion, duracion y URLs."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L003** `import re` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L004** `import unicodedata` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L005** `from datetime import datetime` — Importa funciones, clases o tipos reutilizados por este modulo.
- **L006** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L007** `def validar_correo(correo: str) -> bool:` — Declara una funcion con parametros y comportamiento reutilizable.
- **L008** `"""Comprobar estructura basica de una direccion de email."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L009** `return bool(re.fullmatch(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', correo))` — Devuelve un resultado al llamador, la vista o el servicio.
- **L010** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L011** `def formatear_duracion(segundos: int) -> str:` — Declara una funcion con parametros y comportamiento reutilizable.
- **L012** `"""Convertir segundos no negativos a minutos:segundos."""` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L013** `if segundos < 0:` — Control de flujo: selecciona o recorre casos segun una condicion.
- **L014** `raise ValueError('La duracion no puede ser negativa')` — Produce un error explicito para informar una situacion no valida.
- **L015** `return f'{segundos // 60:02}:{segundos % 60:02}'` — Devuelve un resultado al llamador, la vista o el servicio.
- **L016** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L017** `def generar_slug(texto: str) -> str:` — Declara una funcion con parametros y comportamiento reutilizable.
- **L018** `"""Normalizar texto UTF-8 a una ruta legible."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L019** `sin_tildes = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L020** `slug = re.sub(r'[^a-z0-9]+', '-', sin_tildes.lower())` — Asigna, configura o define un valor utilizado por el resto del bloque.
- **L021** `return slug.strip('-')` — Devuelve un resultado al llamador, la vista o el servicio.
- **L022** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L023** `def obtener_anio_actual() -> int:` — Declara una funcion con parametros y comportamiento reutilizable.
- **L024** `"""Consultar el anio actual sin usar valores fijos."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L025** `return datetime.now().year` — Devuelve un resultado al llamador, la vista o el servicio.
- **L026** `[linea vacia]` — Linea en blanco que separa bloques para mejorar la lectura.
- **L027** `def validar_anio(anio: int) -> bool:` — Declara una funcion con parametros y comportamiento reutilizable.
- **L028** `"""Revisar rangos temporales razonables para lanzamientos."""` — Instruccion que continua la operacion del bloque; relacionarla con las lineas vecinas.
- **L029** `return 1970 <= anio <= obtener_anio_actual() + 3` — Devuelve un resultado al llamador, la vista o el servicio.
