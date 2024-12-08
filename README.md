# CINEMATCH - Recomendador de Películas

Este programa es un recomendador de películas basado en criterios específicos como género, rango de años o una breve descripción. El flujo principal del código empieza con la autenticación del usuario, que da acceso a las funcionalidades. Las películas se cargan desde un archivo JSON, y luego el usuario puede elegir entre obtener recomendaciones o listar películas por género. La interacción se gestiona a través de un menú.

El código se divide en funciones que están organizadas para facilitar la modularidad y la claridad, siendo reutilizables y fácilmente ampliables. Además, el uso de archivos JSON para almacenar los datos permite una separación entre lógica y datos.

## Estructura del Proyecto

### Archivos y Módulos

- `main.py`: Archivo principal que contiene el flujo principal del programa.
- `src/funciones/funciones.py`: Contiene funciones auxiliares para procesamiento y manejo de datos.
- `src/funciones/test_funciones.py`: Archivo para pruebas unitarias de las funciones del sistema.
- `src/login.py`: Maneja la autenticación de usuarios.
- `src/agregarPelicula.py`: Proporciona la funcionalidad para agregar nuevas películas.
- `src/manejarSesion.py`: Contiene funciones relacionadas con el manejo de sesión de usuarios y registros de eventos.
- `src/buscarPeliculas.py`: Contiene funciones para filtrar, buscar y listar películas por distintos criterios.
- `data/logEjecucion.txt`: Archivo de texto donde se registran los logs de ejecución del sistema.
- `data/peliculas.json`: Archivo JSON que almacena los datos de las películas.
- `data/usuarios.txt`: Archivo que almacena los usuarios registrados junto con sus contraseñas y roles.

## Funcionalidades Principales

### 1. **Recomendación de Películas**

Permite al usuario seleccionar un género, año (o rango de años) y calificaciones para recibir recomendaciones personalizadas.

### 2. **Búsqueda por Género**

Permite al usuario listar todas las películas de un género específico.

### 3. **Agregar Películas (Admin)**

Los usuarios con rol de administrador pueden agregar nuevas películas al sistema.

### 4. **Gestión de Usuarios**

#### **Inicio de Sesión**

El sistema autentica a los usuarios al inicio del programa para determinar si tienen acceso a funcionalidades adicionales como la de agregar películas.

#### **Registro de Nuevos Usuarios**

Permite agregar nuevos usuarios al sistema de manera interactiva, validando que el nombre de usuario no esté en uso.

### 5. **Filtrado y Búsqueda Avanzada**

Permite buscar películas por:

- Género
- Año de estreno o rango de años
- Calificación
- Título
- Actores

## Flujo Principal

El programa se ejecuta a través de `main.py`:

1. Carga las películas desde `data/peliculas.json`.
2. Solicita al usuario que inicie sesión.
3. Presenta un menú interactivo con las siguientes opciones:
   - Pedir recomendación.
   - Buscar por género.
   - Agregar película (solo para administradores).
   - Salir del programa.
4. Maneja la interacción con el usuario según las opciones seleccionadas.

## Detalles de las Funciones

### **ingresar_genero(generos)**

Permite al usuario seleccionar un género de una lista disponible. Si el usuario ingresa `-1`, se cancela el proceso.

### **seleccionar_opcion(elementos, tipo_elemento)**

Permite seleccionar un elemento específico (como un género, año, o calificación) de una lista.

### **seleccionar_rango(elementos, tipo_elemento)**

Permite seleccionar un rango de valores (como años o calificaciones).

### **ingresar_anio_estreno(anios)**

Permite seleccionar un año específico o un rango de años.

### **ingresar_calificacion(calificaciones)**

Permite seleccionar una calificación específica o un rango de calificaciones.

### **recomendar_pelicula(peliculas)**

Genera una lista de recomendaciones basada en los filtros seleccionados por el usuario.

### **listar_peliculas_por_genero(peliculas)**

Lista todas las películas disponibles en un género específico.

### **usuario_es_admin()**

Verifica si el usuario autenticado es un administrador.

### **cargarUsuariosDesdeArchivo()**

Carga los usuarios registrados desde el archivo `data/usuarios.txt`.

### **nombreEnUso(usuarios, nombre_usuario)**

Verifica si un nombre de usuario ya está registrado.

### **agregarUsuarioAArchivo(nombre_usuario, contrasenia_usuario, rol_usuario)**

Agrega un nuevo usuario al archivo de usuarios, validando previamente que el nombre no esté en uso.

### **login()**

Maneja el flujo de inicio de sesión e intenta autenticar a un usuario o permite agregar un nuevo usuario.

### **filtrarRangoAnios(anio_inicio, anio_fin, anios)**

Filtra un rango de años a partir de una lista dada.

### **cargarPeliculas(ruta_archivo)**

Carga las películas desde un archivo JSON. Maneja excepciones relacionadas con archivos no encontrados o datos inválidos.

### **buscarPorGenero(peliculas, genero)**

Busca películas por género.

### **buscarPorAnio(peliculas, anio)**

Busca películas por año de estreno.

### **buscarPorCalificacion(peliculas, calificacion)**

Busca películas por calificación.

### **buscarPorTitulo(peliculas, titulo)**

Busca una película específica por su título.

### **mostrarPeliculas(peliculas)**

Imprime una lista de películas con su información detallada.

### **conseguirGeneros(peliculas)**

Obtiene un conjunto único de géneros presentes en la lista de películas.

### **conseguirAnios(peliculas)**

Obtiene un conjunto único de años presentes en la lista de películas.

### **conseguirCalificaciones(peliculas)**

Obtiene un conjunto único de calificaciones presentes en la lista de películas.

### **conseguirTitulos(peliculas)**

Obtiene un conjunto único de títulos presentes en la lista de películas de manera recursiva.

### **conseguirActores(peliculas)**

Obtiene una lista única de actores presentes en la lista de películas.

### **mostrarMenuNumerado(opciones)**

Muestra un menú numerado para facilitar la selección interactiva.

### **listaEstaVacia(lista)**

Verifica si una lista está vacía.

### **cancelarCarga()**

Imprime un mensaje de cancelación y retorna un valor de error (-1).

## Manejo de Errores

El sistema registra errores y excepciones en archivos de log utilizando las funciones `loguearError` y `loguearExcepcion` del módulo `manejarSesion.py`.

## Notas Adicionales

- Si el archivo `data/peliculas.json` no está presente o contiene datos inválidos, el programa no podrá iniciar correctamente.
- Los usuarios deben ingresar datos según las opciones disponibles para evitar errores.

---

**Autor:** Los imaginadores
