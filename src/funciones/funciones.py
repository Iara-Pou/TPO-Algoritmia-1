import json
import  tkinter 
from tkinter import ttk
from io import BytesIO

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
    ventana = tkinter.Tk()
    ventana.title("Películas")

    # Configuración de estilo
    style = ttk.Style()
    style.configure("TLabel", wraplength=400, justify="left", font=("Arial", 12))

    # Configurar la ventana para que se ajuste al tamaño de la pantalla
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight=1)

    # Contenedor principal con scrollbar
    contenedor_principal = ttk.Frame(ventana)
    contenedor_principal.grid(column=0, row=0, sticky="nsew")

    # Canvas para permitir el scroll
    canvas = tkinter.Canvas(contenedor_principal)
    canvas.grid(column=0, row=0, sticky="nsew")

    # Scrollbar vertical
    scrollbar = ttk.Scrollbar(contenedor_principal, orient="vertical", command=canvas.yview)
    scrollbar.grid(column=1, row=0, sticky="ns")

    # Configurar el canvas para usar la scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame dentro del canvas
    contenedor = ttk.Frame(canvas)

    # Crear el contenido del frame
    for i, p in enumerate(peliculas):
        frame_pelicula = ttk.Frame(contenedor, padding=5)
        frame_pelicula.grid(column=0, row=i, sticky="ew", pady=10)

        # Mostrar la información
        titulo = ttk.Label(frame_pelicula, text=f"Título: {p['titulo']}", font=("Arial", 14, "bold"))
        titulo.grid(column=0, row=0, sticky="w")

        genero = ttk.Label(frame_pelicula, text=f"Género: {p['genero']}")
        genero.grid(column=0, row=1, sticky="w")

        calificacion = ttk.Label(frame_pelicula, text=f"Calificación: {p['calificacion']}")
        calificacion.grid(column=0, row=2, sticky="w")

        anio = ttk.Label(frame_pelicula, text=f"Año: {p['anio']}")
        anio.grid(column=0, row=3, sticky="w")

        actores = ttk.Label(frame_pelicula, text=f"Actores: {', '.join(p['actores'])}")
        actores.grid(column=0, row=4, sticky="w")

        descripcion = ttk.Label(frame_pelicula, text=f"Descripción: {p['descripcion']}")
        descripcion.grid(column=0, row=5, sticky="w")

    # Añadir el frame al canvas
    canvas.create_window((0, 0), window=contenedor, anchor="nw")

    # Ajustar el tamaño del canvas al contenido
    contenedor.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Configurar el contenedor principal para expandirse con la ventana
    contenedor_principal.columnconfigure(0, weight=1)
    contenedor_principal.rowconfigure(0, weight=1)

    ventana.mainloop()


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
