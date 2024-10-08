from funciones import *
from login import login


def ingresar_genero(generos): 
    print("\n---------------------------------------------------")
    print("¿Qué género te gustaría ver? Aquí te dejo una lista con los géneros disponibles:")
    mostrarMenuNumerado(generos)
    eleccion_genero = int(input('Ingresá el género:'))  

    while eleccion_genero < 1 or eleccion_genero > len(generos):  
        print("El género elegido no está en la lista. Por favor, intenta de nuevo.")
        eleccion_genero = int(input('Ingresá el género: '))  

    eleccion_genero = list(generos)[eleccion_genero-1]
    
    return eleccion_genero


def ingresar_anio(anios):
    #ingresar anio y que sea valido
    eleccion_anio = input("Por favor, ingresa un año: ").strip().lower()
    anio_valido = False     
    while not anio_valido:
        #si es número, que valide que sea año válido
        if eleccion_anio.isdigit():
            if int(eleccion_anio) in anios:
                anio_valido = True
            else:
                leccion_anio = input("Por favor, ingresa una opción válida: ").strip().lower()
        #si ingresa no, año va a ser none
        else:
            eleccion_anio = input("Por favor, ingresa una opción válida: ").strip().lower()
    
    return eleccion_anio


def ingresar_rango_anio(anios):
    #ingresa primer anio y valida
    primer_anio = input("Por favor, ingresá el año de inicio: ")    
    anio_valido = False
    while not anio_valido:
        if primer_anio.isdigit():
            if int(primer_anio) in anios:
                anio_valido = True
            else:
                primer_anio = input("Por favor, ingresa una opción válida: ").strip().lower()
        else:
            primer_anio = input("Por favor, ingresa una opción válida: ").strip().lower()
                    
    #ingresa segundo anio y valida
    anios_siguientes = filtrar_rango_anios(primer_anio, anios[-1], anios)
    print(' - '.join(map(str, anios_siguientes)))
    segundo_anio = input("Por favor, ingresá el año de fin: ")
    anio_valido = False
    while not anio_valido:
        if segundo_anio.isdigit():
            if int(segundo_anio) in anios and int(segundo_anio) >= int(primer_anio):
                anio_valido = True
            else:
                segundo_anio = input("Por favor, ingresa una opción válida: ").strip().lower()
        else:
            segundo_anio = input("Por favor, ingresa una opción válida: ").strip().lower()
            
    #filtrar anios mayor, menor 
    eleccion_anio = filtrar_rango_anios(primer_anio, segundo_anio, anios)      
    
    return eleccion_anio
                    
                        
def ingresar_anio_estreno(anios):
    #ofrece opciones de busqueda de años
    print("-----------------------------------------------------")
    print("¿Te gustaría elegir un año específico de estreno?")
    print(' - '.join(map(str, anios)))
    mostrarMenuNumerado(['Si', 'Prefiero un rango', 'No'])
    modalidad_anio = input().strip().lower()  

    while modalidad_anio not in ('1', '2', '3'):
        modalidad_anio = input("Por favor, ingresa una opción válida: ").strip().lower()   
    
    eleccion_anio = None
    
    if modalidad_anio == '1' or modalidad_anio == '2':
        print("-----------------------------------------------------")
        print('Años de estreno:')
        print(' - '.join(map(str, anios)))
            
        if modalidad_anio == '1':
            eleccion_anio = ingresar_anio(anios)
        elif modalidad_anio == '2':
            eleccion_anio = ingresar_rango_anio(anios)
    
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
    # filtra anio puede ser una lista, un None o un int
    if isinstance(eleccion_anio, list):  
        lista_por_anio = []
        for anio in eleccion_anio:
            lista_por_anio.extend(conseguir_titulos(buscar_por_anio(peliculas, anio)))
    elif eleccion_anio == None:
        lista_por_anio = []
    else:
        lista_por_anio = conseguir_titulos(buscar_por_anio(peliculas, eleccion_anio))
    lista_por_calificacion = conseguir_titulos(buscar_por_calificacion(peliculas, eleccion_calificacion))

    # Completa la matriz de recomendacion peliculas_filtradas
    peliculas_filtradas.append(lista_por_genero)
    peliculas_filtradas.append(lista_por_anio)
    peliculas_filtradas.append(lista_por_calificacion)

    # Recomienda peliculas según coincidencias en la matriz
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

#variable para controlar el flujo del while principal
programa_reinicia = True

if login():
    while programa_reinicia:
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
        
        #reinicio
        print("¿Deseas otra recomendación?")
        respuesta_usuario = input("Ingresá 'si' para volver a tener una recomendación, \n'no' para salir del programa: ").strip().lower()
        
        while respuesta_usuario.lower() not in ('si', 'no'):
            print("Hubo un error en la respuesta.")
            respuesta_usuario = input("Ingresá 'si' para volver a tener una recomendación, \n'no' para salir del programa: ")
            
        if respuesta_usuario.lower() == 'no':
            programa_reinicia = False
            print("¡Gracias por usar nuestro recomendador!")