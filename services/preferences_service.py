from repository.preferences_repository import crear_preferencia, obtener_preferencias_usuario, obtener_preferencia, actualizar_preferencia, eliminar_preferencia

from services.spotify_service import obtener_cancion_spotify

def completar_datos_cancion(preferencia):

    cancion = obtener_cancion_spotify(
        preferencia["id_cancion_spotify"]
    )

    preferencia["nombre_cancion"] = cancion["name"]

    preferencia["artistas"] = [
        artista["name"]
        for artista in cancion["artists"]
    ]

    return preferencia



def registrar_preferencia(id_usuario, id_cancion_spotify, tipo_preferencia):

    return crear_preferencia (id_usuario, id_cancion_spotify, tipo_preferencia)



def listar_preferencias_usuario(id_usuario):
    
    preferencias = obtener_preferencias_usuario(id_usuario)
    
    return [
        completar_datos_cancion(preferencia)
        for preferencia in preferencias
    ]


def modificar_preferencia(id_usuario, id_cancion_spotify, tipo_preferencia):

    preferencia = obtener_preferencia(id_usuario, id_cancion_spotify)

    if preferencia is None:
        return False

    actualizar_preferencia(
        id_usuario,
        id_cancion_spotify,
        tipo_preferencia
    )

    return True

def borrar_preferencia(id_usuario, id_cancion_spotify):
    return eliminar_preferencia(id_usuario, id_cancion_spotify)
