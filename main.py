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

# seleccionar opcion en anios o calificaciones
def seleccionar_opcion(elementos, tipo_elemento):
    
    eleccion_elemento = input(f"Por favor, ingresa un {tipo_elemento}: ").strip()
    elemento_valido = False   
      
    while not elemento_valido:
        
        #si es número, que valide que sea año válido
        if eleccion_elemento.isdigit():
            if int(eleccion_elemento) in elementos:
                elemento_valido = True
                eleccion_elemento = int(eleccion_elemento)
            else:
                eleccion_elemento = input("Por favor, ingresa una opción válida: ").strip()
        else:
            eleccion_elemento = input("Por favor, ingresa una opción válida: ").strip()
            
    return eleccion_elemento


# seleccionar rango en anios o calificaciones
def seleccionar_rango(elementos, tipo_elemento):
    
    # ingresa primer elemento y valida
    eleccion_primer_elemento = input(f"Por favor, ingresá el primer {tipo_elemento}: ")    
    elemento_valido = False

    while not elemento_valido:
        if eleccion_primer_elemento.isdigit():
            if int(eleccion_primer_elemento) in elementos:
                elemento_valido = True
            else:
                eleccion_primer_elemento = input("Por favor, ingresa una opción válida: ").strip()
        else:
            eleccion_primer_elemento = input("Por favor, ingresa una opción válida: ").strip()
                    
    # ingresa segundo elemento y valida
    elementos_siguientes = filtrar_rango_anios(eleccion_primer_elemento, elementos[-1], elementos)
    print(' - '.join(map(str, elementos_siguientes)))

    eleccion_segundo_elemento = input(f"Por favor, ingresá el {tipo_elemento} de fin: ")
    elemento_valido = False
    while not elemento_valido:
        if eleccion_segundo_elemento.isdigit():
            if int(eleccion_segundo_elemento) in elementos and int(eleccion_segundo_elemento) >= int(eleccion_primer_elemento):
                elemento_valido = True
            else:
                eleccion_segundo_elemento = input("Por favor, ingresa una opción válida: ").strip()
        else:
            eleccion_segundo_elemento = input("Por favor, ingresa una opción válida: ").strip()
            
    # filtrar rango elementos por mayor y menor 
    eleccion_elemento = filtrar_rango_anios(int(eleccion_primer_elemento), int(eleccion_segundo_elemento), elementos)      
    
    return eleccion_elemento
                    
                        
def ingresar_anio_estreno(anios):
    
    # Ofrece opciones de busqueda de años
    print("-----------------------------------------------------")
    print("¿Te gustaría elegir un año específico de estreno?")
    print(' - '.join(map(str, anios)))
    mostrarMenuNumerado(['Si', 'Prefiero un rango', 'No'])
    modalidad_anio = input().strip().lower()  

    while modalidad_anio not in ('1', '2', '3'):
        modalidad_anio = input("Por favor, ingresa una opción válida: ").strip().lower()      
    
    if modalidad_anio == '1' or modalidad_anio == '2':
        print("-----------------------------------------------------")
        print('Años de estreno:')
        print(' - '.join(map(str, anios)))
            
        if modalidad_anio == '1':
            eleccion_anio = seleccionar_opcion(anios, 'años')
        elif modalidad_anio == '2':
            eleccion_anio = seleccionar_rango(anios, 'año')

    # Si ingresa 3, devuelve None
    elif modalidad_anio == '3':
        eleccion_anio = None

    
    return eleccion_anio 


def ingresar_calificacion(calificaciones):
    print("-----------------------------------------------------")
    print("¿Preferís alguna calificación?")
    print(' - '.join(map(str, calificaciones)))
    mostrarMenuNumerado(['Si', 'Prefiero un rango'])
    modalidad_calificacion = input().strip().lower()  

    while modalidad_calificacion not in ('1', '2'):
        modalidad_calificacion = input("Por favor, ingresa una opción válida: ").strip().lower()   
      
    if modalidad_calificacion == '1':
        eleccion_calificacion = seleccionar_opcion(calificaciones, 'calificaciones')
    else: 
        eleccion_calificacion = seleccionar_rango(calificaciones, 'calificación')
    
    return eleccion_calificacion 
 

def recomendarPelicula(peliculas):

    ###### Ingresar genero, anio estreno y calificacion
    generos = sorted(conseguir_generos(peliculas))
    anios = sorted(conseguir_anios(peliculas))
    calificaciones = sorted(conseguir_calificaciones(peliculas))

    eleccion_genero = ingresar_genero(generos)
    eleccion_anio = ingresar_anio_estreno(anios)
    eleccion_calificacion = ingresar_calificacion(calificaciones)
    
    
    ###### Crea la matriz de recomendacion peliculas_filtradas
    peliculas_filtradas = []
    
    # Filtra por género, año, calificacion
    lista_por_genero = conseguir_titulos(buscar_por_genero(peliculas, eleccion_genero))   
    # Año puede ser una lista, un None o un int
    if isinstance(eleccion_anio, list):  
        lista_por_anio = []
        for anio in eleccion_anio:
            lista_por_anio.extend(conseguir_titulos(buscar_por_anio(peliculas, anio)))
    elif eleccion_anio == None:
        lista_por_anio = []
    else:
        lista_por_anio = conseguir_titulos(buscar_por_anio(peliculas, eleccion_anio))
    # Calificación puede ser una lista o un int    
    if isinstance(eleccion_calificacion, list):  
        lista_por_calificacion = []
        for calificacion in eleccion_calificacion:
            lista_por_calificacion.extend(conseguir_titulos(buscar_por_calificacion(peliculas, calificacion)))
    else:
        lista_por_calificacion = conseguir_titulos(buscar_por_calificacion(peliculas, eleccion_calificacion))
        
    # Completa la matriz peliculas_filtradas
    peliculas_filtradas.append(lista_por_genero)
    peliculas_filtradas.append(lista_por_anio)
    peliculas_filtradas.append(lista_por_calificacion)
        
        
    ####### Recomienda películas según coincidencias en peliculas_filtradas
    print("\n---------------------------------------------------")
    peliculas_recomendadas = []
    
    # Si hay coincidencia entre los tres filtros, recomendar película
    for pelicula in peliculas_filtradas[0]:
        # También debe coincidir en año o calificación  
        if pelicula in peliculas_filtradas[1] or pelicula in peliculas_filtradas[2]:              
            peliculas_recomendadas.append(pelicula)
    
    # Si hay películas, las muestra
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
reinicio = True

if login():
    
    while reinicio:
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
