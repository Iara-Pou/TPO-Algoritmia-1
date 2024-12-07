import json
from src.manejarSesion import loguearExcepcion


def filtrarRangoAnios(anio_inicio, anio_fin, anios):
    return list(filter(lambda anio: anio >= int(anio_inicio) and anio <= int(anio_fin), anios))


def cargarPeliculas(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            peliculas = json.load(archivo)
        return peliculas
    except FileNotFoundError:
        mensaje = f"ERROR: No se encontró el archivo en la ruta '{ruta_archivo}'."
        print(mensaje)
        loguearExcepcion(mensaje)
        return []
    except json.JSONDecodeError:
        mensaje = f"ERROR: El archivo '{ruta_archivo}' no contiene un JSON válido.'."
        print(mensaje)
        loguearExcepcion(mensaje)
        return []
    except Exception as e:
        mensaje = f"ERROR INESPERADO: {e}"
        print(mensaje)
        loguearExcepcion(mensaje)
        return []


def buscarPorGenero(peliculas, genero):
    return [p for p in peliculas if p['genero'].lower() == genero.lower()]


def buscarPorAnio(peliculas, anio):
    return [p for p in peliculas if anio == p["anio"]]


def buscarPorCalificacion(peliculas, calificacion):
    return [p for p in peliculas if p['calificacion'] == calificacion]


def buscarPorTitulo(peliculas, titulo):
    for pelicula in peliculas:
        if pelicula['titulo'] == titulo:
            return pelicula
    return None


def mostrarPeliculas(peliculas):
    for p in peliculas:
        print(f"- Título: {p['titulo']}\n- Género: {p['genero']}\n- Calificación: {p['calificacion']}\n- Año: {p['anio']}\n- Actores: {', '.join(p['actores'])}\n- Descripción: {p['descripcion']}\n- URL imágen: {p['urlImagen']}\n")


def conseguirGeneros(peliculas):
    return set(map(lambda pelicula: pelicula['genero'], peliculas))


def conseguirAnios(peliculas):
    return set(map(lambda pelicula: pelicula['anio'], peliculas))


def conseguirCalificaciones(peliculas):
    return set(map(lambda pelicula: pelicula['calificacion'], peliculas))


def conseguirTitulos(peliculas):
    if not peliculas:
        return set()

    # Crea un conjunto con el título de la primera película
    titulo = {peliculas[0]['titulo']}
    # conseguirTitulos se llama a sí misma con peliculas[1:] (lista original menos el primer elemento)
    # en cada llamado, el primer elemento de la lista (peliculas[0]) se procesa. Función vuelve a llamarse con el resto de la lista
    return titulo.union(conseguirTitulos(peliculas[1:]))


def conseguirActores(peliculas):
    actores = []
    for pelicula in peliculas:
        # Asegurarse de que exista key "actores" en la película
        if "actores" in pelicula:
            # Agregar actores a la lista
            actores.extend(pelicula["actores"])

    # parseo a set y después a lista para eliminar duplicados
    return list(set(actores))


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
