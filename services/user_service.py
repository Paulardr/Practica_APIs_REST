from repository.user_repository import crear_usuario, obtener_usuarios, obtener_usuario_id, actualizar_usuario, eliminar_usuario

def registrar_usuario (nombre, apellidos, email):

    return crear_usuario(nombre, apellidos, email)

def lista_usuarios():
    return obtener_usuarios()

def buscar_usuario(id_usuario):
    return obtener_usuario_id(id_usuario)

def modificar_usuario(id_usuario, nombre, apellidos, email):

    usuario = obtener_usuario_id(id_usuario)

    if usuario is None:
        return False

    actualizar_usuario(
        id_usuario,
        nombre, 
        apellidos,
        email
    )

    return True

def borrar_usuario(id_usuario):
    return eliminar_usuario(id_usuario)