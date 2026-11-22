from flask import Blueprint, jsonify
from services.spotify_service import obtener_cancion_spotify, obtener_artista_spotify


spotify_bp = Blueprint("spotify", __name__)

@spotify_bp.route("/spotify/canciones/<id_cancion>", methods=["GET"])
def consultar_cancion(id_cancion):

    try:
        cancion = obtener_cancion_spotify(id_cancion)
        return jsonify(cancion), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500

@spotify_bp.route("/spotify/artistas/<id_artista>", methods=["GET"])
def consultar_artista(id_artista):

    try: 
        artista = obtener_artista_spotify(id_artista)
        return jsonify(artista), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500