from funciones import cargar_peliculas, buscar_por_genero, buscar_por_anio, mostrar_peliculas, buscar_por_descripcion

# Cargar las películas desde el archivo JSON
ruta_json = 'peliculas.json'
peliculas = cargar_peliculas(ruta_json)

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
