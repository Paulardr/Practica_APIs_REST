from repository.favorite_artists_repository import registrar_artista_favorito, obtener_artistas_favoritos_usuario, eliminar_artista_favorito
from services.spotify_service import obtener_artista_spotify

def completar_datos_artista(artista_favorito):

    artista = obtener_artista_spotify(
        artista_favorito["id_artista_spotify"]
    )

    artista_favorito["nombre_artista"] = artista["name"]

    return artista_favorito

def agregar_artista_favorito(id_usuario, id_artista_spotify):

    obtener_artista_spotify(id_artista_spotify)

    return registrar_artista_favorito(
        id_usuario,
        id_artista_spotify
    )


def listar_artistas_favoritos(id_usuario):

    artistas = obtener_artistas_favoritos_usuario(id_usuario)

    return [
        completar_datos_artista(artista)
        for artista in artistas
    ]


def borrar_artista_favorito(id_usuario, id_artista_spotify):

    return eliminar_artista_favorito(
        id_usuario,
        id_artista_spotify
    )
