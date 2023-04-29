# Metodos Strings

# Capitzalized = Convierte la primera letra en Mayuscula
sentence1 = 'i love python'
sentence_capitalized = sentence1.capitalize()
print(sentence_capitalized)

#Center = regresa el texto centrado con la long
sentence2 = 'ejemplos'
sentence_center = sentence2.center(10, "-")
print(sentence_center)

#casefold = Convierte todos los caracteres en miniscula
sentence3 = 'PyTHoN'
sentence_casefold = sentence3.casefold()
print(sentence_casefold)

#count = regresa el numero de veces que se repite  en un string
sentence4 = 'Python is the best leguage in the world!'
sentence_count = sentence4.count("P")
print(sentence_count)

#len = cuenta los caracteres de una cadena
sentence_len = len(sentence4)
print("Cuenta caracteren, len: ", sentence_len)

#endswwith = verifica si una cadena comienza con
sentence5 = 'Luis es el mejor juagdor del mundo'
sentence_endswith = sentence5.endswith("mundo")
print(sentence_endswith)

#startwith = veificasi una cadena termina con
sentence_startwith = sentence5.startswith("Luis")
print(sentence_startwith)

#replace = remplaza un valor por otro
sentence_remplace = sentence5.replace("Luis", "Alex")
print(sentence_remplace)

#split = separa por el param dado
sentence6 = 'Luis_Dame:Tu_Cosita'
sentence_split = sentence6.split('_')
print(sentence_split)

#find = metodo encuentra la pirmera aparicion del valor especificado. sino devuelve -1
sentence_find = sentence6.find('L')
print(sentence_find)

#index = es igual que find, pero si no encuentra nada nos manda una exepcion
sentence_index = sentence6.index('L')
print(sentence_index)


#upper = convierte a mayusculas
sentence_upper = sentence6.upper()
print(sentence_upper)

#lower = convierte a minusculas
sentence_lower = sentence6.lower()
print(sentence_lower)