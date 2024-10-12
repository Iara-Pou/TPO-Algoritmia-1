def cargar_usuarios_desde_archivo():
    usuarios = ()
    with open("usuarios.txt", "r") as archivo:
        for linea in archivo:
            # Eliminar espacios en blanco y separar el nombre de usuario y contraseña
            linea = linea.strip()
            usuario, contrasenia = linea.split(",")
            # Agregar a la tupla de usuarios
            usuarios += ((usuario, contrasenia),)

    return usuarios


def login():
    usuarios = cargar_usuarios_desde_archivo()
    intentos_permitidos = 3

    print('¡Bienvenido!')
    while intentos_permitidos > 0:
        nombre_usuario = input("Introduce tu usuario: ")
        contrasenia_usuario = input("Introduce tu contraseña: ")

        for usuario, contrasenia in usuarios:
            if usuario == nombre_usuario and contrasenia == contrasenia_usuario:
                # Inicio de sesion exitoso
                print("¡Acceso exitoso!")
                print("-----------------------------------------------------------")
                return True

        # Disminuir el numero de intentos
        intentos_permitidos -= 1
        print(
            f"Credenciales incorrectas. Te quedan {intentos_permitidos} intento(s).")
        print("-----------------------------------------------------------")

    # Si no se logran las credenciales después de 3 intentos
    print("Has agotado todos los intentos. Acceso denegado.")
    return False
