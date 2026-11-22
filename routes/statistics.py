
from flask import Blueprint, jsonify

from services.statistics_service import consultar_estadisticas_usuario


statistics_bp = Blueprint("statistics", __name__)


@statistics_bp.route("/usuarios/<int:id_usuario>/estadisticas", methods=["GET"])
def obtener_estadisticas(id_usuario):

    try:
        estadisticas = consultar_estadisticas_usuario(id_usuario)

        if estadisticas is None:
            return jsonify({
                "error": "El usuario no existe"
            }), 404

        return jsonify(estadisticas), 200

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500
