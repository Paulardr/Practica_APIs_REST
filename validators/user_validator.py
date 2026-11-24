import re

def validar_usuario(datos):

    if not isinstance(datos, dict):
        return "Debes enviar un JSON válido"

    nombre = datos.get("nombre")
    apellidos = datos.get("apellidos")
    email = datos.get("email")

    if not all(isinstance(valor, str) and valor.strip()
            for valor in (nombre, apellidos, email)):
        return "Nombre, apellidos y email son obligatorios"

    if len(nombre.strip()) > 100:
        return "El nombre no puede superar los 100 caracteres"

    if len(apellidos.strip()) > 100:
        return "Los apellidos no pueden superar los 100 caracteres"

    if len(email.strip()) > 150:
        return "El email no puede superar los 150 caracteres"

    if not re.fullmatch(r"[A-Za-z0-9._%+-]+@gmail\.com", email.strip(), re.IGNORECASE):
        return "El formato debe ser @gmail.com"
    
    return None