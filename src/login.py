from src.manejarSesion import setInformacionUsuario, loguearInformacionUsuario


def cargarUsuariosDesdeArchivo():
    usuarios = ()
    with open(ruta_usuarios, "r") as archivo:
        for linea in archivo:
            # Eliminar espacios en blanco y separar el nombre de usuario y contraseña
            linea = linea.strip()
            usuario, contrasenia, rol = linea.split(",")
            # Agregar a la tupla de usuarios
            usuarios += ((usuario, contrasenia, rol),)

    return usuarios


def nombreEnUso(usuarios, nombre_usuario):
    # Itero usuarios, si alguno fuera igual retorno True (si existe)
    for usuario in usuarios:
        if usuario[0] == nombre_usuario:
            return True
    # Sino, retorno False (no existe)
    return False


def agregarUsuarioAArchivo(nombre_usuario, contrasenia_usuario, rol_usuario):
    # Cargar usuarios
    usuarios = cargarUsuariosDesdeArchivo()

    # Validar que no repito nombre
    while nombreEnUso(usuarios, nombre_usuario):
        print(
            f"El nombre de usuario '{nombre_usuario}' ya está en uso. Elige otro.")
        nombre_usuario = input('Nombre nuevo: ')
        contrasenia_usuario = input('Contraseña: ')
        print("-----------------------------------------------------------")

    # Agregar el nuevo usuario
    with open(ruta_usuarios, "a") as archivo:
        archivo.write(
            f"{nombre_usuario},{contrasenia_usuario},{rol_usuario}\n")
    print(f"Usuario {nombre_usuario} agregado exitosamente.")
    print("-----------------------------------------------------------")


def login():
    usuarios = cargarUsuariosDesdeArchivo()
    usuarios_con_intentos = dict()
    intentos_permitidos = 3

    # cargo usuarios e intentos permitidos
    for usuario in usuarios:
        usuarios_con_intentos[usuario[0]] = intentos_permitidos

    while True:
        # menu del login
        print("\n---------------------------------------------------")
        print('CINEMATCH')
        print("---------------------------------------------------")
        print("1. Iniciar sesión")
        print("2. Agregar nuevo usuario")
        print("---------------------------------------------------")

        opcion = input("Elige una opción: ").strip()
        print("---------------------------------------------------\n")

        if opcion == "1":
            # Iniciar sesión
            nombre_usuario = input("Introduce tu usuario: ")

            # Verificar si el usuario existe
            if nombre_usuario not in usuarios_con_intentos:
                print("El usuario no existe.")
                continue

            while usuarios_con_intentos[nombre_usuario] > 0:
                contrasenia_usuario = input(
                    "Introduce tu contraseña: ").strip()
                print("---------------------------------------------------")

                # Verificar las credenciales
                for usuario, contrasenia, rol in usuarios:
                    if usuario == nombre_usuario and contrasenia == contrasenia_usuario:
                        # Inicio de sesión exitoso
                        setInformacionUsuario(nombre_usuario, rol)
                        print("¡Acceso exitoso!")
                        print(
                            "-----------------------------------------------------------")
                        # Loguea información del login
                        loguearInformacionUsuario(
                            nombre_usuario, rol, True, False)
                        return True

                # Disminuir el número de intentos
                usuarios_con_intentos[nombre_usuario] -= 1
                print(
                    f"Credenciales incorrectas. Te quedan {usuarios_con_intentos[nombre_usuario]} intento(s).")
                print("---------------------------------------------------")

            print("Acceso denegado por intentos fallidos.")
            return False

        elif opcion == "2":
            # Agregar un nuevo usuario
            nombre_usuario = input("Introduce el nombre del nuevo usuario: ")
            contrasenia_usuario = input(
                "Introduce la contraseña del nuevo usuario: ")
            # el rol por defecto es usuario, si quiere ser admin se modifica el archivo a futuro
            rol_usuario = 'usuario'
            agregarUsuarioAArchivo(
                nombre_usuario, contrasenia_usuario, rol_usuario)
            # Actualizar la lista de usuarios después de agregar uno nuevo
            usuarios = cargarUsuariosDesdeArchivo()
            print('¡Creación de usuario exitosa!')

        else:
            print("Opción no válida. Inténtalo de nuevo.")
            print("-----------------------------------------------------------")


ruta_usuarios = "data/usuarios.txt"
