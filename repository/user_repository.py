from database.connection import obtener_conexion

def crear_usuario(nombre, apellidos, email):

    conexion = obtener_conexion()
    cursor =  None

    try: 
        cursor = conexion.cursor()

        consulta = """
            INSERT INTO usuarios (nombre, apellidos, email)
            VALUES (%s, %s, %s)
            """

        valores = (nombre, apellidos, email)

        cursor.execute(consulta, valores)
        conexion.commit()

        return cursor.lastrowid

    finally:
        if cursor is not None:
            cursor.close()
        conexion.close()


def obtener_usuarios():

    conexion = obtener_conexion()
    cursor = None

    try:
        cursor = conexion.cursor(dictionary=True)

        consulta = """ SELECT * FROM usuarios"""

        cursor.execute(consulta)
        usuarios = cursor.fetchall()

        return usuarios

    finally:
        if cursor is not None:
            cursor.close()
        conexion.close()

def obtener_usuario_id(id_usuario):
    conexion = obtener_conexion()
    cursor = None

    try:
        cursor = conexion.cursor(dictionary=True)

        consulta = """SELECT * FROM usuarios WHERE id_usuario = %s"""

        cursor.execute(consulta, (id_usuario,))

        usuario = cursor.fetchone()

        return usuario
    
    finally: 

        if cursor is not None:
            cursor.close()
        conexion.close()

def actualizar_usuario(id_usuario, nombre, apellidos, email):

    conexion = obtener_conexion()
    cursor = None

    try: 
        cursor = conexion.cursor(dictionary=True)

        consulta = """
            UPDATE usuarios
            SET nombre = %s,
                apellidos = %s,
                email = %s
            WHERE id_usuario = %s
                """

        valores = (nombre, apellidos, email, id_usuario)

        cursor.execute(consulta, valores)
        conexion.commit()

        return cursor.rowcount

    finally: 

        if cursor is not None:
            cursor.close()
        conexion.close()


def eliminar_usuario(id_usuario):

    conexion = obtener_conexion()
    cursor = None

    try:
        cursor = conexion.cursor()

        consulta = """DELETE FROM usuarios WHERE id_usuario = %s"""

        cursor.execute(consulta, (id_usuario,))
        conexion.commit()

        return cursor.rowcount

    finally: 

        if cursor is not None:
            cursor.close()
        conexion.close()