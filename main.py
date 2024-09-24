from funciones import *
from login import login

def recomendarPelicula(peliculas):

    # Ingresar parámetros de búsqueda 
    generos = conseguir_generos(peliculas)
    anios = conseguir_anios(peliculas)
    calificaciones = conseguir_calificaciones(peliculas)

    ###ingresar genero
    print("¿Qué género te gustaría ver? Aquí te dejo una lista con los géneros disponibles:")
    print(f"{generos}")
    eleccion_genero = input().strip()  # Usa strip() para eliminar espacios en blanco

    while eleccion_genero not in generos:
        print("El género elegido no está en la lista. Por favor, intenta de nuevo.")
        eleccion_genero = input().strip()  # Usa strip() para eliminar espacios en blanco


    ###ingresar año de estreno
    print("¿Te gustaría elegir un año específico de estreno?")
    print(f"Tenemos películas de estos años: {anios}")
    print(f"Si no quisieras ingresar un año escribi : NO")
    eleccion_anio = int(input().strip())  # Usa strip() para eliminar espacios en blanco
 
    while(eleccion_anio not in anios):
        print(" Por favor, ingresa una opcion valida")
        eleccion_anio = int(input().strip())  # Usa strip() para eliminar espacios en blanco


    ###ingresar calificacion
    print("¿Preferís alguna calificación? Seleccioná una de la lista:")
    print(f"{calificaciones}")
    eleccion_calificacion = float(input().strip())  # Usa strip() para eliminar espacios en blanco

    while eleccion_calificacion not in calificaciones:
        print("La calificación no está en la lista. Intenta de nuevo.")
        eleccion_calificacion = input().strip()  # Usa strip() para eliminar espacios en blanco


    # Crea la matriz de recomendación vacía basada en la cantidad de géneros
    matriz = []
    lista_por_genero = conseguir_titulos(buscar_por_genero(peliculas,eleccion_genero))   
    lista_por_anio = conseguir_titulos(buscar_por_anio(peliculas,eleccion_anio))
    lista_por_calificacion = conseguir_titulos(buscar_por_calificacion(peliculas,eleccion_calificacion))
    
    matriz.extend(lista_por_genero, lista_por_anio, lista_por_calificacion)


    # Recomienda películas
    print('Peliculas recomendadas:')
    for i in matriz[0]:
        #si coincide con el año o con la calificación, retorno
        if i in matriz[1] or i in matriz[2]:
            print(i)


def listarPeliculasPorGenero(peliculas):
    generos = conseguir_generos(peliculas)

    for genero in generos:
        peliculas_genero = buscar_por_genero(peliculas, genero)

        print(f'Películas de {genero}:')
        print('--------------------------------')
        mostrar_peliculas(peliculas_genero)


# Cargar las películas desde el archivo JSON
ruta_json = 'peliculas.json'
peliculas = cargar_peliculas(ruta_json)

if login():
    # mostrar menu
    print('CINEMATCH')
    print('1. Pedir recomendación.')
    print('2. Listar todas las películas.')
    opcion_usuario = input('Ingresa la opción que desees: ')

    while opcion_usuario != '1' and opcion_usuario != '2':
        opcion_usuario = input(
            'ERROR, tenés que ingresar 1 o 2. \nIngresa la opción que desees: ')

    if opcion_usuario == '1':
        recomendarPelicula(peliculas)
    elif opcion_usuario == '2':
        listarPeliculasPorGenero(peliculas)
