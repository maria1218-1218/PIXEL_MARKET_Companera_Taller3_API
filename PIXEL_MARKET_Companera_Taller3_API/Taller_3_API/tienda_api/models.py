# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.
"""Modelos de persistencia y esquemas de entrada y salida de la API."""
from datetime import datetime, timezone
from typing import Optional
from pydantic import EmailStr, Field as PField, field_validator
from sqlmodel import SQLModel, Field, UniqueConstraint


def now_utc():
    """Generar sello de tiempo UTC sin dependencias externas."""
    return datetime.now(timezone.utc)

class UsuarioBase(SQLModel):
    """Propiedades publicas del usuario."""
    nombre: str = PField(min_length=2, max_length=90)
    correo: str = PField(min_length=5, max_length=255)

class Usuario(UsuarioBase, table=True):
    """Tabla de usuarios con correo unico."""
    id: Optional[int] = Field(default=None, primary_key=True)
    correo: str = Field(index=True, unique=True, max_length=255)
    fecha_registro: datetime = Field(default_factory=now_utc)

class UsuarioCreate(UsuarioBase):
    """Esquema para crear una cuenta con validacion real de email."""
    correo: EmailStr

class UsuarioUpdate(SQLModel):
    """Esquema para modificar datos de una cuenta."""
    nombre: Optional[str] = PField(default=None, min_length=2, max_length=90)
    correo: Optional[EmailStr] = None

class JuegoBase(SQLModel):
    """Informacion comercial de un videojuego digital."""
    titulo: str = PField(min_length=2, max_length=150)
    desarrollador: str = PField(min_length=2, max_length=120)
    plataforma: str = PField(min_length=2, max_length=40)
    genero: str = PField(min_length=2, max_length=80)
    precio: float = PField(ge=0, le=10000000)
    anio_lanzamiento: int = PField(ge=1970, le=2100)
    descripcion: str = PField(default="", max_length=1000)
    disponible: bool = True

    @field_validator('anio_lanzamiento')
    @classmethod
    def validar_anio(cls, value):
        """Evitar juegos con un anio de lanzamiento irrealmente futuro."""
        if value > now_utc().year + 3:
            raise ValueError('Anio de lanzamiento demasiado lejano')
        return value

class Juego(JuegoBase, table=True):
    """Tabla de juegos del catalogo."""
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha_creacion: datetime = Field(default_factory=now_utc)

class JuegoCreate(JuegoBase):
    """Datos validados al crear un juego."""

class JuegoUpdate(SQLModel):
    """Datos opcionales al actualizar un juego."""
    titulo: Optional[str] = PField(default=None, min_length=2, max_length=150)
    desarrollador: Optional[str] = PField(default=None, min_length=2, max_length=120)
    plataforma: Optional[str] = PField(default=None, min_length=2, max_length=40)
    genero: Optional[str] = PField(default=None, min_length=2, max_length=80)
    precio: Optional[float] = PField(default=None, ge=0, le=10000000)
    anio_lanzamiento: Optional[int] = PField(default=None, ge=1970, le=2100)
    descripcion: Optional[str] = PField(default=None, max_length=1000)
    disponible: Optional[bool] = None

    @field_validator('anio_lanzamiento')
    @classmethod
    def validar_anio(cls, value):
        if value is not None and value > now_utc().year + 3:
            raise ValueError('Anio de lanzamiento demasiado lejano')
        return value

class Favorito(SQLModel, table=True):
    """Relacion entre un usuario y un juego marcado como favorito."""
    __table_args__ = (UniqueConstraint('id_usuario', 'id_juego', name='uq_usuario_juego'),)
    id: Optional[int] = Field(default=None, primary_key=True)
    id_usuario: int = Field(foreign_key='usuario.id')
    id_juego: int = Field(foreign_key='juego.id')
    fecha_marcado: datetime = Field(default_factory=now_utc)

class FavoritoCreate(SQLModel):
    """Identificadores para registrar un favorito."""
    id_usuario: int = PField(gt=0)
    id_juego: int = PField(gt=0)
