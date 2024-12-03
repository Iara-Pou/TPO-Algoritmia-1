
from src.funciones.funciones import (
    filtrar_rango_anios,
    buscar_por_genero,
    buscar_por_anio,
    buscar_por_calificacion,
    buscar_por_titulo,
    conseguir_generos,
    conseguir_anios,
    conseguir_calificaciones,
    conseguir_titulos
)

#  datos de películas para probar
peliculas_prueba = [
    {
        "titulo": "Pelicula 1",
        "genero": "Acción",
        "calificacion": 8,
        "anio": 2020,
        "actores": ["Actor 1", "Actor 2"],
        "descripcion": "Una película de acción emocionante."
    },
    {
        "titulo": "Pelicula 2",
        "genero": "Comedia",
        "calificacion": 7,
        "anio": 2018,
        "actores": ["Actor 3", "Actor 4"],
        "descripcion": "Una comedia divertida."
    },
    {
        "titulo": "Pelicula 3",
        "genero": "Drama",
        "calificacion": 9,
        "anio": 2022,
        "actores": ["Actor 5", "Actor 6"],
        "descripcion": "Un drama conmovedor."
    }
]

# Pruebas para `filtrar_rango_anios`
def test_filtrar_rango_anios():
    anios = [2015, 2018, 2020, 2022, 2025]
    resultado = filtrar_rango_anios(2018, 2022, anios)
    assert resultado == [2018, 2020, 2022]

def test_filtrar_rango_anios_fuera_rango():
    anios = [2015, 2018, 2020, 2022, 2025]
    resultado = filtrar_rango_anios(2030, 2040, anios)
    assert resultado == []

# Pruebas para `buscar_por_genero`
def test_buscar_por_genero():
    resultado = buscar_por_genero(peliculas_prueba, "Acción")
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Pelicula 1"

def test_buscar_por_genero_sin_coincidencias():
    resultado = buscar_por_genero(peliculas_prueba, "Ciencia ficción")
    assert resultado == []

# Pruebas para `buscar_por_anio`
def test_buscar_por_anio():
    resultado = buscar_por_anio(peliculas_prueba, 2020)
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Pelicula 1"

def test_buscar_por_anio_sin_coincidencias():
    resultado = buscar_por_anio(peliculas_prueba, 2000)
    assert resultado == []

# Pruebas para `buscar_por_calificacion`
def test_buscar_por_calificacion():
    resultado = buscar_por_calificacion(peliculas_prueba, 9)
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Pelicula 3"

def test_buscar_por_calificacion_sin_coincidencias():
    resultado = buscar_por_calificacion(peliculas_prueba, 10)
    assert resultado == []

# Pruebas para `buscar_por_titulo`
def test_buscar_por_titulo():
    resultado = buscar_por_titulo(peliculas_prueba, "Pelicula 2")
    assert resultado["titulo"] == "Pelicula 2"
    assert resultado["genero"] == "Comedia"

def test_buscar_por_titulo_sin_coincidencias():
    resultado = buscar_por_titulo(peliculas_prueba, "Pelicula inexistente")
    assert resultado is None

# Pruebas para `conseguir_generos`
def test_conseguir_generos():
    resultado = conseguir_generos(peliculas_prueba)
    assert resultado == {"Acción", "Comedia", "Drama"}

# Pruebas para `conseguir_anios`
def test_conseguir_anios():
    resultado = conseguir_anios(peliculas_prueba)
    assert resultado == {2020, 2018, 2022}

# Pruebas para `conseguir_calificaciones`
def test_conseguir_calificaciones():
    resultado = conseguir_calificaciones(peliculas_prueba)
    assert resultado == {8, 7, 9}

# Pruebas para `conseguir_titulos`
def test_conseguir_titulos():
    resultado = conseguir_titulos(peliculas_prueba)
    assert resultado == {"Pelicula 1", "Pelicula 2", "Pelicula 3"}