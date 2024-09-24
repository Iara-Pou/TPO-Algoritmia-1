### README

#### 1. Análisis del archivo `funciones.py`

Este archivo contiene las funciones auxiliares que se utilizan para filtrar y manejar las películas. Estas funciones permiten buscar películas basadas en diferentes criterios, cargar datos desde un archivo JSON y procesar la información.

- **`similar(a, b)`**: 
  - **Propósito**: Compara dos strings y devuelve una medida de similitud.
  - **Parámetros**: 
    - `a` (str): Primer string.
    - `b` (str): Segundo string.
  - **Salida**: Un número flotante entre 0 y 1 que indica cuán similares son los dos strings.

- **`buscar_por_descripcion(peliculas, palabras_clave)`**:
  - **Propósito**: Busca películas cuya descripción tenga coincidencias aproximadas con las palabras clave proporcionadas.
  - **Parámetros**: 
    - `peliculas` (list): Lista de películas.
    - `palabras_clave` (str): Palabras clave que se buscan en las descripciones.
  - **Salida**: Lista de películas con coincidencias en la descripción.

- **`cargar_peliculas(ruta_archivo)`**:
  - **Propósito**: Cargar las películas desde un archivo JSON.
  - **Parámetros**:
    - `ruta_archivo` (str): Ruta del archivo JSON.
  - **Salida**: Una lista de diccionarios con información de cada película.

- **`buscar_por_genero(peliculas, genero)`**:
  - **Propósito**: Filtrar películas por género.
  - **Parámetros**:
    - `peliculas` (list): Lista de películas.
    - `genero` (str): Género seleccionado.
  - **Salida**: Lista de películas que pertenecen al género seleccionado.

- **`buscar_por_anio(peliculas, anio)`**:
  - **Propósito**: Filtrar películas por año.
  - **Parámetros**:
    - `peliculas` (list): Lista de películas.
    - `anio` (int): Año seleccionado.
  - **Salida**: Lista de películas lanzadas en el año seleccionado.

- **`buscar_por_calificacion(peliculas, calificacion)`**:
  - **Propósito**: Filtrar películas por calificación.
  - **Parámetros**:
    - `peliculas` (list): Lista de películas.
    - `calificacion` (float): Calificación seleccionada.
  - **Salida**: Lista de películas con la calificación seleccionada.

- **`mostrar_peliculas(peliculas)`**:
  - **Propósito**: Mostrar la información completa de las películas.
  - **Parámetros**:
    - `peliculas` (list): Lista de películas.
  - **Salida**: Información impresa de cada película.

- **`conseguir_generos(peliculas)`**:
  - **Propósito**: Obtener una lista de géneros disponibles.
  - **Parámetros**:
    - `peliculas` (list): Lista de películas.
  - **Salida**: Un conjunto de géneros.

- **`conseguir_anios(peliculas)`**:
  - **Propósito**: Obtener una lista de años de estreno disponibles.
  - **Parámetros**:
    - `peliculas` (list): Lista de películas.
  - **Salida**: Un conjunto de años.

- **`conseguir_calificaciones(peliculas)`**:
  - **Propósito**: Obtener una lista de calificaciones disponibles.
  - **Parámetros**:
    - `peliculas` (list): Lista de películas.
  - **Salida**: Un conjunto de calificaciones.

- **`conseguir_titulos(peliculas)`**:
  - **Propósito**: Obtener una lista de títulos de películas.
  - **Parámetros**:
    - `peliculas` (list): Lista de películas.
  - **Salida**: Un conjunto de títulos.

---

#### 2. Análisis del archivo `main.py`

Este archivo contiene el flujo principal del programa, encargándose de la interacción con el usuario, la elección de opciones, y la lógica de recomendación de películas.

- **`recomendarPelicula(peliculas)`**:
  - **Propósito**: Filtrar películas por género, año y calificación, y mostrar las recomendaciones.
  - **Entradas**: 
    - Lista de películas.
  - **Flujo**:
    1. Se solicitan los géneros, años y calificaciones disponibles.
    2. El usuario selecciona un género, año y calificación.
    3. Se genera una matriz con películas filtradas por cada criterio.
    4. Se muestran las películas que coinciden con al menos dos de los criterios.
  - **Salidas**: Películas recomendadas impresas en consola.

- **`listarPeliculasPorGenero(peliculas)`**:
  - **Propósito**: Mostrar las películas disponibles de un género específico.
  - **Entradas**: 
    - Lista de películas.
  - **Flujo**:
    1. Se muestra una lista de géneros disponibles.
    2. El usuario selecciona un género.
    3. Se muestran los títulos de las películas del género seleccionado.
  - **Salidas**: Películas filtradas por género impresas en consola.

- **Lógica de menú principal**:
  - Al iniciar, se cargan las películas desde el archivo `peliculas.json`.
  - El programa solicita el inicio de sesión mediante la función `login()`.
  - Después del login exitoso, el usuario puede elegir entre:
    1. Recibir una recomendación de películas.
    2. Listar las películas por género.
  - Según la opción seleccionada, se llama a la función correspondiente.

---

#### 3. Análisis del archivo `peliculas.json`

El archivo `peliculas.json` contiene la base de datos de las películas en formato JSON, con varios atributos como título, género, calificación, año, actores y descripción.

- **Formato de las películas**:
  Cada película es un diccionario con las siguientes claves:
  - `titulo`: El nombre de la película.
  - `genero`: El género al que pertenece.
  - `calificacion`: La calificación en una escala de 1 a 10.
  - `anio`: El año en que fue lanzada.
  - `actores`: Lista de actores que participaron.
  - `descripcion`: Una breve descripción del argumento.

Este archivo es esencial para la ejecución del programa, ya que todos los filtros y recomendaciones se basan en los datos almacenados aquí.

