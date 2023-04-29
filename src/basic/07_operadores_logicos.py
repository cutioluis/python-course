# Logical Operators

# and - Devuelve True si los 2 son True
print(True and True) 
print(False and False) 
print(True and False)
print(False and True)

print("-----------------------")
# or - Devuelve True si almenos un elemento es True
print(True or False)
print(False or False)
print(False or True)
print(True or True)

print("-----------------------")
# Se resuelve primeros los 2 primeros y despues el otro, tambien se pueden mezaclar los operadores
print(True and True and False)



print("-----------------------")
# not - invierte True por False y viceversa
print(not True)
print(not False)
# Podemos anidar los not, si es par si queda el mismo pero si no se cambia  el valor
print(not not not not True)



print("------------- EJEMPLOS ---------------")
# Prioridad not and, or
print(True or True and False and True)
print(True or False and False)
print(0 and not 1 or 1 and not 0 or 1 and 0)
