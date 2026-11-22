
from database.connection import obtener_conexion


def crear_playlist(id_usuario, nombre, descripcion):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        consulta = """
            INSERT INTO playlists
            (id_usuario, nombre, descripcion)
            VALUES (%s, %s, %s)
        """

        cursor.execute(
            consulta,
            (id_usuario, nombre, descripcion)
        )

        conexion.commit()

        return cursor.lastrowid

    finally:
        cursor.close()
        conexion.close()


def obtener_playlists_usuario(id_usuario):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        consulta = """
            SELECT * FROM playlists WHERE id_usuario = %s
        """

        cursor.execute(consulta, (id_usuario,))

        return cursor.fetchall()

    finally:
        cursor.close()
        conexion.close()


def obtener_playlist(id_usuario, id_playlist):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        consulta = """
            SELECT * FROM playlists WHERE id_usuario = %s AND id_playlist = %s
        """

        cursor.execute(
            consulta,
            (id_usuario, id_playlist)
        )

        return cursor.fetchone()

    finally:
        cursor.close()
        conexion.close()


def actualizar_playlist(id_usuario, id_playlist, nombre, descripcion):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        consulta = """
            UPDATE playlists
            SET nombre = %s, descripcion = %s
            WHERE id_usuario = %s AND id_playlist = %s
        """

        valores = (
            nombre,
            descripcion,
            id_usuario,
            id_playlist
        )

        cursor.execute(consulta, valores)

        conexion.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexion.close()



def eliminar_playlist(id_usuario, id_playlist):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        consulta = """
            DELETE FROM playlists WHERE id_usuario = %s AND id_playlist = %s
        """

        cursor.execute(
            consulta,
            (id_usuario, id_playlist)
        )

        conexion.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexion.close()

def agregar_cancion_playlist (id_playlist, id_cancion_spotify):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        consulta = """INSERT INTO playlist_canciones
                        (id_playlist, id_cancion_spotify)
                        VALUES (%s, %s)"""

        cursor.execute(consulta, (id_playlist, id_cancion_spotify))

        conexion.commit()

        return cursor.lastrowid

    finally:
        cursor.close()
        conexion.close()

def obtener_canciones_playlist(id_playlist):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        consulta = """ SELECT * FROM playlist_canciones WHERE id_playlist = %s """

        cursor.execute(consulta, (id_playlist,))

        return cursor.fetchall()

    finally:
        cursor.close()
        conexion.close()


def eliminar_cancion_playlist(id_playlist, id_cancion_spotify):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        consulta = """ DELETE FROM playlist_canciones WHERE id_playlist = %s AND id_cancion_spotify = %s """

        cursor.execute(
            consulta,
            (id_playlist, id_cancion_spotify)
        )

        conexion.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexion.close()
