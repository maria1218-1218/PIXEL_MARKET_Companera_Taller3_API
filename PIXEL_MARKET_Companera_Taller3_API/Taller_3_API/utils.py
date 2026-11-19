# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.
"""Funciones auxiliares de validacion, duracion y URLs."""
import re
import unicodedata
from datetime import datetime

def validar_correo(correo: str) -> bool:
    """Comprobar estructura basica de una direccion de email."""
    return bool(re.fullmatch(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', correo))

def formatear_duracion(segundos: int) -> str:
    """Convertir segundos no negativos a minutos:segundos."""
    if segundos < 0:
        raise ValueError('La duracion no puede ser negativa')
    return f'{segundos // 60:02}:{segundos % 60:02}'

def generar_slug(texto: str) -> str:
    """Normalizar texto UTF-8 a una ruta legible."""
    sin_tildes = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    slug = re.sub(r'[^a-z0-9]+', '-', sin_tildes.lower())
    return slug.strip('-')

def obtener_anio_actual() -> int:
    """Consultar el anio actual sin usar valores fijos."""
    return datetime.now().year

def validar_anio(anio: int) -> bool:
    """Revisar rangos temporales razonables para lanzamientos."""
    return 1970 <= anio <= obtener_anio_actual() + 3
