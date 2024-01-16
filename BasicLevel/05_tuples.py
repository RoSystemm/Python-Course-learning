### TUPLAS ###

#Declarar tuplas
my_first_tuple = tuple()
my_second_tuple = ()

#Asignando Valores a las tuplas
my_first_tuple = (20, 2.55, "Luis", False)
my_second_tuple = (50, 30, "Hola", True)

#imprimir tuplas
print(my_first_tuple) # ----> Output: (20, 2.55, 'Luis', False)
print(my_second_tuple) # ----> Output: (50, 30, 'Hola', True)

#Conocer el tipo tuple
print(type(my_first_tuple)) # ----> Output: Tipo = 'tuple'

#Ubicar valores dentro de una tupla
print(my_first_tuple[0]) # ----> Output: 20 | Recuerda que una tupla comienza desde el i=0 es decir el primer valor es el [0] y asi sucesivamente

print(my_first_tuple[2]) # ----> Output: Luis

print(my_first_tuple[3]) # ----> Output: False

#Ubircar valores dentro de una tupla pero con indice negativo

print(my_first_tuple[-1]) # ----> Output: False | Recuerda que al buscar elementos de forma negativa es como tomar de inicio el final y contamos como en un recta numerica ...-3 -2 -1

print(my_first_tuple[-3]) # ----> Output: 2.55

print(my_first_tuple[-2]) # ----> Output: Luis

#Devolver numero de ocurrencias dentro de una tupla usando el metodo .count()

print(my_first_tuple.count(20)) # ----> Output: 1

print(my_first_tuple.count("Luis")) # ----> Output: 1

print(my_first_tuple.count(False)) # ----> Output: 1

#Buscar un elemento dentro de una tupla mediante el elemento y te devuelve el indice con .index()

print(my_first_tuple.index(20)) # ----> Output: 0

print(my_first_tuple.index("Luis")) # ----> Output: 2

print(my_first_tuple.index(False)) # ----> Output: 3

#Concatenar tuplas
new_tuple = my_first_tuple + my_second_tuple
print(new_tuple) # ----> Output: (20, 2.55, 'Luis', False, 50, 30, 'Hola', True)

#Subtuplas mediante indice de una tupla fusionada
print(new_tuple[2:6]) # ----> Output: ('Luis', False, 50, 30)

print(new_tuple[2:4]) # ----> Output: ('Luis', False)

print(new_tuple[1:3]) # ----> Output: (2.55, 'Luis')

#Crear tuplas mutables, poder usar las funciones una lista y luego volverlo una tupla denuevo
my_first_tuple = list(my_first_tuple)
print(type(my_first_tuple)) # ----> Output: Tipo = 'list'

my_first_tuple.insert(1, 80)
print(my_first_tuple) # ----> Output: [20, 80, 2.55, 'Luis', False]

# Convertir nuevamente la lista en una tupla
my_first_tuple = tuple(my_first_tuple)
print(type(my_first_tuple)) # ----> Output: Tipo = 'tuple'
print(my_first_tuple) # ----> Output: (20, 80, 2.55, 'Luis', False)

#Eliminar variables que contengan tuplas

del my_first_tuple # ----> Esto elimina la variable y se queda sin asignacion es decir ya deja de tener valor
del my_second_tuple # ----> Esto elimina la variable y se queda sin asignacion es decir ya deja de tener valor
