from repository.preferences_repository import crear_preferencia, obtener_preferencias_usuario, obtener_preferencia, actualizar_preferencia, eliminar_preferencia

def registrar_preferencia(id_usuario, id_cancion_spotify, tipo_preferencia):

    return crear_preferencia (id_usuario, id_cancion_spotify, tipo_preferencia)



def listar_preferencias_usuario(id_usuario):
    return obtener_preferencias_usuario(id_usuario)


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
