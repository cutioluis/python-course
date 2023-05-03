# Variables 2.0

#creando los datos 
datos_en_tupla = ('Luis', "Cutiopala", 12121)
datos_en_lista = ["Luis", "Cutiopala", 2121]

#desempaquetado
nombre,apellido,suscriptores = datos_en_lista

#mostrando resmltados
print(datos_en_lista)
print(nombre)



#creando tuplas con tuple()
tupla = tuple(["Dato1", "Dato2", "Dato3"])
print(type(tupla))

#creando una tupla sin parentesis y varios datos
tupla = "dato3", "dato3", "dato3"
print(type(tupla))


#creando una tupla con un solo dato
tupla = "dato_alone",
print(type(tupla))



#CONJUNTO SET()

#creando un conjunto con set()
conjunto = set(["Dato1"])

#metiendo un conjunto dentro de otro
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)



#Teoria de conjuntos
conjunto1 = {1,2,3,3}
conjunto2 = {1,2,3,3}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1
print(resultado)


#verificar si es un superocnjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1
print(resultado)


#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)