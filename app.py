from flask import Flask, request
from routes.users import usuarios_bp
from routes.spotify import spotify_bp
from routes.preferences import preferencias_bp

app = Flask(__name__)

app.register_blueprint(usuarios_bp)
app.register_blueprint(spotify_bp)
app.register_blueprint(preferencias_bp)


if __name__ == "__main__":
    app.run(debug=True)