
def validar_preferencia(datos):

    if not isinstance(datos, dict):
        return "Se debe enviar un JSON válido"

    tipo_preferencia = datos.get("tipo_preferencia")

    if tipo_preferencia not in ("like", "dislike"):
        return "La preferencia debe ser like o dislike"

    return None


def validar_nueva_preferencia(datos):

    error = validar_preferencia(datos)

    if error:
        return error

    id_cancion_spotify = datos.get("id_cancion_spotify")

    if not isinstance(id_cancion_spotify, str) or not id_cancion_spotify.strip():
        return "El identificador de la canción es obligatorio"

    return None
