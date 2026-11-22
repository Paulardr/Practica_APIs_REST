from services.spotify_service import obtener_token_spotify

respuesta = obtener_token_spotify()

#print("Tipo de token:", respuesta["token_type"])
#print("Tiempo de expiración:", respuesta["expires_in"])
#print("Token obtenido correctamente:", bool(respuesta.get("access_token")))


token1 = obtener_token_spotify()
token2 = obtener_token_spotify()

print("Primer token obtenido:", bool(token1))
print("Segundo token obtenido:", bool(token2))
print("¿Se ha reutilizado el token?", token1 == token2)