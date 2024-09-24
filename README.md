# TPO Algoritmia 1
 ### Análisis General del Proyecto
Este programa es un recomendador de películas basado en criterios específicos como género, rango de años o una breve descripción. El flujo principal del código empieza con la autenticación del usuario, que da acceso a las funcionalidades. Las películas se cargan desde un archivo JSON, y luego el usuario puede elegir entre obtener recomendaciones o listar películas por género. La interacción se gestiona a través de un menú.

El código se divide en funciones que están organizadas para facilitar la modularidad y la claridad, siendo reutilizables y fácilmente ampliables. Además, el uso de archivos JSON para almacenar los datos permite una separación entre lógica y datos.


### Documentacion detallada

#### `main.py`
1. **recomendarPelicula(peliculas)**
   - **Parámetros**: `peliculas` (lista de diccionarios con información de películas).
   - **Entrada**: Elige una opción de búsqueda (género, rango de años, descripción) e ingresa los valores correspondientes.
   - **Salida**: Muestra las películas que cumplen con los criterios elegidos.
   - **Descripción**: Esta función permite recomendar películas al usuario basado en tres criterios de búsqueda: género, rango de años y palabras clave en la descripción.

2. **listarPeliculasPorGenero(peliculas)**
   - **Parámetros**: `peliculas` (lista de películas).
   - **Entrada**: Ninguna entrada adicional, simplemente muestra todas las películas cargadas.
   - **Salida**: Lista las películas por género.
   - **Descripción**: Muestra todas las películas almacenadas en el archivo JSON.

3. **login()**
   - **Parámetros**: Ninguno.
   - **Entrada**: Solicita el nombre de usuario y contraseña.
   - **Salida**: Devuelve `True` si el login es exitoso, `False` en caso contrario.
   - **Descripción**: Valida las credenciales del usuario. Si el login es exitoso, permite acceder a las funcionalidades del programa.

#### `funciones.py`
1. **similar(a, b)**
   - **Parámetros**: `a` (cadena de texto), `b` (cadena de texto).
   - **Entrada**: Dos cadenas de texto a comparar.
   - **Salida**: Un valor de similitud entre 0 y 1.
   - **Descripción**: Calcula la similitud entre dos cadenas utilizando el módulo `SequenceMatcher`.

2. **buscar_por_descripcion(peliculas, palabras_clave)**
   - **Parámetros**: `peliculas` (lista de películas), `palabras_clave` (texto ingresado por el usuario).
   - **Entrada**: Descripción o palabras clave.
   - **Salida**: Lista de películas que coinciden parcialmente con las palabras clave.
   - **Descripción**: Filtra las películas que contienen coincidencias aproximadas con las palabras clave en su descripción.

3. **cargar_peliculas(ruta_archivo)**
   - **Parámetros**: `ruta_archivo` (ruta al archivo JSON).
   - **Entrada**: Ninguna entrada adicional.
   - **Salida**: Carga y devuelve una lista de películas desde el archivo JSON.
   - **Descripción**: Lee un archivo JSON y retorna la lista de películas contenida en él.

4. **buscar_por_genero(peliculas, genero)**
   - **Parámetros**: `peliculas` (lista de películas), `genero` (texto ingresado por el usuario).
   - **Entrada**: Género de película.
   - **Salida**: Lista de películas que coinciden con el género.
   - **Descripción**: Busca y filtra las películas que coinciden exactamente con el género proporcionado.

5. **buscar_por_anio(peliculas, anio_inicio, anio_fin)**
   - **Parámetros**: `peliculas` (lista de películas), `anio_inicio` (número entero), `anio_fin` (número entero).
   - **Entrada**: Rango de años.
   - **Salida**: Lista de películas que fueron lanzadas dentro del rango especificado.
   - **Descripción**: Filtra películas dentro de un rango de años dado.

6. **mostrar_peliculas(peliculas)**
   - **Parámetros**: `peliculas` (lista de películas).
   - **Entrada**: Ninguna entrada adicional.
   - **Salida**: Muestra información detallada de las películas.
   - **Descripción**: Imprime el título, género, calificación, año y actores de cada película.
