# Ejercicios dicionarios
"""

1.Crea un diccionario llamado person con las siguientes claves y valores:

"name": "Juan",
"age": 25,
"city": "Madrid",
"email": "juan@gmail.com"

a) Imprime el valor asociado a la clave "name".
b) Agrega la clave "phone" con el valor "123-456-789" al diccionario.
c) Elimina la clave "email" del diccionario.
d) Imprime todas las claves del diccionario.

"""

person = {'name': 'Juan', "age": 25, "city": "Madrid", "email": "juan@gmail."}

person_name = person.get("name")
print(person_name)

person["phone"] = "123-456-789"
print(person)

person.pop("email")
print(person)

person_items = person.items()
print(person_items)
""" 

Crea un diccionario llamado grades que represente las calificaciones de un grupo de estudiantes. 
Las claves deben ser el nombre del estudiante y los valores una lista de calificaciones.
a) Agrega un nuevo estudiante llamado "Luis" con las siguientes calificaciones: [9, 10, 8, 7, 9].
b) Imprime el promedio de calificaciones del estudiante "Juan".
c) Imprime una lista con todos los nombres de los estudiantes en el diccionario.
d) Calcula el promedio de calificaciones de todo el grupo.

"""

grades = {
    "Juan": [8, 7, 9, 8, 7],
    "Ana": [9, 9, 8, 9, 10],
    "Vanesa": [10, 10, 10, 5, 5]
}

grades["Luis"] = [7, 6, 5, 4, 6]
students = grades.items()
print(students)

prom_juan = sum(grades["Juan"]) / len(grades["Juan"])
print(prom_juan)

students = grades.keys()
for student in students:
    print(student)

promedio_grupo = 0
total_calificaciones = 0

for calificaciones in grades.values():
    total_calificaciones += len(calificaciones)
    promedio_grupo += sum(calificaciones)
promedio_grupo /= total_calificaciones
print(f"El promedio del grupo es: {promedio_grupo}")
