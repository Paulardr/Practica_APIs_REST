from flask import Blueprint, jsonify, request
from mysql.connector import IntegrityError
from requests.exceptions import HTTPError, RequestException

from services.favorite_artists_service import agregar_artista_favorito, listar_artistas_favoritos, borrar_artista_favorito

from validators.favorite_artists_validator import validar_artista_favorito

artistas_favoritos_bp = Blueprint("artistas_favoritos", __name__)


@artistas_favoritos_bp.route("/usuarios/<int:id_usuario>/artistas-favoritos", methods=["POST"])
def registrar_artista_favorito_usuario(id_usuario):

    try:
        datos = request.get_json(silent=True)

        error = validar_artista_favorito(datos)

        if error:
            return jsonify({"error": error}), 400

        id_artista_spotify = datos.get("id_artista_spotify")

        id_favorito = agregar_artista_favorito(
            id_usuario,
            id_artista_spotify
        )

        return jsonify({
            "mensaje": "Artista favorito registrado correctamente",
            "id_favorito": id_favorito
        }), 201

    except HTTPError as error:

        if error.response is not None and error.response.status_code == 404:
            return jsonify({
                "error": "El artista no existe en Spotify"
            }), 404

        return jsonify({
            "error": "Error al consultar la API de Spotify"
        }), 502

    except IntegrityError as error:
        if error.errno == 1062:
            return jsonify({"error": "El artista ya está registrado como favorito"}), 409

        if error.errno == 1452:
            return jsonify({"error": "El usuario no existe"}), 404

        return jsonify({"error": "Error de integridad en la base de datos"}), 400

    except Exception as error:
        return jsonify({"error": str(error)}), 500



@artistas_favoritos_bp.route("/usuarios/<int:id_usuario>/artistas-favoritos", methods=["GET"])
def consultar_artistas_favoritos_usuario(id_usuario):

    try:
        artistas = listar_artistas_favoritos(id_usuario)

        return jsonify({
            "artistas_favoritos": artistas
        }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500



@artistas_favoritos_bp.route("/usuarios/<int:id_usuario>/artistas-favoritos/<id_artista_spotify>", methods=["DELETE"])
def eliminar_artista_favorito_usuario(id_usuario, id_artista_spotify):

    try:
        eliminado = borrar_artista_favorito(
            id_usuario,
            id_artista_spotify
        )

        if eliminado == 0:
            return jsonify({"error": "Artista favorito no encontrado"}), 404

        return jsonify({
            "mensaje": "Artista favorito eliminado correctamente"
        }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500
