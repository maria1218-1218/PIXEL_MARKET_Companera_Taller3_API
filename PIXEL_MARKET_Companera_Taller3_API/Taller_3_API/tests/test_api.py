# ARCHIVO DIDACTICO: revisar GUIA_COMENTARIOS_LINEA_A_LINEA.md para explicar cada instruccion.
"""Pruebas CRUD, validaciones, errores y flujo integrado de tienda."""
class TestEstado:
    def test_documentacion(self, client):
        assert client.get('/openapi.json').status_code == 200
    def test_info(self, client):
        assert '/api/juegos' in client.get('/api').json()['recursos']
    def test_portada(self, client):
        assert client.get('/').status_code == 200

class TestUsuarios:
    def test_lista_inicial(self, client):
        assert client.get('/api/usuarios').json() == []
    def test_crear_y_consultar(self, client, usuario):
        assert client.get(f"/api/usuarios/{usuario['id']}").json()['correo'] == 'cliente@example.com'
    def test_correo_duplicado(self, client, usuario):
        r = client.post('/api/usuarios', json={'nombre': 'Otro Cliente', 'correo': usuario['correo']})
        assert r.status_code == 409
    def test_correo_invalido(self, client):
        assert client.post('/api/usuarios', json={'nombre': 'Prueba', 'correo': 'incorrecto'}).status_code == 422
    def test_nombre_corto(self, client):
        assert client.post('/api/usuarios', json={'nombre': 'A', 'correo': 'a@demo.com'}).status_code == 422
    def test_actualizar(self, client, usuario):
        r = client.put(f"/api/usuarios/{usuario['id']}", json={'nombre': 'Nuevo Nombre'})
        assert r.status_code == 200 and r.json()['nombre'] == 'Nuevo Nombre'
    def test_eliminar(self, client, usuario):
        assert client.delete(f"/api/usuarios/{usuario['id']}").status_code == 204
        assert client.get(f"/api/usuarios/{usuario['id']}").status_code == 404
    def test_no_encontrado(self, client):
        assert client.get('/api/usuarios/999').status_code == 404
    def test_paginacion(self, client, usuario):
        assert len(client.get('/api/usuarios?limit=1&offset=0').json()) == 1
        assert client.get('/api/usuarios?limit=1&offset=1').json() == []
    def test_paginacion_invalida(self, client):
        assert client.get('/api/usuarios?limit=1000').status_code == 422

class TestJuegos:
    def test_lista_vacia(self, client):
        assert client.get('/api/juegos').json() == []
    def test_crear_y_consultar(self, client, juego):
        assert client.get(f"/api/juegos/{juego['id']}").json()['titulo'] == 'Reinos de Neon'
    def test_precio_negativo(self, client, juego):
        datos = {**juego, 'precio': -3}
        assert client.post('/api/juegos', json=datos).status_code == 422
    def test_anio_invalido(self, client, juego):
        datos = {**juego, 'anio_lanzamiento': 2200}
        assert client.post('/api/juegos', json=datos).status_code == 422
    def test_campos_obligatorios(self, client):
        assert client.post('/api/juegos', json={'titulo': 'Sin Datos'}).status_code == 422
    def test_actualizar_precio(self, client, juego):
        r = client.put(f"/api/juegos/{juego['id']}", json={'precio': 30000})
        assert r.json()['precio'] == 30000
    def test_busqueda(self, client, juego):
        assert len(client.get('/api/juegos/buscar?titulo=neon&genero=rpg&plataforma=PC&precio_max=60000').json()) == 1
        assert client.get('/api/juegos/buscar?genero=Simulador').json() == []
    def test_paginacion(self, client, juego):
        assert client.get('/api/juegos?offset=1&limit=1').json() == []
    def test_inexistente(self, client):
        assert client.get('/api/juegos/999').status_code == 404
    def test_eliminar(self, client, juego):
        assert client.delete(f"/api/juegos/{juego['id']}").status_code == 204
        assert client.get(f"/api/juegos/{juego['id']}").status_code == 404

class TestFavoritos:
    def test_lista_vacia(self, client):
        assert client.get('/api/favoritos').json() == []
    def test_crear_y_consultar(self, client, usuario, juego):
        r = client.post('/api/favoritos', json={'id_usuario': usuario['id'], 'id_juego': juego['id']})
        assert r.status_code == 201
        assert client.get(f"/api/favoritos/{r.json()['id']}").status_code == 200
    def test_duplicado(self, client, usuario, juego):
        datos = {'id_usuario': usuario['id'], 'id_juego': juego['id']}
        assert client.post('/api/favoritos', json=datos).status_code == 201
        assert client.post('/api/favoritos', json=datos).status_code == 409
    def test_usuario_invalido(self, client, juego):
        assert client.post('/api/favoritos', json={'id_usuario': 999, 'id_juego': juego['id']}).status_code == 404
    def test_juego_invalido(self, client, usuario):
        assert client.post('/api/favoritos', json={'id_usuario': usuario['id'], 'id_juego': 999}).status_code == 404
    def test_favorito_inexistente(self, client):
        assert client.get('/api/favoritos/999').status_code == 404
    def test_borrar_favorito(self, client, usuario, juego):
        datos = {'id_usuario': usuario['id'], 'id_juego': juego['id']}
        fav = client.post('/api/favoritos', json=datos).json()
        assert client.delete(f"/api/favoritos/{fav['id']}").status_code == 204
    def test_desde_usuario(self, client, usuario, juego):
        ruta = f"/api/usuarios/{usuario['id']}/favoritos/{juego['id']}"
        assert client.post(ruta).status_code == 201
        assert len(client.get(f"/api/usuarios/{usuario['id']}/favoritos").json()) == 1
        assert client.delete(ruta).status_code == 204
    def test_cascada_logica_juego(self, client, usuario, juego):
        client.post('/api/favoritos', json={'id_usuario': usuario['id'], 'id_juego': juego['id']})
        client.delete(f"/api/juegos/{juego['id']}")
        assert client.get('/api/favoritos').json() == []
    def test_cascada_logica_usuario(self, client, usuario, juego):
        client.post('/api/favoritos', json={'id_usuario': usuario['id'], 'id_juego': juego['id']})
        client.delete(f"/api/usuarios/{usuario['id']}")
        assert client.get('/api/favoritos').json() == []

class TestIntegracion:
    def test_flujo_completo(self, client):
        usuario = client.post('/api/usuarios', json={'nombre':'Cliente Final', 'correo':'final@example.com'}).json()
        juego = client.post('/api/juegos', json={'titulo':'Galaxia Infinita', 'desarrollador':'Prueba Studio', 'plataforma':'Xbox', 'genero':'Accion', 'precio':90000, 'anio_lanzamiento':2025}).json()
        r = client.post('/api/favoritos', json={'id_usuario':usuario['id'], 'id_juego':juego['id']})
        assert r.status_code == 201
        assert len(client.get(f"/api/usuarios/{usuario['id']}/favoritos").json()) == 1
        assert client.get('/api/juegos/buscar?plataforma=Xbox').json()[0]['id'] == juego['id']
