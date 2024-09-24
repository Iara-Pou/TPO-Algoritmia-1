from funciones import *
from login import login


def recomendarPelicula(peliculas):
    # Opciones del usuario
    print("Opciones de búsqueda:")
    print("1. Buscar por género")
    print("2. Buscar por rango de años")
    print("3. Buscar por descripción")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        genero = input("Introduce el género: ")
        resultado = buscar_por_genero(peliculas, genero)
    elif opcion == 2:
        anio_inicio = int(input("Introduce el año de inicio: "))
        anio_fin = int(input("Introduce el año final: "))
        resultado = buscar_por_anio(peliculas, anio_inicio, anio_fin)
    elif opcion == 3:
        palabras_clave = input(
            "Introduce una breve descripción o palabras clave: ")
        resultado = buscar_por_descripcion(peliculas, palabras_clave)

    # Mostrar los resultados
    if resultado:
        mostrar_peliculas(resultado)
    else:
        print("No se encontraron películas que coincidan con la búsqueda.")


def listarPeliculasPorGenero(peliculas):
    generos = conseguir_generos(peliculas)

    for genero in generos:
        peliculas_genero = buscar_por_genero(peliculas, genero)

        print(f'Películas de {genero}:')
        print('--------------------------------')
        mostrar_peliculas(peliculas_genero)


ruta_json = 'peliculas.json'
peliculas = cargar_peliculas(ruta_json)

if login():
    # mostrar menu
    print('CINEMATCH')
    print('1. Pedir recomendación.')
    print('2. Mostrar películas por género.')
    opcion_usuario = input('Ingresa la opción que desees: ')

    while opcion_usuario != '1' and opcion_usuario != '2':
        opcion_usuario = input(
            'ERROR, tenés que ingresar 1 o 2. \nIngresa la opción que desees: ')

    if opcion_usuario == '1':
        recomendarPelicula(peliculas)
    elif opcion_usuario == '2':
        listarPeliculasPorGenero(peliculas)
