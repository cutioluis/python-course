# Listas - mutables y dinamicas

# append = agrega un item al final de la lista
lista = [1, 3, 4, 5]
lista.append(6)
print(lista)

#clear = vacia todos los elementos de la lista
lista.clear()
print(lista)

#extend = une 2 listas
l1 = [1, 2, 3]
l2 = [1, 3, 4]
l1.extend(l2)
print(l1)

#count = cuenta el numero de veces que aprece un item
l4 = [1, 2, 3, 4, 1, 1, 1].count(1)
print(l4)

#index = devuelve el indice el que esta
l5 = [1, 2, 3, 4].index(2)
print(l5)

#insert = agreaga un item a la posicion deseado
l6 = [1, 2, 3, 4]
l6.insert(0, 8)
print(l6)

#pop = extae un item de la lista y lo borra
l7 = [1, 2, 3, 4]
l7_custom = l7.pop(0)
print(l7_custom)  # solo el lo que extrajimos
print(l7)  # nueva lista

#remove = elimina el primer valor que concuerde con el dado
l8 = [1, 2, 3, 4]
l8.remove(2)
print(l8)

#reverse = le da vuelva a la lista no vale con string
l9 = [1, 2, 3, 4]
l9.reverse()
print(l9)

#sort = ordena el valor de manor a mayor
l10 = [1, 2, 3, 4, 3, 2, 1]
l10.sort()
#l10.sort(reverse=True)
print(l10)