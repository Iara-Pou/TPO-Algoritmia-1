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


def agregar_usuario_a_archivo(nombre_usuario, contrasenia_usuario):
    # Modo "a" para agregar al final
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre_usuario},{contrasenia_usuario}\n")
    print(f"Usuario {nombre_usuario} agregado exitosamente.")


def login():
    usuarios = cargar_usuarios_desde_archivo()
    intentos_permitidos = 3

    while intentos_permitidos > 0:
        # menu del login
        print("\n---------------------------------------------------")
        print('CINEMATCH')
        print("---------------------------------------------------")
        print("1. Iniciar sesión")
        print("2. Agregar nuevo usuario")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Iniciar sesión
            while intentos_permitidos > 0:
                nombre_usuario = input("Introduce tu usuario: ")
                contrasenia_usuario = input("Introduce tu contraseña: ")

                for usuario, contrasenia in usuarios:
                    if usuario == nombre_usuario and contrasenia == contrasenia_usuario:
                        # Inicio de sesión exitoso
                        print("¡Acceso exitoso!")
                        print(
                            "-----------------------------------------------------------")
                        return True

                # Disminuir el número de intentos
                intentos_permitidos -= 1
                print(
                    f"Credenciales incorrectas. Te quedan {intentos_permitidos} intento(s).")
                print("-----------------------------------------------------------")

        elif opcion == "2":
            # Agregar un nuevo usuario
            nombre_usuario = input("Introduce el nombre del nuevo usuario: ")
            contrasenia_usuario = input(
                "Introduce la contraseña del nuevo usuario: ")
            agregar_usuario_a_archivo(nombre_usuario, contrasenia_usuario)
            # Actualizar la lista de usuarios después de agregar uno nuevo
            usuarios = cargar_usuarios_desde_archivo()
            print('¡Creación de usuario exitosa!')

        else:
            print("Opción no válida. Inténtalo de nuevo.")
            print("-----------------------------------------------------------")

    print('Acceso denegado.')
