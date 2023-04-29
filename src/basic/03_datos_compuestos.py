# LISTAS

# Podemos modificar los elemtos
listas = ["Cbum", "Carlos Best", "Turbosteps", 12, False]
print(listas[1])
listas[1] = "Luis"
print(listas[1])

# TUPLAS
tupla = ("Cbum", "Carlos Best", "Turbosteps", 12, False)
# tupla[0] = "Daddy" - No se puede modificar los elementos

# SETS
# No se puede acceder a los elementos por indice
set = {"Cbum", "Carlos Best", "Turbosteps", 12, False}
# print(set[1]) - No sirve

# JSON - Diccionarios
# Su estructura es in key = value para acceder al elemntos accedes con el nombre del KEY
diccionario = {
    "key": "value",
    "nombre": "Luis",
    "edad": 12,
    "estado_civil": True
}

print(diccionario["estado_civil"])



