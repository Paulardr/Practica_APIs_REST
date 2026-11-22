import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# gestion de token renovacion automatica
token_actual = None
fecha_expiracion = 0

def obtener_token_spotify():

    global token_actual, fecha_expiracion

    if token_actual is not None and time.time() < fecha_expiracion:
        return token_actual



    url = "https://accounts.spotify.com/api/token"

    datos = {
        "grant_type": "client_credentials"
    }

    respuesta = requests.post(
        url,
        data=datos,
        auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET),
        timeout=10
    )

    respuesta.raise_for_status()

    datos_token = respuesta.json()
    token_actual = datos_token["access_token"]
    fecha_expiracion = time.time() + datos_token["expires_in"] - 60

    return token_actual

def obtener_cancion_spotify(id_cancion):

    token = obtener_token_spotify()

    url = f"https://api.spotify.com/v1/tracks/{id_cancion}"

    cabeceras = {
        "Authorization": f"Bearer {token}"
    }

    respuesta = requests.get(url, headers=cabeceras, timeout=10)

    # en caso de error, esta funcion permite la generacion de una excepcion

    respuesta.raise_for_status()

    return respuesta.json()


def obtener_artista_spotify(id_artista):
    
    token = obtener_token_spotify()

    url = f"https://api.spotify.com/v1/artists/{id_artista}"

    cabeceras = {
            "Authorization": f"Bearer {token}"
        }
    
    respuesta = requests.get(url, headers=cabeceras, timeout=10)

    respuesta.raise_for_status()

    return respuesta.json()

