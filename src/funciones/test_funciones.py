
from src.funciones.funciones import (
    filtrarRangoAnios,
    buscarPorGenero,
    buscarPorAnio,
    buscarPorCalificacion,
    buscarPorTitulo,
    conseguirGeneros,
    conseguirAnios,
    conseguirCalificaciones,
    conseguirTitulos
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
    resultado = filtrarRangoAnios(2018, 2022, anios)
    assert resultado == [2018, 2020, 2022]


def test_filtrar_rango_anios_fuera_rango():
    anios = [2015, 2018, 2020, 2022, 2025]
    resultado = filtrarRangoAnios(2030, 2040, anios)
    assert resultado == []

# Pruebas para `buscar_por_genero`


def test_buscar_por_genero():
    resultado = buscarPorGenero(peliculas_prueba, "Acción")
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Pelicula 1"


def test_buscar_por_genero_sin_coincidencias():
    resultado = buscarPorGenero(peliculas_prueba, "Ciencia ficción")
    assert resultado == []

# Pruebas para `buscar_por_anio`


def test_buscar_por_anio():
    resultado = buscarPorAnio(peliculas_prueba, 2020)
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Pelicula 1"


def test_buscar_por_anio_sin_coincidencias():
    resultado = buscarPorAnio(peliculas_prueba, 2000)
    assert resultado == []

# Pruebas para `buscar_por_calificacion`


def test_buscar_por_calificacion():
    resultado = buscarPorCalificacion(peliculas_prueba, 9)
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Pelicula 3"


def test_buscar_por_calificacion_sin_coincidencias():
    resultado = buscarPorCalificacion(peliculas_prueba, 10)
    assert resultado == []

# Pruebas para `buscar_por_titulo`


def test_buscar_por_titulo():
    resultado = buscarPorTitulo(peliculas_prueba, "Pelicula 2")
    assert resultado["titulo"] == "Pelicula 2"
    assert resultado["genero"] == "Comedia"


def test_buscar_por_titulo_sin_coincidencias():
    resultado = buscarPorTitulo(peliculas_prueba, "Pelicula inexistente")
    assert resultado is None

# Pruebas para `conseguir_generos`


def test_conseguir_generos():
    resultado = conseguirGeneros(peliculas_prueba)
    assert resultado == {"Acción", "Comedia", "Drama"}

# Pruebas para `conseguir_anios`


def test_conseguir_anios():
    resultado = conseguirAnios(peliculas_prueba)
    assert resultado == {2020, 2018, 2022}

# Pruebas para `conseguir_calificaciones`


def test_conseguir_calificaciones():
    resultado = conseguirCalificaciones(peliculas_prueba)
    assert resultado == {8, 7, 9}

# Pruebas para `conseguir_titulos`


def test_conseguir_titulos():
    resultado = conseguirTitulos(peliculas_prueba)
    assert resultado == {"Pelicula 1", "Pelicula 2", "Pelicula 3"}
