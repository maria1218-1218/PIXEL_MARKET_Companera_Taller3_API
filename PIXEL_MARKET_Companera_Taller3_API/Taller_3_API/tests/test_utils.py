# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.
"""Pruebas de funciones auxiliares de la plantilla original."""
import pytest
from utils import validar_correo, formatear_duracion, generar_slug, obtener_anio_actual, validar_anio

def test_correos():
    assert validar_correo('persona@correo.com')
    assert not validar_correo('correo-invalido')

def test_duracion():
    assert formatear_duracion(125) == '02:05'
    with pytest.raises(ValueError):
        formatear_duracion(-1)

def test_slug():
    assert generar_slug('Edicion Epica: Accion!') == 'edicion-epica-accion'

def test_anio():
    assert validar_anio(2020)
    assert not validar_anio(1800)
    assert obtener_anio_actual() >= 2026
