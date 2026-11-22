
def validar_playlist(datos):

    if not isinstance(datos, dict):
        return "Se debe enviar un JSON valido"

    nombre = datos.get("nombre")
    descripcion = datos.get("descripcion")

    if not isinstance(nombre, str) or not nombre.strip():
        return "El nombre de la playlist es obligatorio"

    if len(nombre) > 150:
        return "El nombre no puede superar los 150 caracteres"

    if descripcion is not None:
        if not isinstance(descripcion, str):
            return "La descripción debe ser un texto"

        if len(descripcion) > 255:
            return "La descripción no puede superar los 255 caracteres"

    return None



def validar_cancion_playlist(datos):

    if not isinstance(datos, dict):
        return "Se debe enviar un JSON válido"

    id_cancion_spotify = datos.get("id_cancion_spotify")

    if not isinstance(id_cancion_spotify, str) or not id_cancion_spotify.strip():
        return "El identificador de la canción es obligatorio"

    if len(id_cancion_spotify) > 100:
        return "El identificador de la canción no puede superar los 100 caracteres"

    return None
