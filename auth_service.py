def validar_credenciales(usuario: str, contrasena: str) -> bool:
    """
    Valida credenciales de ejemplo.

    Esta implementación es únicamente demostrativa: en una aplicación real,
    las contraseñas deben almacenarse como hashes seguros y verificarse
    mediante una biblioteca especializada.
    """
    usuarios_demo = {
        "admin": "admin123",
        "usuario": "clave123",
    }

    return usuarios_demo.get(usuario) == contrasena


if __name__ == "__main__":
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if validar_credenciales(usuario, contrasena):
        print("Credenciales válidas. Acceso concedido.")
    else:
        print("Credenciales incorrectas. Acceso denegado.")
