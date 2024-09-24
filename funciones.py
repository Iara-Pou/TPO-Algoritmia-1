import json
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def buscar_por_descripcion(peliculas, palabras_clave):
    palabras = palabras_clave.lower().split()
    peliculas_encontradas = []

    for pelicula in peliculas:
        descripcion = pelicula['descripcion'].lower()
        # Verificamos si hay coincidencias aproximadas en la descripción
        if any(similar(palabra, descripcion) > 0.6 for palabra in palabras):  # Coincidencia aproximada > 60%
            peliculas_encontradas.append(pelicula)

    return peliculas_encontradas


def cargar_peliculas(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        peliculas = json.load(archivo)
    return peliculas


def buscar_por_genero(peliculas, genero):
    return [p for p in peliculas if p['genero'].lower() == genero.lower()]


def buscar_por_anio(peliculas,anio):
    return [p for p in peliculas if anio == p["anio"]]

def buscar_por_calificacion(peliculas, calificacion):
    return [p for p in peliculas if p['calificacion'] == calificacion]


def mostrar_peliculas(peliculas):
    for p in peliculas:
        print(f"Título: {p['titulo']}\nGénero: {p['genero']}\nCalificación: {p['calificacion']}\nAño: {p['anio']}\nActores: {', '.join(p['actores'])}\n")


def conseguir_generos(peliculas):
    generos = set()
    for pelicula in peliculas:
        generos.add(pelicula['genero'])

    return generos

def conseguir_anios(peliculas):
    anios = set()
    for pelicula in peliculas:
        anios.add(pelicula['anio'])
        
    return anios

def conseguir_calificaciones(peliculas):
    calificaciones = set()
    for pelicula in peliculas:
        calificaciones.add(pelicula['calificacion'])

    return calificaciones

def conseguir_titulos(peliculas):
    titulos = set()
    for pelicula in peliculas:
        titulos.add(pelicula['titulo'])
    return titulos