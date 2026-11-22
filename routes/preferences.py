from services.preferences_service import registrar_preferencia, listar_preferencias_usuario, modificar_preferencia, borrar_preferencia
from mysql.connector import Error, IntegrityError
from validators.preferences_validator import validar_preferencia, validar_nueva_preferencia
from flask import Blueprint, jsonify, request
from services.preferences_service import registrar_preferencia

preferencias_bp = Blueprint("preferencias", __name__)



@preferencias_bp.route("/usuarios/<int:id_usuario>/preferencias", methods=["POST"])
def registrar_preferencia_usuario(id_usuario):

    try:
        datos = request.get_json(silent=True)

        error = validar_nueva_preferencia(datos)

        if error:
            return jsonify({"error": error}), 400

        id_cancion_spotify = datos.get("id_cancion_spotify")
        tipo_preferencia = datos.get("tipo_preferencia")

        id_preferencia = registrar_preferencia(
            id_usuario,
            id_cancion_spotify,
            tipo_preferencia
        )

        return jsonify({
            "mensaje": "Preferencia registrada correctamente",
            "id_preferencia": id_preferencia
        }), 201

    except IntegrityError:
        return jsonify({
            "error": "La preferencia ya existe o el usuario no es válido"
        }), 409

    except Exception as error:
        return jsonify({"error": str(error)}), 500



@preferencias_bp.route("/usuarios/<int:id_usuario>/preferencias", methods=["GET"])
def listar_preferencias(id_usuario):

    try:
        preferencias = listar_preferencias_usuario(id_usuario)

        return jsonify({
            "preferencias": preferencias
        }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500



@preferencias_bp.route("/usuarios/<int:id_usuario>/preferencias/<id_cancion_spotify>", methods=["PUT"])
def actualizar_preferencia_usuario(id_usuario, id_cancion_spotify):

    try:
        datos = request.get_json(silent=True)

        error = validar_preferencia(datos)

        if error:
            return jsonify({"error": error}), 400

        tipo_preferencia = datos.get("tipo_preferencia")

        actualizado = modificar_preferencia(
            id_usuario,
            id_cancion_spotify,
            tipo_preferencia
        )

        if not actualizado:
            return jsonify({"error": "Preferencia no encontrada"}), 404

        return jsonify({
            "mensaje": "Preferencia actualizada correctamente"
        }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@preferencias_bp.route("/usuarios/<int:id_usuario>/preferencias/<id_cancion_spotify>", methods=["DELETE"])
def eliminar_preferencia_usuario(id_usuario, id_cancion_spotify):

    try:
        eliminado = borrar_preferencia(
            id_usuario,
            id_cancion_spotify
        )

        if eliminado == 0:
            return jsonify({"error": "Preferencia no encontrada"}), 404

        return jsonify({
            "mensaje": "Preferencia eliminada correctamente"
        }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500
