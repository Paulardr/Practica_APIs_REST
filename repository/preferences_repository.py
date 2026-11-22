from database.connection import obtener_conexion

def crear_preferencia(id_usuario, id_cancion_spotify, tipo_preferencia):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:

        consulta = """INSERT INTO preferencias_canciones
                        (id_usuario, id_cancion_spotify, tipo_preferencia)
                        VALUES (%s,%s,%s)
                    """

        cursor.execute(consulta, (id_usuario, id_cancion_spotify, tipo_preferencia))

        conexion.commit()

        return cursor.lastrowid

    finally:

        cursor.close()
        conexion.close()


def obtener_preferencias_usuario(id_usuario):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        consulta = """
            SELECT * FROM preferencias_canciones WHERE id_usuario = %s
        """

        cursor.execute(consulta, (id_usuario,))

        return cursor.fetchall()

    finally:
        cursor.close()
        conexion.close()


def obtener_preferencia(id_usuario, id_cancion_spotify):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    try:
        consulta = """
            SELECT *
            FROM preferencias_canciones
            WHERE id_usuario = %s
            AND id_cancion_spotify = %s
        """

        cursor.execute(
            consulta,
            (id_usuario, id_cancion_spotify)
        )

        return cursor.fetchone()

    finally:
        cursor.close()
        conexion.close()



def actualizar_preferencia(id_usuario, id_cancion_spotify, tipo_preferencia):

    conexion = obtener_conexion()
    cursor = None

    try: 
        cursor = conexion.cursor()

        consulta =  """
            UPDATE preferencias_canciones
            SET tipo_preferencia = %s
            WHERE id_usuario = %s AND id_cancion_spotify = %s
        """

        valores = (tipo_preferencia, id_usuario, id_cancion_spotify)

        cursor.execute(consulta, valores)
        conexion.commit()

        return cursor.rowcount

    finally: 

        if cursor is not None:
            cursor.close()
        conexion.close()


def eliminar_preferencia(id_usuario, id_cancion_spotify):

    conexion = obtener_conexion()
    cursor = None

    try:
        cursor = conexion.cursor()

        consulta = """DELETE FROM preferencias_canciones WHERE id_usuario = %s AND id_cancion_spotify = %s"""

        cursor.execute(consulta, (id_usuario, id_cancion_spotify))
        conexion.commit()

        return cursor.rowcount

    finally: 

        if cursor is not None:
            cursor.close()
        conexion.close()