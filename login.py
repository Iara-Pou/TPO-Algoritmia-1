from manejarSesion import set_informacion_usuario


def cargar_usuarios_desde_archivo():
    usuarios = ()
    with open("usuarios.txt", "r") as archivo:
        for linea in archivo:
            # Eliminar espacios en blanco y separar el nombre de usuario y contraseña
            linea = linea.strip()
            usuario, contrasenia, rol = linea.split(",")
            # Agregar a la tupla de usuarios
            usuarios += ((usuario, contrasenia, rol),)

    return usuarios


def nombre_en_uso(usuarios, nombre_usuario):
    # Itero usuarios, si alguno fuera igual retorno True (si existe)
    for usuario in usuarios:
        if usuario[0] == nombre_usuario:
            return True
    # Sino, retorno False (no existe)
    return False


def agregar_usuario_a_archivo(nombre_usuario, contrasenia_usuario, rol_usuario):
    # Cargar usuarios
    usuarios = cargar_usuarios_desde_archivo()

    # Validar que no repito nombre
    while nombre_en_uso(usuarios, nombre_usuario):
        print(
            f"El nombre de usuario '{nombre_usuario}' ya está en uso. Elige otro.")
        nombre_usuario = input('Nombre nuevo: ')
        contrasenia_usuario = input('Contraseña: ')
        print("-----------------------------------------------------------")

    # Agregar el nuevo usuario
    with open("usuarios.txt", "a") as archivo:
        archivo.write(
            f"{nombre_usuario},{contrasenia_usuario},{rol_usuario}\n")
    print(f"Usuario {nombre_usuario} agregado exitosamente.")
    print("-----------------------------------------------------------")


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

                for usuario, contrasenia, rol in usuarios:
                    if usuario == nombre_usuario and contrasenia == contrasenia_usuario:
                        # Inicio de sesión exitoso
                        # Seteo datos del usuario logueado
                        set_informacion_usuario(nombre_usuario, rol)
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
            # el rol por defecto es usuario, si quiere ser admin se modifica el archivo a futuro
            rol_usuario = 'usuario'
            agregar_usuario_a_archivo(
                nombre_usuario, contrasenia_usuario, rol_usuario)
            # Actualizar la lista de usuarios después de agregar uno nuevo
            usuarios = cargar_usuarios_desde_archivo()
            print('¡Creación de usuario exitosa!')

        else:
            print("Opción no válida. Inténtalo de nuevo.")
            print("-----------------------------------------------------------")

    print('Acceso denegado.')
