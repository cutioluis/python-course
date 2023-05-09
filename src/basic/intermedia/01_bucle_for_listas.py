# For - Nos ayuda a iterar

from collections.abc import Iterable
""" for variable in secuencia:
    Codigo 
 """

for i in "Python":
    print("iteracion", i)

for a in range(10, 10):
    print(a)

animales = ['gato', 'snake', 'cocodrillo']
for animal in animales:
    print(animal)

# Iteradores e iterables
# lo que va después del in deberá ser siempre un iterable.
""" for <variable> in <iterable>:
    <Código>
"""
#Saber si es iterable
lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10

print(isinstance(lista, Iterable))
print(isinstance(cadena, Iterable))
print(isinstance(numero, Iterable))


#For de la misma longitud
numeros = [1, 2, 3, 4]
caracteres = ["a", "b", "c", "d"]

for numero, caracter in zip(numeros, caracteres):
    print(caracter)
    print(numero)
    
#Range
for num in range(0, 20):
    print(num)

#Enumerate, obtener el indice de la lista
for num in enumerate(numeros):
    print(f"Este es el indice de numeros: {num[0]}, este es el valor de numeros: {num[1]}")
    
#usando el else
for numero in numeros:
    print(numero)
else:
    print("El bucle termino")
    #Si no hay elementos igual se ejecuta
    
frutas = ["banana", "pera", "pepperoni", "orange", "watermelon"]


#termina el bucle con break
for fruta in frutas:
    print(f"usando break {fruta}")
    if fruta == "orange":
        break

#se salta con el continue
for fruta in frutas:
    if fruta == "pera":
        continue
    print(f"usando contunue {fruta}")