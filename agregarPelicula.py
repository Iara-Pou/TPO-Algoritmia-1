from funciones import *
import re
from datetime import datetime
import json

ruta_json = 'peliculas.json'
peliculas = cargar_peliculas(ruta_json)

def guardar_peliculas(peliculas, ruta_json):
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
    if titulo in conseguir_titulos(peliculas):
        return False

    # Validar que el título solo tenga letras, números, espacios, comas o "#"
    expresion_validacion = r"^[a-zA-Z0-9 #,]+$"
    if not re.match(expresion_validacion, titulo):
        print("El título contiene caracteres inválidos.")
        return False

    return True


def generoValido(genero_num, generos_disponibles):
    return 1 <= genero_num <= len(generos_disponibles)


def calificacionValida(calificacion):
    return 1 <= int(calificacion) <= 10


def actorValido(actor):
    expresion_validacion = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$"
    if not re.match(expresion_validacion, actor):
        print("El actor contiene caracteres inválidos.")
        return False
    return True


def agregar_pelicula():
    pelicula = {}

    # Ingresar un título y anexarlo a película
    titulo_ingresado = input('Ingresá el título de la pelicula: ')
    while not tituloValido(titulo_ingresado):
        titulo_ingresado = input('Título inválido. Ingresá un nuevo título para la pelicula: ')

    pelicula["titulo"] = titulo_ingresado

    # Ingresar género por número
    # Asume que devuelve una lista de géneros
    generos_disponibles = list(conseguir_generos(peliculas))  # Convertir a lista
    mostrarMenuNumerado(generos_disponibles)

    genero_ingresado = input('Ingresá un número para cargar el género: ')
    while not genero_ingresado.isdigit() or not generoValido(int(genero_ingresado), generos_disponibles):
        genero_ingresado = input(
            'Número inválido. Ingresá un número válido para cargar el género: ')
    pelicula["genero"] = generos_disponibles[int(genero_ingresado) - 1]

    # ingresar calificación
    calificacion_ingresada = input('Ingresá una calificación del 1 al 10:')
    while not calificacion_ingresada.isdigit() or not calificacionValida(calificacion_ingresada):
        # Calificación va del 1 al 10
        calificacion_ingresada = input(
            'Calificación inválida. Ingresá un número del 1 al 10 para cargar la calificación: ')
    pelicula["calificacion"] = calificacion_ingresada

    # Ingresar año
    anio_ingresado = input('Ingresá el año de la película: ')
    while not anio_ingresado.isdigit() or not anioValido(int(anio_ingresado)):
        anio_ingresado = input(
            'Año inválido. Ingresá un año válido para la película: ')
    pelicula["anio"] = int(anio_ingresado)

    # ingresar dos actores
    actores = []

    primer_actor = input('Ingresá un actor: ')
    while not actorValido(primer_actor):
        print("Nombre de actor inválido. Ingresá solo letras y acentos.")
        primer_actor = input('Ingresá un actor: ')
    actores.append(primer_actor)

    segundo_actor = input('Ingresá otro actor: ')
    while not actorValido(segundo_actor):
        print("Nombre de actor inválido. Ingresá solo letras y acentos.")
        segundo_actor = input('Ingresá otro actor: ')
    actores.append(segundo_actor)

    pelicula['actores'] = actores

    # Ingresar descripción
    descripcion_ingresada = input(
        'Ingresá la descripción de la película (hasta 200 caracteres): ')
    while not descripcionValida(descripcion_ingresada):
        descripcion_ingresada = input(
            'Descripción inválida. Ingresá una descripción válida (letras, números, puntos, comas, hasta 200 caracteres): ')
    pelicula["descripcion"] = descripcion_ingresada

    # Ingresar URL de la imagen
    url_imagen_ingresada = input(
        'Ingresá la URL de la imagen de la película: ')
    while not urlImagenValida(url_imagen_ingresada):
        url_imagen_ingresada = input(
            'URL de imagen inválida. Ingresá una URL válida (que termine en .jpg, .jpeg, o .png): ')
    pelicula["urlImagen"] = url_imagen_ingresada

    # Guardar la lista de películas actualizada en el archivo JSON
    peliculas.append(pelicula)
    guardar_peliculas(peliculas, ruta_json)
    print("Película agregada y guardada con éxito.")

