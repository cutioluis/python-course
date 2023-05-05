# For - Nos ayuda a iterar

from collections.abc import Iterable
""" for variable in secuencia:
    Codigo 
 """

for i in "Python":
    print("iteracion", i)

for a in range(10, 10):
    print(a)

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

