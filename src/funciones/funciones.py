import json
from src.manejarSesion import loguear_excepcion


def filtrar_rango_anios(anio_inicio, anio_fin, anios):
    return list(filter(lambda anio: anio >= int(anio_inicio) and anio <= int(anio_fin), anios))


def cargar_peliculas(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            peliculas = json.load(archivo)
        return peliculas
    except FileNotFoundError:
        mensaje = f"ERROR: No se encontró el archivo en la ruta '{ruta_archivo}'."
        print(mensaje)
        loguear_excepcion(mensaje)
        return []
    except json.JSONDecodeError:
        mensaje = f"ERROR: El archivo '{ruta_archivo}' no contiene un JSON válido.'."
        print(mensaje)
        loguear_excepcion(mensaje)
        return []
    except Exception as e:
        mensaje = f"ERROR INESPERADO: {e}"
        print(mensaje)
        loguear_excepcion(mensaje)
        return []


def buscar_por_genero(peliculas, genero):
    return [p for p in peliculas if p['genero'].lower() == genero.lower()]


def buscar_por_anio(peliculas, anio):
    return [p for p in peliculas if anio == p["anio"]]


def buscar_por_calificacion(peliculas, calificacion):
    return [p for p in peliculas if p['calificacion'] == calificacion]


def buscar_por_titulo(peliculas, titulo):
    for pelicula in peliculas:
        if pelicula['titulo'] == titulo:
            return pelicula
    return None


def mostrar_peliculas(peliculas):
    for p in peliculas:
        print(f"Título: {p['titulo']}\nGénero: {p['genero']}\nCalificación: {p['calificacion']}\nAño: {p['anio']}\nActores: {', '.join(p['actores'])}\nDescripción: {p['descripcion']}\n")


def conseguir_generos(peliculas):
    return set(map(lambda pelicula: pelicula['genero'], peliculas))


def conseguir_anios(peliculas):
    return set(map(lambda pelicula: pelicula['anio'], peliculas))


def conseguir_calificaciones(peliculas):
    return set(map(lambda pelicula: pelicula['calificacion'], peliculas))


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


def listaEstaVacia(lista):
    if len(lista) == 0:
        return True
    return False


def cancelarCarga():
    print('Carga cancelada')
    return -1