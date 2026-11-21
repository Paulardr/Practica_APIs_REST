from database.connection import obtener_conexion

conexion = None

try:
    conexion = obtener_conexion()

    if conexion.is_connected():
        print ("Conexion establecida correctamente")

except Exception as error:
    print("Error al conectar con BBDD", error)

finally:
    if conexion is not None and conexion.is_connected():
        conexion.close()