from flask import Blueprint, jsonify, request
from mysql.connector import IntegrityError
from requests.exceptions import HTTPError, RequestException

from services.playlists_service import registrar_playlist, listar_playlists_usuario, consultar_playlist, modificar_playlist, borrar_playlist, registrar_cancion_playlist, listar_canciones_playlist, borrar_cancion_playlist

from validators.playlists_validator import validar_playlist, validar_cancion_playlist


playlists_bp = Blueprint("playlists", __name__)


@playlists_bp.route("/usuarios/<int:id_usuario>/playlists", methods=["POST"])
def crear_playlist_usuario(id_usuario):

    try:
        datos = request.get_json(silent=True)

        error = validar_playlist(datos)

        if error:
            return jsonify({"error": error}), 400

        nombre = datos.get("nombre").strip()
        descripcion = datos.get("descripcion")

        id_playlist = registrar_playlist(
            id_usuario,
            nombre,
            descripcion
        )

        return jsonify({
            "mensaje": "Playlist creada correctamente",
            "id_playlist": id_playlist
        }), 201

    except IntegrityError as error:

        if error.errno == 1452:
            return jsonify({"error": "El usuario no existe"}), 404

        return jsonify({
            "error": "Error de integridad en la base de datos"
        }), 400

    except Exception as error:
        return jsonify({"error": str(error)}), 500



@playlists_bp.route("/usuarios/<int:id_usuario>/playlists", methods=["GET"])
def obtener_playlists_usuario_route(id_usuario):

    try:
        playlists = listar_playlists_usuario(id_usuario)

        return jsonify({
            "playlists": playlists
        }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500



@playlists_bp.route("/usuarios/<int:id_usuario>/playlists/<int:id_playlist>", methods=["GET"])
def obtener_playlist_usuario_route(id_usuario, id_playlist):

    try:
        playlist = consultar_playlist(id_usuario, id_playlist)

        if playlist is None:
            return jsonify({"error": "Playlist no encontrada"}), 404

        return jsonify(playlist), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500




@playlists_bp.route("/usuarios/<int:id_usuario>/playlists/<int:id_playlist>", methods=["PUT"])
def actualizar_playlist_usuario(id_usuario, id_playlist):

    try:
        datos = request.get_json(silent=True)

        error = validar_playlist(datos)

        if error:
            return jsonify({"error": error}), 400

        nombre = datos.get("nombre").strip()
        descripcion = datos.get("descripcion")

        actualizado = modificar_playlist(
            id_usuario,
            id_playlist,
            nombre,
            descripcion
        )

        if not actualizado:
            return jsonify({"error": "Playlist no encontrada"}), 404

        return jsonify({
            "mensaje": "Playlist actualizada correctamente"
        }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500



@playlists_bp.route("/usuarios/<int:id_usuario>/playlists/<int:id_playlist>", methods=["DELETE"])
def eliminar_playlist_usuario(id_usuario, id_playlist):

    try:
        eliminado = borrar_playlist(id_usuario, id_playlist)

        if eliminado == 0:
            return jsonify({"error": "Playlist no encontrada"}), 404

        return jsonify({
            "mensaje": "Playlist eliminada correctamente"
        }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500



@playlists_bp.route("/usuarios/<int:id_usuario>/playlists/<int:id_playlist>/canciones", methods=["POST"])
def agregar_cancion_playlist_usuario(id_usuario, id_playlist):

    try:
        datos = request.get_json(silent=True)

        error = validar_cancion_playlist(datos)

        if error:
            return jsonify({"error": error}), 400

        id_cancion_spotify = datos["id_cancion_spotify"].strip()

        cancion = registrar_cancion_playlist(
            id_usuario,
            id_playlist,
            id_cancion_spotify
        )

        if cancion is None:
            return jsonify({"error": "Playlist no encontrada"}), 404

        return jsonify({
            "mensaje": "Cancion añadida correctamente",
            "cancion": cancion
        }), 201

    except HTTPError as error:

        if error.response is not None and error.response.status_code == 404:
            return jsonify({
                "error": "La cancion no existe en Spotify"
            }), 404

        return jsonify({
            "error": "Error al consultar Spotify"
        }), 502

    except RequestException:
        return jsonify({
            "error": "No se ha podido conectar con Spotify"
        }), 502

    except IntegrityError as error:

        if error.errno == 1062:
            return jsonify({
                "error": "La cancion ya existe en esta playlist"
            }), 409

        if error.errno == 1452:
            return jsonify({
                "error": "La playlist no existe"
            }), 404

        return jsonify({
            "error": "Error de integridad en la base de datos"
        }), 400

    except Exception:
        return jsonify({
            "error": "Error interno del servidor"
        }), 500



@playlists_bp.route("/usuarios/<int:id_usuario>/playlists/<int:id_playlist>/canciones", methods=["GET"])
def obtener_canciones_playlist_usuario(id_usuario, id_playlist):

    try:
        canciones = listar_canciones_playlist(
            id_usuario,
            id_playlist
        )

        if canciones is None:
            return jsonify({
                "error": "Playlist no encontrada"
            }), 404

        return jsonify({
            "id_playlist": id_playlist,
            "canciones": canciones
        }), 200

    except HTTPError:
        return jsonify({
            "error": "Error al obtener informacion de las canciones desde Spotify"
        }), 502

    except RequestException:
        return jsonify({
            "error": "No se ha podido conectar con Spotify"
        }), 502

    except Exception:
        return jsonify({
            "error": "Error interno del servidor"
        }), 500



@playlists_bp.route("/usuarios/<int:id_usuario>/playlists/<int:id_playlist>/canciones/<id_cancion_spotify>", methods=["DELETE"])
def eliminar_cancion_playlist_usuario(id_usuario, id_playlist, id_cancion_spotify):

    try:
        eliminado = borrar_cancion_playlist(
            id_usuario,
            id_playlist,
            id_cancion_spotify
        )

        if eliminado is None:
            return jsonify({
                "error": "Playlist no encontrada"
            }), 404

        if eliminado == 0:
            return jsonify({
                "error": "La cancion no existe en esta playlist"
            }), 404

        return jsonify({
            "mensaje": "Cancion eliminada correctamente"
        }), 200

    except Exception:
        return jsonify({
            "error": "Error interno del servidor"
        }), 500
