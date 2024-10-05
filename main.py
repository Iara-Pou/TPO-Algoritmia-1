from funciones import *
from login import login

def ingresar_genero(generos): 
    print("\n---------------------------------------------------")
    print("¿Qué género te gustaría ver? Aquí te dejo una lista con los géneros disponibles:")
    mostrarMenuNumerado(generos)
    eleccion_genero = int(input('Ingresá el género:'))  

    while eleccion_genero < 1 or eleccion_genero > len(generos):  
        print("El género elegido no está en la lista. Por favor, intenta de nuevo.")
        eleccion_genero = int(input('Ingresá el género:'))  

    eleccion_genero = list(generos)[eleccion_genero-1]
    
    return eleccion_genero
    
    
def ingresar_anio_estreno(anios):
    print("-----------------------------------------------------")
    print("¿Te gustaría elegir un año específico de estreno?")
    print(' - '.join(map(str, anios)))
    print(f"Si no quisieras ingresar un año escribí: NO")
    eleccion_anio = input().strip()  # Validar si el usuario escribe 'NO' sin importar mayúsculas
    if eleccion_anio.lower() == 'no':
        eleccion_anio = None
    else:
        while not eleccion_anio.isdigit() or int(eleccion_anio) not in anios:
            print("Por favor, ingresa una opción válida.")
            eleccion_anio = input().strip()
        eleccion_anio = int(eleccion_anio)
    
    return eleccion_anio


def ingresar_calificacion(calificaciones):
    print("-----------------------------------------------------")
    print("¿Preferís alguna calificación? Seleccioná una de la lista:")
    print(' - '.join(map(str, calificaciones)))
    eleccion_calificacion = int(input().strip())  
    while eleccion_calificacion not in calificaciones:
        print("La calificación no está en la lista. Intenta de nuevo.")
        eleccion_calificacion = int(input().strip())
        
    return eleccion_calificacion
 

def recomendarPelicula(peliculas):
    # Ingresar parámetros de búsqueda y los ordena 
    generos = sorted(conseguir_generos(peliculas))
    anios = sorted(conseguir_anios(peliculas))
    calificaciones = sorted(conseguir_calificaciones(peliculas))

    # Ingresar genero, anio estreno y calificacion
    eleccion_genero = ingresar_genero(generos)
    eleccion_anio = ingresar_anio_estreno(anios)
    eleccion_calificacion = ingresar_calificacion(calificaciones)

    # Crea la matriz de recomendacion peliculas_filtradas
    peliculas_filtradas = []
    lista_por_genero = conseguir_titulos(buscar_por_genero(peliculas, eleccion_genero))
    lista_por_anio = conseguir_titulos(buscar_por_anio(peliculas, eleccion_anio)) if eleccion_anio else []
    lista_por_calificacion = conseguir_titulos(buscar_por_calificacion(peliculas, eleccion_calificacion))

    peliculas_filtradas.append(lista_por_genero)
    peliculas_filtradas.append(lista_por_anio)
    peliculas_filtradas.append(lista_por_calificacion)

    # Recomienda peliculas
    print("\n---------------------------------------------------")
    peliculas_recomendadas = []
    for i in peliculas_filtradas[0]:
        # Si coincide con el año o con la calificacion, retorna
        if i in peliculas_filtradas[1] or i in peliculas_filtradas[2]:
            peliculas_recomendadas.append(i)

    if len(peliculas_recomendadas) != 0:
        informacion_peliculas = []
        # Busca la información completa de cada película recomendada
        for titulo in peliculas_recomendadas:
            info = buscar_por_titulo(peliculas, titulo)
            if info:
                informacion_peliculas.append(info)
        print("Te recomendamos: \n")
        mostrar_peliculas(informacion_peliculas)
        print("\nEsperamos que te gusten ;D")
        
    else:
        print('No se encontraron películas para recomendar.')
    print("\n---------------------------------------------------")


def listarPeliculasPorGenero(peliculas):

    generos = sorted(conseguir_generos(peliculas))
    eleccion_genero = ingresar_genero(generos)
    
    print("\n---------------------------------------------------")
    print("Peliculas encontradas:\n")
    peliculas_genero = mostrar_peliculas(buscar_por_genero(peliculas, eleccion_genero))
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
