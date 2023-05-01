# Metodos de diccionarios


def center_text(phrase):
    return print(phrase.center(30, '-'))


# Acceder pordemos acceder con get() o usando su key
p1 = {'nickname': "Luis", 'power': 300, "live": False, "gold": 3000}
print(p1.get('nickname'))

# Msodificar un elemento
p1["power"] = 500
print(p1)

# Agrega automaticamente
p1["married"] = True
print(p1)

# Iterrar el key
for x in p1:
    print(x)
frase = "Separacion"
print(frase.center(30, '-'))
# Iterar el value
for x1 in p1:
    print(p1[x1])
print(frase.center(30, '-'))

# Iterar los 2 juntos
for a, b in p1.items():
    print(a, b)

# Dicionarios aninados
print(frase.center(30, '-'))

anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {"anidado1": anidado1, "anidado2": anidado2}
print(d)

# METODOS

center_text("METODOS")

# clear() = elimina toda el dicionario
dicionario_clear = {"d": 1, "center": True}
dicionario_clear.clear()
print(dicionario_clear)

#items() = devuelve una lista con los keys y values
dicionario_listas = {"d": 1, "center": True}
dicionario_listas.items()
print(dicionario_listas)

#keys() = devuelve los keys del dicionario
dicionario_keys = {"d": 1, "hg": 300}
keys = dicionario_keys.keys()
print(keys)


#values() = deuvuelve una lista con todos los valores
dicionario_values = {"d": 1, "center": True}
values = dicionario_values.values()
print(values)


#pop() = elimina la key que se pasa como parametro, si no hay da eror(solucionado com otro parametro -1)
dicionario_pop = {"d": 1, "low": False}
dicionario_pop.pop("a", -1)
print(dicionario_pop)