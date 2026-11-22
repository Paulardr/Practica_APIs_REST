from database.connection import obtener_conexion

def obtener_estadisticas_usuario(id_usuario):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try: 

        consulta = """SELECT
                    (SELECT COUNT(*) FROM preferencias_canciones WHERE id_usuario = %s AND tipo_preferencia = 'like') AS total_likes,
                    (SELECT COUNT(*) FROM preferencias_canciones WHERE id_usuario = %s AND tipo_preferencia = 'dislike') AS total_dislikes,
                    (SELECT COUNT(*) FROM artistas_favoritos WHERE id_usuario = %s) AS total_artistas_favoritos,
                    (SELECT COUNT(*) FROM playlists WHERE id_usuario = %s) AS total_playlists
                    """

        cursor.execute(
            # se pone cuatro veces id_usuario debido a que cada subconsulta tiene un marcador
            consulta, (id_usuario, id_usuario, id_usuario, id_usuario))

        return cursor.fetchone()

    finally:
        cursor.close()
        conexion.close()
