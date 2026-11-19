# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.
"""CRUD de cuentas de usuario y favoritos asociados."""
from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select
from tienda_api.database import get_session
from tienda_api.models import Usuario, UsuarioCreate, UsuarioUpdate, Favorito

router = APIRouter(prefix='/api/usuarios', tags=['Usuarios'])

@router.get('', response_model=list[Usuario])
def listar_usuarios(offset: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100), session: Session = Depends(get_session)):
    """Listado paginado de usuarios."""
    return session.exec(select(Usuario).offset(offset).limit(limit)).all()

@router.post('', response_model=Usuario, status_code=201)
def crear_usuario(payload: UsuarioCreate, session: Session = Depends(get_session)):
    """Crear usuario con correo unico."""
    usuario = Usuario.model_validate(payload)
    usuario.correo = str(usuario.correo).lower()
    session.add(usuario)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(409, 'El correo ya esta registrado')
    session.refresh(usuario)
    return usuario

@router.get('/{usuario_id}', response_model=Usuario)
def obtener_usuario(usuario_id: int, session: Session = Depends(get_session)):
    """Recuperar un usuario por ID."""
    usuario = session.get(Usuario, usuario_id)
    if usuario is None:
        raise HTTPException(404, 'Usuario no encontrado')
    return usuario

@router.put('/{usuario_id}', response_model=Usuario)
def actualizar_usuario(usuario_id: int, payload: UsuarioUpdate, session: Session = Depends(get_session)):
    """Modificar los campos proporcionados de un usuario."""
    usuario = obtener_usuario(usuario_id, session)
    datos = payload.model_dump(exclude_unset=True)
    if 'correo' in datos and datos['correo'] is not None:
        datos['correo'] = str(datos['correo']).lower()
    usuario.sqlmodel_update(datos)
    session.add(usuario)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(409, 'El correo ya esta registrado')
    session.refresh(usuario)
    return usuario

@router.delete('/{usuario_id}', status_code=204)
def eliminar_usuario(usuario_id: int, session: Session = Depends(get_session)):
    """Borrar favoritos del usuario antes de eliminar su cuenta."""
    usuario = obtener_usuario(usuario_id, session)
    for fav in session.exec(select(Favorito).where(Favorito.id_usuario == usuario_id)).all():
        session.delete(fav)
    session.delete(usuario)
    session.commit()
    return Response(status_code=204)

@router.get('/{usuario_id}/favoritos', response_model=list[Favorito])
def favoritos_usuario(usuario_id: int, session: Session = Depends(get_session)):
    """Listar favoritos de una cuenta existente."""
    obtener_usuario(usuario_id, session)
    return session.exec(select(Favorito).where(Favorito.id_usuario == usuario_id)).all()

@router.post('/{usuario_id}/favoritos/{juego_id}', response_model=Favorito, status_code=201)
def marcar_favorito(usuario_id: int, juego_id: int, session: Session = Depends(get_session)):
    """Marcar un juego como favorito."""
    from tienda_api.routers.favoritos import crear_favorito
    from tienda_api.models import FavoritoCreate
    return crear_favorito(FavoritoCreate(id_usuario=usuario_id, id_juego=juego_id), session)

@router.delete('/{usuario_id}/favoritos/{juego_id}', status_code=204)
def quitar_favorito(usuario_id: int, juego_id: int, session: Session = Depends(get_session)):
    """Quitar un juego de favoritos de un usuario."""
    favorito = session.exec(select(Favorito).where(Favorito.id_usuario == usuario_id, Favorito.id_juego == juego_id)).first()
    if favorito is None:
        raise HTTPException(404, 'Favorito no encontrado')
    session.delete(favorito)
    session.commit()
    return Response(status_code=204)
