# PIXEL MARKET | Version academica comentada

Consulta `GUIA_COMENTARIOS_LINEA_A_LINEA.md` y `../GUION_EXPOSICION.md` para preparar la exposicion.

# PIXEL MARKET | LPA2 Taller 3

> API RESTful para una tienda academica de videojuegos digitales, inspirada en el funcionamiento general de catalogos como Steam y Xbox, sin usar marcas ni contenidos comerciales como si fueran propios.

## Descripcion

Proyecto construido sobre la plantilla del docente **LPA2 Taller 3**. La plantilla original describe usuarios, canciones y favoritos, pero esta adaptacion convierte las canciones en **juegos digitales**: usuarios, juegos y favoritos (lista de deseos). La venta con pagos, licencias y transacciones reales **no** esta implementada; este taller desarrolla la base de datos y la API del catalogo. El frontend completo se desarrollara en el **Taller 4**.

**Tecnologias:** Python, FastAPI, SQLModel, Pydantic, SQLite, pytest, Ruff, pre-commit, GitHub Actions, Docker y Docker Compose. La portada de la API utiliza CSS propio y Bootstrap 5 por CDN.

## Requisitos del docente: seguimiento

| Requisito | Solucion incluida | Accion del estudiante |
| --- | --- | --- |
| README con datos del estudiante | Documento editable | Agregar nombre, curso y repositorio |
| 5 usuarios y 10 registros directos con DBeaver | `sql/datos_dbeaver.sql` | Ejecutar el SQL con DBeaver y guardar captura |
| Pre-commit, Ruff y workflow pytest | `.pre-commit-config.yaml`, `pyproject.toml`, `.github/workflows/quality.yml` | Activar pre-commit y publicar en GitHub |
| Resolver TODO y FIXME | Modelos, rutas, validaciones y funciones construidas | Realizar commits individuales, no se pueden inventar commits |
| Verificar Swagger o ReDoc | `/docs` y `/redoc` | Ejecutar endpoints y capturar resultados |
| Pruebas automatizadas | `tests/test_api.py`, `tests/test_utils.py` | Instalar dependencias y ejecutar `pytest -v` |
| Implementar dos mejoras | **Paginacion** y **Docker** | Mostrar pruebas y contenedor operativo |

## Preparacion en Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn main:app --reload
```

Si PowerShell impide activar el entorno, desde la carpeta raiz usa directamente `.venv\Scripts\python.exe -m pip install -r requirements.txt` y `.venv\Scripts\python.exe -m uvicorn main:app --reload`.

## Preparacion en Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
```

La API crea automaticamente `videojuegos.db` cuando inicia.

## Direcciones importantes

- `http://localhost:8000/` - Portada oscura PIXEL MARKET con Bootstrap y CSS.
- `http://localhost:8000/docs` - Swagger UI interactivo.
- `http://localhost:8000/redoc` - ReDoc.
- `http://localhost:8000/api` - Resumen JSON de recursos.
- `http://localhost:8000/health` - Verificacion de base de datos.
- `http://localhost:8000/openapi.json` - Contrato OpenAPI para el frontend del Taller 4.

## Estructura principal

```text
lpa2_taller3_videojuegos/
  main.py
  utils.py
  tienda_api/
    config.py
    database.py
    models.py
    routers/
      usuarios.py
      juegos.py
      favoritos.py
  static/
    index.html
    styles.css
  sql/
    datos_dbeaver.sql
  tests/
    conftest.py
    test_api.py
    test_utils.py
  .github/workflows/quality.yml
  .pre-commit-config.yaml
  Dockerfile
  compose.yaml
  requirements.txt
  pyproject.toml
```

## Endpoints REST

| Metodo | Ruta | Funcion |
| --- | --- | --- |
| GET, POST | `/api/usuarios` | Listar (paginado) y crear usuarios |
| GET, PUT, DELETE | `/api/usuarios/{id}` | Consultar, actualizar y eliminar usuario |
| GET, POST | `/api/juegos` | Listar (paginado) y crear juegos |
| GET | `/api/juegos/buscar` | Buscar por `titulo`, `genero`, `plataforma`, `precio_max` |
| GET, PUT, DELETE | `/api/juegos/{id}` | Consultar, actualizar y eliminar juego |
| GET, POST | `/api/favoritos` | Listar (paginado) y marcar favoritos |
| GET, DELETE | `/api/favoritos/{id}` | Consultar o eliminar favorito |
| GET | `/api/usuarios/{id}/favoritos` | Listar favoritos de un usuario |
| POST, DELETE | `/api/usuarios/{id}/favoritos/{juego_id}` | Marcar y desmarcar favorito |

### Ejemplo para crear un usuario

```json
{"nombre":"Cliente Demo","correo":"cliente@example.com"}
```

### Ejemplo para crear un juego

```json
{
  "titulo": "Nebula Rift",
  "desarrollador": "Pixel Forge",
  "plataforma": "PC",
  "genero": "RPG",
  "precio": 89000,
  "anio_lanzamiento": 2025,
  "descripcion": "Aventura espacial",
  "disponible": true
}
```

### Ejemplo de favorito

```json
{"id_usuario":1,"id_juego":1}
```

## Uso con DBeaver

1. Iniciar la API para crear la base `videojuegos.db` y detenerla antes de ejecutar SQL.
2. Abrir DBeaver, crear conexion de tipo **SQLite** y elegir la ruta absoluta a `videojuegos.db`.
3. Verificar las tablas `usuario`, `juego` y `favorito`.
4. Ejecutar **una sola vez** el contenido de `sql/datos_dbeaver.sql` en una base sin datos.
5. Consultar `SELECT * FROM usuario;` y `SELECT * FROM juego;`.
6. Guardar capturas de los 5 usuarios y 10 juegos insertados con DBeaver.

**Nota:** El SQL es una alternativa reproducible para cumplir el trabajo de carga directa desde DBeaver; la insercion y captura deben efectuarse en tu computador.

## Dos mejoras opcionales implementadas

**Mejora 1: paginacion.** Las listas de usuarios, juegos y favoritos aceptan `offset` (desde 0) y `limit` (de 1 a 100; por defecto 20). Ejemplo: `/api/juegos?offset=0&limit=5`.

**Mejora 2: Docker.** La API se empaqueta en un contenedor y persiste SQLite en un volumen. Para iniciarla:

```bash
docker compose up --build
```

La portada estara en `http://localhost:8000/`. Para detener: `docker compose down`. No es necesario Docker para la ejecucion local.

## Pruebas y calidad

```bash
pytest -v
ruff format .
ruff check .
pre-commit install
pre-commit run --all-files
```

GitHub Actions ejecuta instalacion, Ruff y pytest en cada push o pull request. Las pruebas usan una base SQLite en memoria, sin modificar datos de la base de desarrollo.

## Commits sugeridos para el punto TODO/FIXME

El historial de commits debe reflejar trabajo real en Git; un ZIP no incluye un historial autentico. Se sugiere dividir las confirmaciones en cambios progresivos:

1. `feat: modelos y validaciones Pydantic de videojuegos`
2. `feat: conexion SQLModel y CRUD de usuarios`
3. `feat: CRUD de juegos y busqueda`
4. `feat: favoritos y restricciones de duplicados`
5. `test: pruebas unitarias y flujo integrado`
6. `ci: ruff precommit y github actions`
7. `feat: paginacion y despliegue docker`
8. `style: portada Bootstrap y CSS oscuro`

## Preparacion para Taller 4

El frontend de React/TypeScript consumira `http://localhost:8000/api/usuarios`, `/api/juegos` y `/api/favoritos`. En la configuracion CORS estan habilitados `http://localhost:3000` y `http://127.0.0.1:3000`. En Swagger `/openapi.json` se documentan esquemas y rutas para construir el prompt de v0 indicado por el profesor. No se implementan pagos reales ni autenticacion; para una tienda comercial haria falta agregar controles de seguridad.

## Identificacion del estudiante

- Estudiante: **[Completar]**
- Curso: **Lenguaje de Programacion Avanzada II**
- Taller: **3 - API RESTful con FastAPI, SQLModel y Pydantic**
- Repositorio de GitHub: **[Completar]**

## Estado de validacion

La compilacion de sintaxis Python y las pruebas de utilidades se pueden ejecutar sin SQLModel. Para comprobar realmente la API, hay que instalar todas las dependencias de `requirements.txt` y ejecutar la suite `pytest -v`, seguida de pruebas en Swagger y DBeaver. No afirmar pruebas API aprobadas hasta realizar esa validacion en un entorno con SQLModel.
