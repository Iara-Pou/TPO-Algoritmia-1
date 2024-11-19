import json
from difflib import SequenceMatcher

def filtrar_rango_anios(anio_inicio, anio_fin, anios):
    return list(filter(lambda anio: anio >= int(anio_inicio) and anio <= int(anio_fin), anios))    


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


def buscar_por_titulo(peliculas, titulo):
    return next((p for p in peliculas if p['titulo'] == titulo), None)


def mostrar_peliculas(peliculas):
    for p in peliculas:
        print(f"Título: {p['titulo']}\nGénero: {p['genero']}\nCalificación: {p['calificacion']}\nAño: {p['anio']}\nActores: {', '.join(p['actores'])}\nDescripción: {p['descripcion']}\n")


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
    if not peliculas:  # Caso base: lista vacía
        return set()
    # Extraer el título de la primera película y llamar recursivamente con el resto de titulos
    titulo = {peliculas[0]['titulo']}
    return titulo.union(conseguir_titulos(peliculas[1:]))


def mostrarMenuNumerado(opciones):
    opciones_menu = list(opciones)
    for i in range(len(opciones_menu)):
        print(f'{i + 1}. {opciones_menu[i]}')
        