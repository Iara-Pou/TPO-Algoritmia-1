from funciones import *
from login import login

def mostrarMenuNumerado(opciones):
    opciones_menu = list(opciones)
    for i in range(len(opciones_menu)):
        print(f'{i + 1}. {opciones_menu[i]}')

def recomendarPelicula(peliculas):

    # Ingresar parámetros de búsqueda 
    generos = conseguir_generos(peliculas)
    anios = conseguir_anios(peliculas)
    calificaciones = conseguir_calificaciones(peliculas)

    ###ingresar genero
    print("\n---------------------------------------------------")
    print("¿Qué género te gustaría ver? Aquí te dejo una lista con los géneros disponibles:")
    print(f"{', '.join(generos)}")
    eleccion_genero = input().strip()  

    while eleccion_genero.lower() not in [g.lower() for g in generos]:  
        print("El género elegido no está en la lista. Por favor, intenta de nuevo.")
        eleccion_genero = input().strip()  


    ###ingresar año de estreno
    print("-----------------------------------------------------")
    print("¿Te gustaría elegir un año específico de estreno?")
    print(f"{', '.join(map(str, anios))}")
    print(f"Si no quisieras ingresar un año escribí: NO")
    eleccion_anio = input().strip()  # Validar si el usuario escribe 'NO' sin importar mayúsculas
    if eleccion_anio.lower() == 'no':
        eleccion_anio = None
    else:
        while not eleccion_anio.isdigit() or int(eleccion_anio) not in anios:
            print("Por favor, ingresa una opción válida.")
            eleccion_anio = input().strip()
        eleccion_anio = int(eleccion_anio)

    ### Ingresar calificacion
    print("-----------------------------------------------------")
    print("¿Preferís alguna calificación? Seleccioná una de la lista:")
    print(f"{', '.join(map(str, calificaciones))}")
    print('\n'.join(map(lambda calificacion: f"- {calificacion}", calificaciones)))
    eleccion_calificacion = float(input().strip())  
    while eleccion_calificacion not in calificaciones:
        print("La calificación no está en la lista. Intenta de nuevo.")
        eleccion_calificacion = float(input().strip())

    # Crea la matriz de recomendacion vacia basada en la cantidad de generos
    matriz = []
    lista_por_genero = conseguir_titulos(buscar_por_genero(peliculas, eleccion_genero))
    lista_por_anio = conseguir_titulos(buscar_por_anio(peliculas, eleccion_anio)) if eleccion_anio else []
    lista_por_calificacion = conseguir_titulos(buscar_por_calificacion(peliculas, eleccion_calificacion))

    matriz.append(lista_por_genero)
    matriz.append(lista_por_anio)
    matriz.append(lista_por_calificacion)


    # Recomienda peliculas
    print("\n---------------------------------------------------")
    peliculas_recomendadas = []
    for i in matriz[0]:
        # Si coincide con el año o con la calificacion, retorna
        if i in matriz[1] or i in matriz[2]:
            peliculas_recomendadas.append(i)

    if len(peliculas_recomendadas) != 0:
        for i in peliculas_recomendadas:
            print(f"Tu recomendacion es: {', '.join(peliculas_recomendadas)}")
            print("Esperamos que te guste ;D")
    else:
        print('No se encontraron películas para recomendar.')
    print("\n---------------------------------------------------")


def listarPeliculasPorGenero(peliculas):
    generos = conseguir_generos(peliculas)

    print("\n---------------------------------------------------")
    print(f"Tenemos estos generos disponibles :")
    print(f"{', '.join(generos)}")
    print("\n---------------------------------------------------")
    eleccion_genero = input("Selecciona uno: ")

    while eleccion_genero.lower() not in [g.lower() for g in generos]:  
        print("El género elegido no está en la lista. Por favor, intenta de nuevo.")
        eleccion_genero = input().strip()  

    peliculas_genero = conseguir_titulos(buscar_por_genero(peliculas,eleccion_genero))
    print("\n---------------------------------------------------")
    print(f"Peliculas encontradas: {', '.join(peliculas_genero)}")
    print("\n---------------------------------------------------")

# Cargar las películas desde el archivo JSON
ruta_json = 'peliculas.json'
peliculas = cargar_peliculas(ruta_json)

if login():
    # mostrar menu
    print("\n---------------------------------------------------")
    print('CINEMATCH')
    print("---------------------------------------------------")
    print('1. Pedir recomendación.')
    print('2. Buscar por genero.')
    print("---------------------------------------------------")
    opcion_usuario = input('Ingresa la opción que desees: ')

    while opcion_usuario != '1' and opcion_usuario != '2':
        opcion_usuario = input(
            'ERROR, tenés que ingresar 1 o 2. \nIngresa la opción que desees: ')

    if opcion_usuario == '1':
        recomendarPelicula(peliculas)
    elif opcion_usuario == '2':
        listarPeliculasPorGenero(peliculas)
    print("\n---------------------------------------------------")
