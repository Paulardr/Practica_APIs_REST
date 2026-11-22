from repository.favorite_artists_repository import registrar_artista_favorito, obtener_artistas_favoritos_usuario, eliminar_artista_favorito
from services.spotify_service import obtener_artista_spotify

def agregar_artista_favorito(id_usuario, id_artista_spotify):

    obtener_artista_spotify(id_artista_spotify)

    return registrar_artista_favorito(
        id_usuario,
        id_artista_spotify
    )


def listar_artistas_favoritos(id_usuario):

    return obtener_artistas_favoritos_usuario(id_usuario)


def borrar_artista_favorito(id_usuario, id_artista_spotify):

    return eliminar_artista_favorito(
        id_usuario,
        id_artista_spotify
    )
