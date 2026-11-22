from repository.playlists_repository import (crear_playlist, obtener_playlists_usuario, obtener_playlist, actualizar_playlist, eliminar_playlist, agregar_cancion_playlist, obtener_canciones_playlist, eliminar_cancion_playlist)

from services.spotify_service import obtener_cancion_spotify

from repository.playlists_repository import (
    crear_playlist,
    obtener_playlists_usuario,
    obtener_playlist,
    actualizar_playlist,
    eliminar_playlist
)


def registrar_playlist(id_usuario, nombre, descripcion):

    return crear_playlist(id_usuario, nombre, descripcion)


def listar_playlists_usuario(id_usuario):

    return obtener_playlists_usuario(id_usuario)


def consultar_playlist(id_usuario, id_playlist):

    return obtener_playlist(id_usuario, id_playlist)


def modificar_playlist(id_usuario, id_playlist, nombre, descripcion):

    playlist = obtener_playlist(id_usuario, id_playlist)

    if playlist is None:
        return False

    actualizar_playlist(
        id_usuario,
        id_playlist,
        nombre,
        descripcion
    )

    return True


def borrar_playlist(id_usuario, id_playlist):

    return eliminar_playlist(id_usuario, id_playlist)





def registrar_cancion_playlist(id_usuario, id_playlist, id_cancion_spotify):

    playlist = obtener_playlist(id_usuario, id_playlist)

    if playlist is None:
        return None

    cancion = obtener_cancion_spotify(id_cancion_spotify)

    id_playlist_cancion = agregar_cancion_playlist(
        id_playlist,
        id_cancion_spotify
    )

    return {
        "id_playlist_cancion": id_playlist_cancion,
        "id_playlist": id_playlist,
        "id_cancion_spotify": id_cancion_spotify,
        "nombre": cancion["name"],
        "artistas": [
            artista["name"]
            for artista in cancion["artists"]
        ]
    }



def listar_canciones_playlist(id_usuario, id_playlist):

    playlist = obtener_playlist(id_usuario, id_playlist)

    if playlist is None:
        return None

    canciones = obtener_canciones_playlist(id_playlist)

    resultado = []

    for registro in canciones:

        id_cancion_spotify = registro["id_cancion_spotify"]

        cancion = obtener_cancion_spotify(id_cancion_spotify)

        resultado.append({
            "id_playlist_cancion": registro["id_playlist_cancion"],
            "id_cancion_spotify": id_cancion_spotify,
            "nombre": cancion["name"],
            "artistas": [
                artista["name"]
                for artista in cancion["artists"]
            ],
            "fecha_agregado": registro["fecha_agregado"]
        })

    return resultado



def borrar_cancion_playlist(id_usuario, id_playlist, id_cancion_spotify):

    playlist = obtener_playlist(id_usuario, id_playlist)

    if playlist is None:
        return None

    return eliminar_cancion_playlist(
        id_playlist,
        id_cancion_spotify
    )
