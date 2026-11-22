from repository.statistics_repository import obtener_estadisticas_usuario
from repository.user_repository import obtener_usuario_id


def consultar_estadisticas_usuario(id_usuario):

    usuario = obtener_usuario_id(id_usuario)

    if usuario is None:
        return None

    estadisticas = obtener_estadisticas_usuario(id_usuario)

    return {
        "id_usuario": id_usuario,
        "estadisticas": estadisticas
    }