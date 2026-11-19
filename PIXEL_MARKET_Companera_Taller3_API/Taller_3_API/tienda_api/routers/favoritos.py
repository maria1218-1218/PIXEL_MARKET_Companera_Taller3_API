# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.
"""Operaciones sobre la lista de deseos de los clientes."""
from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select
from tienda_api.database import get_session
from tienda_api.models import Favorito, FavoritoCreate, Usuario, Juego

router = APIRouter(prefix='/api/favoritos', tags=['Favoritos'])

@router.get('', response_model=list[Favorito])
def listar_favoritos(offset: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100), session: Session = Depends(get_session)):
    """Listado paginado de favoritos."""
    return session.exec(select(Favorito).offset(offset).limit(limit)).all()

@router.post('', response_model=Favorito, status_code=201)
def crear_favorito(payload: FavoritoCreate, session: Session = Depends(get_session)):
    """Asociar juego y usuario, evitando referencias invalidas y duplicados."""
    if not session.get(Usuario, payload.id_usuario):
        raise HTTPException(404, 'Usuario no encontrado')
    if not session.get(Juego, payload.id_juego):
        raise HTTPException(404, 'Juego no encontrado')
    anterior = session.exec(select(Favorito).where(Favorito.id_usuario == payload.id_usuario, Favorito.id_juego == payload.id_juego)).first()
    if anterior:
        raise HTTPException(409, 'El juego ya esta en favoritos')
    favorito = Favorito.model_validate(payload)
    session.add(favorito)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(409, 'El juego ya esta en favoritos')
    session.refresh(favorito)
    return favorito

@router.get('/{favorito_id}', response_model=Favorito)
def obtener_favorito(favorito_id: int, session: Session = Depends(get_session)):
    """Consultar una relacion de favoritos."""
    favorito = session.get(Favorito, favorito_id)
    if favorito is None:
        raise HTTPException(404, 'Favorito no encontrado')
    return favorito

@router.delete('/{favorito_id}', status_code=204)
def eliminar_favorito(favorito_id: int, session: Session = Depends(get_session)):
    """Eliminar un favorito existente."""
    favorito = obtener_favorito(favorito_id, session)
    session.delete(favorito)
    session.commit()
    return Response(status_code=204)
