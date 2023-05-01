nombres = ["Juan", "María", "Pedro", "Lucía", "Luis"]


# Agregar un nuevo nombre al final de la lista
nombres.append('LuisDev')
print(nombres)

# Agregar un nuevo nombre en una posición específica de la lista
nombres.insert(0, "LuisDev")
print(nombres)

# Eliminar el primer nombre de la lista
nombres.pop(0)
print(nombres)

# Eliminar un nombre específico de la lista
nombres.remove("LuisDev")
print(nombres)

# Ordenar los nombres alfabéticamente
nombres.sort()
print(nombres)

# Obtener la cantidad de nombres en la lista
ct_names = len(nombres)
print(f'La lista contiene {ct_names} nombres ')

# Obtener el índice de un nombre específico en la lista
nl  = nombres.index('Luis')
print(nl)