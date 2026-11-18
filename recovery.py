import secrets


def solicitar_recuperacion(correo: str) -> str | None:
    """
    Simula una solicitud de recuperación de contraseña.

    En un sistema real, se debería comprobar el correo en la base de datos
    y enviar un enlace o código temporal al usuario.
    """
    if not correo or "@" not in correo:
        print("Correo electrónico no válido.")
        return None

    token = secrets.token_urlsafe(16)
    print(f"Solicitud de recuperación registrada para: {correo}")
    print(f"Código de recuperación simulado: {token}")

    return token


def restablecer_contrasena(token_recibido: str, token_valido: str,
                           nueva_contrasena: str) -> bool:
    """
    Simula el restablecimiento de contraseña verificando el código recibido.
    """
    if not token_recibido or token_recibido != token_valido:
        print("El código de recuperación no es válido.")
        return False

    if len(nueva_contrasena) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False

    print("Contraseña restablecida correctamente (simulación).")
    return True


if __name__ == "__main__":
    correo = input("Correo electrónico: ")
    token = solicitar_recuperacion(correo)

    if token:
        codigo = input("Ingresa el código mostrado: ")
        nueva = input("Nueva contraseña (mínimo 8 caracteres): ")
        restablecer_contrasena(codigo, token, nueva)
