from flask import Blueprint, request
from mysql.connector import Error, IntegrityError
from validators.user_validator import validar_usuario
from services.user_service import registrar_usuario, lista_usuarios, buscar_usuario, modificar_usuario, borrar_usuario


usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", methods=["POST"])

def registrar_datos_usuario():
    datos = request.get_json(silent=True)

    error = validar_usuario(datos)

    if error:
        return {"error": error}, 400

    try:
        id_usuario = registrar_usuario(
            datos["nombre"].strip(),
            datos["apellidos"].strip(),
            datos["email"].strip(),
        )

        return {
            "mensaje": "Usuario creado correctamente",
            "id_usuario": id_usuario
        }, 201

    except IntegrityError:
        return {"error": "El email ya está registrado"}, 409

    except Error:
        return {"error": "Error al guardar el usuario"}, 500


@usuarios_bp.route("/usuarios", methods = ["GET"])

def lista_datos_usuarios():
    try:
        usuarios = lista_usuarios()

        return{
            "Lista de usuarios": usuarios
        }, 200

    except Error:
        return {"error": "Error al obtener la lista de usuarios"}, 500


@usuarios_bp.route("/usuarios/<int:id_usuario>", methods=["GET"])
def buscar_datos_usuario(id_usuario):
    try:
        usuario = buscar_usuario(id_usuario)

        if usuario is None:
            return {"error": "usuario no encontrado"}, 404

        return {"usuario": usuario}, 200

    except Error:
        return {"error": "Error al obtener el usuario"}, 500


@usuarios_bp.route("/usuarios/<int:id_usuario>", methods = ["PUT"])
def actualizar_datos_usuario(id_usuario):
    try: 
        datos = request.get_json(silent=True)

        error = validar_usuario(datos)

        if error:
            return {"error": error}, 400

        try:

            actualizado = modificar_usuario(
                id_usuario,
                datos["nombre"].strip(),
                datos["apellidos"].strip(),
                datos["email"].strip()
            )

            if not actualizado:
                return {"error": "Usuario no encontrado"}, 404

            return {
                "mensaje": "Usuario actualizado correctamente"
            }, 200

        except IntegrityError:
            return {"error": "El email ya existe"}, 409

    except Error:
        return {"error": "Error al actualizar el usuario"}, 500


@usuarios_bp.route("/usuarios/<int:id_usuario>", methods = ["DELETE"])
def borrar_datos_usuario(id_usuario):
    try:

        num_filas_eliminadas = borrar_usuario(id_usuario)

        if num_filas_eliminadas == 0:
            return {"error": "Usuario no encontrado"}, 404

        return {
            "mensaje": "Usuario eliminado correctamente"
        }, 200

    except Error:
        return {"error": "Error al eliminar el usuario"}, 500

