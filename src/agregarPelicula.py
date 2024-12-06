from src.funciones.funciones import *
import re
from datetime import datetime
import json
from src.manejarSesion import loguearError

ruta_json = 'data/peliculas.json'
peliculas = cargarPeliculas(ruta_json)


def guardarPeliculas(peliculas, ruta_json):
    with open(ruta_json, 'w', encoding='utf-8') as archivo:
        json.dump(peliculas, archivo, ensure_ascii=False, indent=4)


def anioValido(anio):
    anio_actual = datetime.now().year
    return 1888 <= anio <= anio_actual  # Primeras películas en 1888


def descripcionValida(descripcion):
    # Permitir letras, números, espacios, puntos y comas, y hasta 200 caracteres
    expresion_validacion = r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s.,]+$"
    return re.match(expresion_validacion, descripcion) and len(descripcion) <= 200


def urlImagenValida(url):
    # Verifica si la URL termina en una extensión de imagen común
    expresion_validacion = r"^https?://.+\.(jpg|jpeg|png)$"
    return re.match(expresion_validacion, url)


def tituloValido(titulo):
    # que no se repita
    if titulo in conseguirTitulos(peliculas):
        print('Error: el titulo ya se usó en otra película.')
        return False

    # Validar que el título solo tenga letras, números, espacios, comas o "#"
    expresion_validacion = r"^[a-zA-Z0-9 #,]+$"
    if not re.match(expresion_validacion, titulo):
        return False

    return True


def generoValido(genero_num, generos_disponibles):
    return 1 <= genero_num <= len(generos_disponibles)


def calificacionValida(calificacion):
    return 1 <= int(calificacion) <= 10


def actorValido(actor):
    expresion_validacion = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$"
    if not re.match(expresion_validacion, actor):
        return False
    return True


def crearPelicula(titulo_ingresado, genero_ingresado, calificacion_ingresada, anio_ingresado, actores, descripcion_ingresada, url_imagen_ingresada):
    pelicula = {}
    pelicula["titulo"] = titulo_ingresado
    pelicula["genero"] = genero_ingresado
    pelicula["calificacion"] = int(calificacion_ingresada)
    pelicula["anio"] = int(anio_ingresado)
    pelicula['actores'] = actores
    pelicula["descripcion"] = descripcion_ingresada
    pelicula["urlImagen"] = url_imagen_ingresada

    return pelicula


def agregarPelicula():
    print("\n---------------------------------------------------")
    print('Carga de películas: \nIMPORTANTE || Por favor, ingresá -1 en cualquier momento de la carga para cancelar el proceso. ')

    # Ingresar datos y validar:
    # título
    titulo_ingresado = input('Ingresá el título de la pelicula: ')
    while not tituloValido(titulo_ingresado):
        if titulo_ingresado == '-1':
            return cancelarCarga()
        titulo_ingresado = input(
            'Título inválido. Ingresá un nuevo título para la pelicula: ')
        loguearError(
            'Título inválido. Ingresá un nuevo título para la pelicula: ')
    print("---------------------------------------------------")

    # género (por número)
    generos_disponibles = sorted(list(conseguirGeneros(peliculas)))
    mostrarMenuNumerado(generos_disponibles)
    genero_ingresado = input('Ingresá un número para cargar el género: ')
    while not genero_ingresado.isdigit() or not generoValido(int(genero_ingresado), generos_disponibles):
        if genero_ingresado == '-1':
            return cancelarCarga()
        genero_ingresado = input(
            'Número inválido. Ingresá un número válido para cargar el género: ')
        loguearError(
            'Número inválido. Ingresá un número válido para cargar el género: ')
    print("---------------------------------------------------")

    # calificación
    calificacion_ingresada = input('Ingresá una calificación del 1 al 10:')
    while not calificacion_ingresada.isdigit() or not calificacionValida(calificacion_ingresada):
        if calificacion_ingresada == '-1':
            return cancelarCarga()
        # Calificación va del 1 al 10
        calificacion_ingresada = input(
            'Calificación inválida. Ingresá un número del 1 al 10 para cargar la calificación: ')
        loguearError(
            'Calificación inválida. Ingresá un número del 1 al 10 para cargar la calificación: ')
    print("---------------------------------------------------")

    # año
    anio_ingresado = input('Ingresá el año de la película: ')
    while not anio_ingresado.isdigit() or not anioValido(int(anio_ingresado)):
        if anio_ingresado == '-1':
            return cancelarCarga()
        anio_ingresado = input(
            'Año inválido. Ingresá un año válido para la película: ')
        loguearError('Año inválido. Ingresá un año válido para la película: ')
    print("---------------------------------------------------")

    # actores
    actores = []
    continua_carga = True
    actor_ingresado = input(
        'Ingresá un actor que forme parte del elenco, o "0" para finalizar la carga: ')

    while continua_carga:

        while not actorValido(actor_ingresado) and actor_ingresado not in ('0', '-1'):
            print(
                "ERROR: Nombre de actor inválido. Ingresá solo letras, espacios y acentos.")
            loguearError(
                "Nombre de actor inválido. Ingresá solo letras, espacios y acentos.")
            actor_ingresado = input(
                'Ingresá un actor o "0" para finalizar la carga: ')

        if actor_ingresado == '0' and not listaEstaVacia(actores):
            continua_carga = False
        # si usuario ingresa -1, cancelo la carga
        elif actor_ingresado == '-1':
            return cancelarCarga()
        # si quiere dejar de cargar actores, pero la lista esta vacía, error
        elif actor_ingresado == "0" and listaEstaVacia(actores):
            print("ERROR: Debes ingresar por lo menos un actor.")
            loguearError("Debes ingresar por lo menos un actor.")
            actor_ingresado = input(
                'Ingresá un actor o "0" para finalizar la carga: ')
        else:
            actores.append(actor_ingresado)
            actor_ingresado = input(
                'Ingresá otro actor que forme parte del elenco, o "0" para finalizar la carga: ')
    print("---------------------------------------------------")

    # descripción
    descripcion_ingresada = input(
        'Ingresá la descripción de la película (hasta 200 caracteres): ')
    while not descripcionValida(descripcion_ingresada):
        if descripcion_ingresada == '-1':
            return cancelarCarga()
        descripcion_ingresada = input(
            'Descripción inválida. Ingresá una descripción válida (letras, números, puntos, comas, hasta 200 caracteres): ')
        loguearError(
            'Descripción inválida. Ingresá una descripción válida (letras, números, puntos, comas, hasta 200 caracteres): ')
    print("---------------------------------------------------")

    # URL de imagen
    url_imagen_ingresada = input(
        'Ingresá la URL de la imagen de la película: ')
    while not urlImagenValida(url_imagen_ingresada):
        if url_imagen_ingresada == '-1':
            return cancelarCarga()
        url_imagen_ingresada = input(
            'URL de imagen inválida. Ingresá una URL válida (que termine en .jpg, .jpeg, o .png): ')
        loguearError(
            'URL de imagen inválida. Ingresá una URL válida (que termine en .jpg, .jpeg, o .png): ')
    print("---------------------------------------------------")

    # Guardar la lista de películas actualizada en el archivo JSON
    pelicula = crearPelicula(titulo_ingresado,
                             generos_disponibles[int(genero_ingresado) - 1],
                             calificacion_ingresada,
                             anio_ingresado,
                             actores,
                             descripcion_ingresada,
                             url_imagen_ingresada)

    print("\n---------------------------------------------------")
    print('La película a sumar es:\n')
    mostrarPeliculas([pelicula])
    print("\n---------------------------------------------------")

    print('¿Deseas agregar la película?')

    respuesta_agregar_pelicula = input(
        'Ingresá "si" para agregarla, "no" para cancelar la carga:').lower()
    while respuesta_agregar_pelicula not in ("no", "si"):
        respuesta_agregar_pelicula = input(
            'Por favor, ingresá "si" o "no" para decidir si cargar la película:')

    # si actualizo la pelicula, cargo y retorno el archivo actualizado
    if respuesta_agregar_pelicula == "si":
        peliculas.append(pelicula)
        guardarPeliculas(peliculas, ruta_json)
        print("Película agregada y guardada con éxito.")
        # Recarga películas para que no quede el json de películas desactualizado
        return cargarPeliculas(ruta_json)
    else:
        return cancelarCarga()

    # si no actualizo la película, retorna None
