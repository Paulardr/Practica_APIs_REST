from database.connection import obtener_conexion

def registrar_artista_favorito(id_usuario, id_artista_spotify):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        consulta = """INSERT INTO artistas_favoritos 
                        (id_usuario, id_artista_spotify)
                        VALUES (%s,%s) 
                        
                    """

        cursor.execute(consulta, (id_usuario, id_artista_spotify))

        conexion.commit()

        return cursor.lastrowid

    finally:

        cursor.close()
        conexion.close()

def obtener_artistas_favoritos_usuario(id_usuario):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        consulta = """SELECT * FROM artistas_favoritos WHERE id_usuario = %s"""

        cursor.execute(consulta, (id_usuario,))
        return cursor.fetchall()

    finally:
        cursor.close()
        conexion.close()


def eliminar_artista_favorito(id_usuario, id_artista_spotify):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        consulta = """DELETE FROM artistas_favoritos WHERE id_usuario = %s AND id_artista_spotify = %s"""

        cursor.execute(consulta, (id_usuario, id_artista_spotify))

        conexion.commit()
        return cursor.rowcount

    finally:
        cursor.close()
        conexion.close()
