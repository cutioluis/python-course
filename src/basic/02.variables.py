#Variables son un espacio de memoria de guardado.
nombres_desarrolladores = "Alex y Luis"

# Concatenacion con +
bienvenida = "Hola " + nombres_desarrolladores + "Como están"

# Concatenación con fStrings.5
bienvenida = f"Hola {nombres_desarrolladores} Como están"

# Operadores de pertenecia in y not in
print("estan" in bienvenida)
print("como" not in bienvenida)

#Str - functions
my_int_variable = 5
print(type(my_int_variable))
my_int_to_string = str(my_int_variable)
print(type(my_int_to_string))

#Variables en una linea - Pesima practica
name, surname, alias, age = "Luis", "Cutiopala", "cutioluis", 17
print(
    f"Hola me llamo {name}, y mi otro nombre {surname}, mi alias es {alias}, y mi edad {age} "
)

#Inputs
nombre = input("Cual es tu nombre")
print(nombre)
