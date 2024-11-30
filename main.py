from funciones import *
from login import login
from agregarPelicula import agregar_pelicula

def ingresar_genero(generos): 
    print("\n---------------------------------------------------")
    print('IMPORTANTE || Por favor, ingresá -1 en cualquier momento de la carga para cancelar el proceso.')
    print("¿Qué género te gustaría ver? Aquí te dejo una lista con los géneros disponibles:")
    mostrarMenuNumerado(generos)
    
    while True:
        try:
            eleccion_genero = int(input('Ingresá el género: '))  
            while eleccion_genero < 1 or eleccion_genero > len(generos):  
                if eleccion_genero == -1: return -1
                print("El género elegido no está en la lista. Por favor, intenta de nuevo.")
                eleccion_genero = int(input('Ingresá el género: '))  
            return list(generos)[eleccion_genero-1]
        except ValueError:
            print('Debes ingresar un número. ')

def seleccionar_opcion(elementos, tipo_elemento):
    eleccion = input(f"Por favor, ingresa un/una {tipo_elemento}: ").strip()
    while True:
        if eleccion == "-1": return -1
        if eleccion.isdigit() and int(eleccion) in elementos:
            return int(eleccion)
        eleccion = input(f"Por favor, ingresa un/una {tipo_elemento} válido/a: ").strip()

def seleccionar_rango(elementos, tipo_elemento):
    primer_elemento = seleccionar_opcion(elementos, f"primer {tipo_elemento}")
    if primer_elemento == -1: return -1

    elementos_siguientes = filtrar_rango_anios(primer_elemento, elementos[-1], elementos)
    print(' - '.join(map(str, elementos_siguientes)))

    segundo_elemento = seleccionar_opcion(elementos, f"{tipo_elemento} de fin")
    if segundo_elemento == -1: return -1

    if segundo_elemento >= primer_elemento:
        return filtrar_rango_anios(primer_elemento, segundo_elemento, elementos)
    else:
        #si no ingresó un rango válido, vuelve a llamar a la funcion para que lo haga
        print("El rango no es válido. Intenta nuevamente.")
        print("-----------------------------------------------------")
        print(' - '.join(map(str, elementos)))

        return seleccionar_rango(elementos, tipo_elemento)

def ingresar_anio_estreno(anios):
    print("-----------------------------------------------------")
    print("¿Te gustaría elegir un año específico de estreno?")
    print(' - '.join(map(str, anios)))
    mostrarMenuNumerado(['Sí', 'Prefiero un rango', 'No'])
    modalidad = input().strip()

    while modalidad not in ('1', '2', '3'):
        modalidad = input("Por favor, ingresa una opción válida: ").strip()

    if modalidad == '1':
        return seleccionar_opcion(anios, 'año')
    elif modalidad == '2':
        return seleccionar_rango(anios, 'año')
    return None

def ingresar_calificacion(calificaciones):
    print("-----------------------------------------------------")
    print("¿Preferís alguna calificación?")
    print(' - '.join(map(str, calificaciones)))
    mostrarMenuNumerado(['Sí', 'Prefiero un rango', 'No'])
    modalidad = input().strip()

    while modalidad not in ('1', '2', '3'):
        modalidad = input("Por favor, ingresa una opción válida: ").strip()

    if modalidad == '1':
        return seleccionar_opcion(calificaciones, 'calificación')
    elif modalidad == '2':
        return seleccionar_rango(calificaciones, 'calificación')
    return None

def recomendar_pelicula(peliculas):
    generos = sorted(conseguir_generos(peliculas))
    anios = sorted(conseguir_anios(peliculas))
    calificaciones = sorted(conseguir_calificaciones(peliculas))

    eleccion_genero = ingresar_genero(generos)
    if eleccion_genero == -1: return
    eleccion_anio = ingresar_anio_estreno(anios)
    if eleccion_anio == -1: return
    eleccion_calificacion = ingresar_calificacion(calificaciones)
    if eleccion_calificacion == -1: return

    peliculas_filtradas = []
    lista_por_genero = conseguir_titulos(buscar_por_genero(peliculas, eleccion_genero))
    lista_por_anio = []
    lista_por_calificacion = []

    if isinstance(eleccion_anio, list):
        for anio in eleccion_anio:
            lista_por_anio.extend(conseguir_titulos(buscar_por_anio(peliculas, anio)))
    elif eleccion_anio is not None:
        lista_por_anio = conseguir_titulos(buscar_por_anio(peliculas, eleccion_anio))

    if isinstance(eleccion_calificacion, list):
        for calificacion in eleccion_calificacion:
            lista_por_calificacion.extend(conseguir_titulos(buscar_por_calificacion(peliculas, calificacion)))
    elif eleccion_calificacion is not None:
        lista_por_calificacion = conseguir_titulos(buscar_por_calificacion(peliculas, eleccion_calificacion))

    # arma matriz de películas filtradas por parámetros anteriores
    peliculas_filtradas = [lista_por_genero, lista_por_anio, lista_por_calificacion]
    peliculas_recomendadas = []
    
    ### GENERA LISTA DE PELÍCULAS RECOMENDADAS
    # si la película tiene el genero y el año o el género y la calificación, la almacena como una película a recomendar
    if listaEstaVacia(lista_por_anio) and listaEstaVacia(lista_por_calificacion):
        peliculas_recomendadas = lista_por_genero
    else:
        for pelicula in peliculas_filtradas[0]:
            if pelicula in peliculas_filtradas[1] or pelicula in peliculas_filtradas[2]:
                peliculas_recomendadas.append(pelicula)

    if peliculas_recomendadas:
        informacion_peliculas = [buscar_por_titulo(peliculas, titulo) for titulo in peliculas_recomendadas if buscar_por_titulo(peliculas, titulo)]
        print("Te recomendamos:\n")
        mostrar_peliculas(informacion_peliculas)
        print("\nEsperamos que te gusten ;D")
    else:
        print('No se encontraron películas para recomendar.')
    print("\n---------------------------------------------------")

def listar_peliculas_por_genero(peliculas):
    generos = sorted(conseguir_generos(peliculas))
    eleccion_genero = ingresar_genero(generos)
    if eleccion_genero == -1: return
    print("\n---------------------------------------------------")
    print("Películas encontradas:\n")
    mostrar_peliculas(buscar_por_genero(peliculas, eleccion_genero))
    print("\n---------------------------------------------------")

# Flujo principal del programa
ruta_json = 'peliculas.json'
peliculas = cargar_peliculas(ruta_json)

if login():
    continuar = True
    while continuar:
        print("\n---------------------------------------------------")
        print('CINEMATCH')
        print("---------------------------------------------------")
        print('1. Pedir recomendación.')
        print('2. Buscar por género.')
        print('3. Agregar película.')
        print('4. Salir del programa.')
        print("---------------------------------------------------")
        opcion = input('Ingresa la opción que desees: ').strip()

        while opcion not in ('1', '2', '3', '4'):
            opcion = input("ERROR: Por favor, ingresá 1, 2, 3 o 4: ").strip()

        if opcion == '1':
            recomendar_pelicula(peliculas)
        elif opcion == '2':
            listar_peliculas_por_genero(peliculas)
        elif opcion == '3':
            resultado = agregar_pelicula()
            if resultado is not None:
                peliculas = resultado
        elif opcion == '4':
            continuar = False
            print("¡Gracias por usar nuestro recomendador!")
