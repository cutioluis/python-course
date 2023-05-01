""" 
Supongamos que tienes un diccionario llamado peliculas que contiene información sobre varias películas.
Cada película es representada por una clave que es el título de la película, y el valor asociado a cada clave es otro diccionario con información adicional de la película. 
Cada diccionario interno contiene los siguientes campos: 
   año, director, actores (una lista de nombres de los actores principales), 
   duracion (en minutos) y rating (en una escala del 1 al 10).

Tu tarea es escribir un programa en Python que realice las siguientes operaciones:

Calcular el promedio de duración de todas las películas.
Calcular el promedio de rating de todas las películas.
Encontrar la película con el mayor rating y mostrar toda su información.

"""

movies = {
    "The Godfather": {
        "año": 1972,
        "director": "Francis Ford Coppola",
        "actores": ["Marlon Brando", "Al Pacino", "James Caan"],
        "duracion": 175,
        "rating": 9.2
    },
    "The Shawshank Redemption": {
        "año": 1994,
        "director": "Frank Darabont",
        "actores": ["Tim Robbins", "Morgan Freeman"],
        "duracion": 142,
        "rating": 9.3
    },
    "La primera vez": {
        "año": 2018,
        "director": "David Clen",
        "actores": ["Tinker Robert", "Sven Acter"],
        "duracion": 242,
        "rating": 7.3
    },
}

#Calcular el promedio de duración de todas las películas.
movie_len = len(movies)
movie_total_duracion = 0

for movie in movies.values():
    movie_total_duracion += movie["duracion"]

total_promedio = movie_total_duracion / movie_len
print(f"El promedio de las peliculas de duracion es: {total_promedio} ")

#Calcular el promedio de rating de todas las películas.
rating_len = len(movies)
movie_rating_total = 0

for movie in movies.values():
    movie_rating_total += movie["rating"]

total_rating = movie_rating_total / rating_len
print(f"El promedio de las peliculas de rating es: {total_rating} ")

#Encontrar la película con el mayor rating y mostrar toda su información.
mayor_rating = -1
movie_max_rating = None

for movie in movies.values():
    if movie["rating"] > mayor_rating:
        mayor_rating = movie["rating"]
        movie_max_rating = movie

print("La película con el mayor rating es:")
print(f"Año: {movie_max_rating['año']}")
print(f"Director: {movie_max_rating['director']}")
print(f"Duración: {movie_max_rating['duracion']}")
print(f"Rating: {movie_max_rating['rating']}")

