# Base de conocimientos de películas y preferencias de usuarios
base_conocimientos_peliculas = {
    'El Padrino': {'drama', 'crimen', 'clasico'},
    'Titanic': {'romance', 'drama', 'clasico'},
    'Interestelar': {'ciencia ficcion', 'aventura', 'drama'},
    'Harry Potter': {'fantasia', 'aventura'},
    'Toy Story': {'animacion', 'familiar', 'comedia'}
}

preferencias_usuario = {
    'drama',
    'aventura'
}

# Función para recomendar películas al usuario basadas en sus preferencias
def recomendar_peliculas(preferencias_usuario, base_conocimientos_peliculas):
    """Recomienda películas al usuario basadas en sus preferencias."""
    peliculas_recomendadas = []
    for pelicula, generos in base_conocimientos_peliculas.items():
        if generos.intersection(preferencias_usuario):
            peliculas_recomendadas.append(pelicula)
    return peliculas_recomendadas

# Recomendar películas al usuario
peliculas_recomendadas = recomendar_peliculas(preferencias_usuario, base_conocimientos_peliculas)

# Mostrar las películas recomendadas al usuario
print("Preferencias del usuario:", preferencias_usuario)
print("Peliculas recomendadas:", peliculas_recomendadas)
