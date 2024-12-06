from src.funciones.funciones import *
from src.login import login
from src.agregarPelicula import agregarPelicula
from functools import reduce
from src.manejarSesion import getIdUsuario, getRolUsuario, loguearInformacionUsuario, loguearError


def ingresar_genero(generos):
    print("\n---------------------------------------------------")
    print('IMPORTANTE || Por favor, ingresá -1 en cualquier momento de la carga para cancelar el proceso.')
    print("¿Qué género te gustaría ver? Aquí te dejo una lista con los géneros disponibles:")
    mostrarMenuNumerado(generos)

    while True:
        try:
            eleccion_genero = int(input('Ingresá el género: '))
            while eleccion_genero < 1 or eleccion_genero > len(generos):
                if eleccion_genero == -1:
                    return cancelarCarga()
                print(
                    "El género elegido no está en la lista. Por favor, intenta de nuevo.")
                loguearError(
                    "El género elegido no está en la lista. Por favor, intenta de nuevo.")
                eleccion_genero = int(input('Ingresá el género: '))
            return list(generos)[eleccion_genero-1]
        except ValueError:
            mensaje = "Debes ingresar un número para ingresar el género."
            print(mensaje)
            loguearExcepcion(mensaje)


def seleccionar_opcion(elementos, tipo_elemento):
    while True:
        try:
            eleccion = int(input(
                f"Por favor, ingresa un/una {tipo_elemento}: ").strip())
            # Si el usuario ingresa -1, cancela el circuito
            if eleccion == -1:
                return cancelarCarga()
            # Si es un número y está dentro de los elementos que puedo elegir, lo retorna
            if eleccion in elementos:
                return eleccion
            # mensaje error
            print("El", tipo_elemento,
                  "no está en la lista. Por favor, intenta de nuevo.")
            loguearError("El", tipo_elemento,
                         "no está en la lista. Por favor, intenta de nuevo.")
        except ValueError:
            mensaje = "Debes ingresar un número para seleccionar la opción."
            print(mensaje)
            loguearExcepcion(mensaje)


def seleccionar_rango(elementos, tipo_elemento):
    primer_elemento = seleccionar_opcion(elementos, f"primer {tipo_elemento}")
    if primer_elemento == -1:
        return cancelarCarga()

    elementos_siguientes = filtrarRangoAnios(
        primer_elemento, elementos[-1], elementos)
    print(' - '.join(map(str, elementos_siguientes)))

    segundo_elemento = seleccionar_opcion(elementos, f"{tipo_elemento} de fin")
    if segundo_elemento == -1:
        return cancelarCarga()

    if segundo_elemento >= primer_elemento:
        return filtrarRangoAnios(primer_elemento, segundo_elemento, elementos)
    else:
        # si no ingresó un rango válido, vuelve a llamar a la funcion para que lo haga
        print("El rango no es válido. Intenta nuevamente.")
        print("-----------------------------------------------------")
        print(' - '.join(map(str, elementos)))
        loguearError("El rango no es válido. Intenta nuevamente.")

        return seleccionar_rango(elementos, tipo_elemento)


def ingresar_anio_estreno(anios):
    print("-----------------------------------------------------")
    print("¿Te gustaría elegir un año específico de estreno?")
    print(' - '.join(map(str, anios)))
    mostrarMenuNumerado(['Sí', 'Prefiero un rango', 'No'])
    modalidad = input().strip()

    while modalidad not in ('1', '2', '3'):
        modalidad = input("Por favor, ingresa una opción válida: ").strip()
        loguearError("Por favor, ingresa una opción válida: ")

    if modalidad == '1':
        return seleccionar_opcion(anios, 'año')
    elif modalidad == '2':
        return seleccionar_rango(anios, 'año')
    return None


def ingresar_calificacion(calificaciones):
    print("-----------------------------------------------------")
    print("¿Preferís alguna calificación?")
    print(' - '.join(map(str, calificaciones)))
    mostrarMenuNumerado(['Sí', 'Prefiero un rango', 'No'])
    modalidad = input().strip()

    while modalidad not in ('1', '2', '3'):
        modalidad = input("Por favor, ingresa una opción válida: ").strip()
        loguearError("Por favor, ingresa una opción válida: ")

    if modalidad == '1':
        return seleccionar_opcion(calificaciones, 'calificación')
    elif modalidad == '2':
        return seleccionar_rango(calificaciones, 'calificación')
    return None


def recomendar_pelicula(peliculas):
    # recupera todos los generos, anios y calificaciones
    generos = sorted(conseguirGeneros(peliculas))
    anios = sorted(conseguirAnios(peliculas))
    calificaciones = sorted(conseguirCalificaciones(peliculas))

    # CONSEGUIR DATOS DEL USUARIO
    # obtiene las elecciones de genero, anio, calificación como parámetros para el filtro de la recomendación
    eleccion_genero = ingresar_genero(generos)
    if eleccion_genero == -1:
        return
    eleccion_anio = ingresar_anio_estreno(anios)
    if eleccion_anio == -1:
        return
    eleccion_calificacion = ingresar_calificacion(calificaciones)
    if eleccion_calificacion == -1:
        return

    # GENERAR MATRIZ DE RECOMENDACIÓN
    lista_por_genero = conseguirTitulos(
        buscarPorGenero(peliculas, eleccion_genero))
    lista_por_anio = []
    lista_por_calificacion = []

    # filtra películas por año ingresado y devuelve una lista
    if isinstance(eleccion_anio, list):
        lista_por_anio = reduce(lambda acumulador, anio: acumulador + list(
            conseguirTitulos(buscarPorAnio(peliculas, anio))), eleccion_anio, [])
    elif eleccion_anio is not None:
        lista_por_anio = conseguirTitulos(
            buscarPorAnio(peliculas, eleccion_anio))

    # filtra películas por calificación ingresada y devuelve una lista
    if isinstance(eleccion_calificacion, list):
        lista_por_calificacion = reduce(lambda acumulador, calificacion: acumulador + list(
            conseguirTitulos(buscarPorCalificacion(peliculas, calificacion))), eleccion_calificacion, [])
    elif eleccion_calificacion is not None:
        lista_por_calificacion = conseguirTitulos(
            buscarPorCalificacion(peliculas, eleccion_calificacion))

    # arma matriz de películas filtradas por parámetros anteriores
    peliculas_filtradas = [lista_por_genero,
                           lista_por_anio, lista_por_calificacion]
    peliculas_recomendadas = []

    # GENERA LISTA DE PELÍCULAS RECOMENDADAS
    # si la película tiene el genero y el año o el género y la calificación, la almacena como una película a recomendar
    if listaEstaVacia(lista_por_anio) and listaEstaVacia(lista_por_calificacion):
        peliculas_recomendadas = lista_por_genero
    else:
        peliculas_recomendadas = list(filter(
            lambda pelicula: pelicula in peliculas_filtradas[1] or pelicula in peliculas_filtradas[2],
            peliculas_filtradas[0]
        ))

    # MUESTRA RECOMENDACIÓN
    if peliculas_recomendadas:
        informacion_peliculas = [buscarPorTitulo(
            peliculas, titulo) for titulo in peliculas_recomendadas if buscarPorTitulo(peliculas, titulo)]
        print("Te recomendamos:\n")
        mostrarPeliculas(informacion_peliculas)
        print("\nEsperamos que te gusten ;D")
    else:
        print('No se encontraron películas para recomendar.')
    print("\n---------------------------------------------------")


def listar_peliculas_por_genero(peliculas):
    generos = sorted(conseguirGeneros(peliculas))
    eleccion_genero = ingresar_genero(generos)
    if eleccion_genero == -1:
        return
    print("\n---------------------------------------------------")
    print("Películas encontradas:\n")
    mostrarPeliculas(buscarPorGenero(peliculas, eleccion_genero))
    print("\n---------------------------------------------------")


def usuario_es_admin():
    return getRolUsuario() == 'admin'


# Flujo principal del programa
ruta_json = 'data/peliculas.json'
peliculas = cargarPeliculas(ruta_json)


# Tienen que existir películas con formato valido
# (cargar_peliculas retorna una lista vacía si se genera una excepción en la carga del archivo)
if not listaEstaVacia(peliculas) and login():
    continuar = True
    while continuar:

        # IMPRIMIR MENU
        print("\n---------------------------------------------------")
        print(f'¡Bienvenido a CINEMATCH, {getIdUsuario()}!')
        print("---------------------------------------------------")
        print('1. Pedir recomendación.')
        print('2. Buscar por género.')
        # Opcion de agregar película solo disponible para usuarios admin
        if usuario_es_admin():
            print('3. Agregar película.')
            print('4. Salir del programa.')
        else:
            print('3. Salir del programa.')

        print("---------------------------------------------------")
        opcion = input('Ingresa la opción que desees: ').strip()
        print("---------------------------------------------------\n")

        # VALIDAR ITEM DE MENU INGRESADO
        while opcion not in ('1', '2', '3', '4') and usuario_es_admin():
            opcion = input("ERROR: Por favor, ingresá 1, 2, 3 o 4: ").strip()
            loguearError("Por favor, ingresá 1, 2, 3 o 4:")
        while opcion not in ('1', '2', '3') and not usuario_es_admin():
            opcion = input("ERROR: Por favor, ingresá 1, 2 o 3: ").strip()
            loguearError("Por favor, ingresá 1, 2 o 3: ")

        # REDIRIGIR A MÉTODO CORRESPONDIENTE SEGUN ITEM DE MENU
        if opcion == '1':
            recomendar_pelicula(peliculas)

        elif opcion == '2':
            listar_peliculas_por_genero(peliculas)

        # si usuario es admin, puede agregar pelicula
        elif opcion == '3' and usuario_es_admin():
            resultado = agregarPelicula()
            if resultado != -1:
                peliculas = resultado

        # la opción 4 del admin y tres del usuario normal cierra la sesión
        elif (opcion == '4' and usuario_es_admin()) or (opcion == '3' and not usuario_es_admin()):
            continuar = False
            # loguea logout en archivo de excepciones
            loguearInformacionUsuario(getIdUsuario(), '', False, True)
            print("¡Gracias por usar nuestro recomendador!")
