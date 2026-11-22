
def validar_artista_favorito(datos):

    if not isinstance(datos, dict):
        return "Se debe enviar un JSON válido"

    id_artista_spotify = datos.get("id_artista_spotify")

    if not isinstance(id_artista_spotify, str) or not id_artista_spotify.strip():
        return "El identificador del artista es obligatorio"

    return None
