# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.
"""CRUD y busqueda de juegos digitales."""
from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlmodel import Session, select
from tienda_api.database import get_session
from tienda_api.models import Juego, JuegoCreate, JuegoUpdate, Favorito

router = APIRouter(prefix='/api/juegos', tags=['Juegos'])

@router.get('', response_model=list[Juego])
def listar_juegos(offset: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100), session: Session = Depends(get_session)):
    """Catalogo paginado de juegos."""
    return session.exec(select(Juego).offset(offset).limit(limit)).all()

@router.get('/buscar', response_model=list[Juego])
def buscar_juegos(titulo: str | None = None, genero: str | None = None, plataforma: str | None = None, precio_max: float | None = Query(None, ge=0), offset: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100), session: Session = Depends(get_session)):
    """Filtrar catalogo por titulo, genero, plataforma y precio."""
    consulta = select(Juego)
    if titulo:
        consulta = consulta.where(Juego.titulo.ilike(f'%{titulo}%'))
    if genero:
        consulta = consulta.where(Juego.genero.ilike(f'%{genero}%'))
    if plataforma:
        consulta = consulta.where(Juego.plataforma.ilike(f'%{plataforma}%'))
    if precio_max is not None:
        consulta = consulta.where(Juego.precio <= precio_max)
    return session.exec(consulta.offset(offset).limit(limit)).all()

@router.post('', response_model=Juego, status_code=201)
def crear_juego(payload: JuegoCreate, session: Session = Depends(get_session)):
    """Registrar videojuego con datos validados por Pydantic."""
    juego = Juego.model_validate(payload)
    session.add(juego)
    session.commit()
    session.refresh(juego)
    return juego

@router.get('/{juego_id}', response_model=Juego)
def obtener_juego(juego_id: int, session: Session = Depends(get_session)):
    """Consultar un juego por ID."""
    juego = session.get(Juego, juego_id)
    if juego is None:
        raise HTTPException(404, 'Juego no encontrado')
    return juego

@router.put('/{juego_id}', response_model=Juego)
def actualizar_juego(juego_id: int, payload: JuegoUpdate, session: Session = Depends(get_session)):
    """Actualizar uno o mas campos del juego."""
    juego = obtener_juego(juego_id, session)
    juego.sqlmodel_update(payload.model_dump(exclude_unset=True))
    session.add(juego)
    session.commit()
    session.refresh(juego)
    return juego

@router.delete('/{juego_id}', status_code=204)
def eliminar_juego(juego_id: int, session: Session = Depends(get_session)):
    """Borrar favoritos asociados y despues el juego."""
    juego = obtener_juego(juego_id, session)
    for favorito in session.exec(select(Favorito).where(Favorito.id_juego == juego_id)).all():
        session.delete(favorito)
    session.delete(juego)
    session.commit()
    return Response(status_code=204)
