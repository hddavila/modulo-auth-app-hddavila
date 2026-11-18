# Servicio básico de autenticación

Este proyecto contiene un ejemplo simulado de validación de credenciales en Python.

## Archivos

- `auth_service.py`: contiene la función `validar_credenciales(usuario, contrasena)` y un ejemplo de ejecución por consola.

## Instrucciones de ejecución

### Requisitos

- Python 3 instalado.
- No se requieren dependencias externas.

### Ejecutar el programa

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta el siguiente comando:

   ```bash
   python auth_service.py
   ```

   En algunos sistemas puede ser necesario utilizar:

   ```bash
   python3 auth_service.py
   ```

3. Ingresa un usuario y una contraseña cuando el programa lo solicite.

### Credenciales de prueba

| Usuario | Contraseña |
|---|---|
| `admin` | `admin123` |
| `usuario` | `clave123` |

El programa mostrará un mensaje indicando si las credenciales son válidas.

## Nota

Este código es una simulación con fines educativos. No debe utilizarse como mecanismo de autenticación en producción, ya que las contraseñas se encuentran escritas directamente en el código y no están protegidas mediante hashes.
