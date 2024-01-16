### DICCIONARIOS ###

#Declarar diccionarios
my_first_dict = dict()
my_second_dict = {}

#Asignando Valores a los sets de distintas formas
my_first_dict = {"Nombre":"Luis", "Edad":15, "Curso":"Python"}

my_second_dict = {
    "Frutas": {"Fresa", "Melon", "Papaya", "Mango", "Platano"},
    "Lenguajes": {"Python", "Lua", "JavaScript", "TypeScript", "Rust"}
}

#imprimir sets
print(my_first_dict) # ----> Output: {'RoSystem', 25, 'Fabiano'}
print(my_second_dict) # ----> Output: {'Luis', 'Developer', 15}

#Conocer el tipo dict
print(type(my_first_dict)) # ----> Output: Tipo = 'dict' | Debemos recordar que los dicts son una estructura de tipo "Clave":"Valor"

#Calcular la longitud de los dicts
print(len(my_first_dict)) # ----> Output: 3
print(len(my_second_dict)) # ----> Output: 2

#Acceder a elementos dentro de un diccionario
print(my_first_dict["Nombre"]) # ----> Output: Luis | Esto busca con el parametro que le pasaste una key del mismo valor para retornarnos el contenido de ese valor
print(my_second_dict["Frutas"]) # ----> Output: {'Mango', 'Melon', 'Papaya', 'Platano', 'Fresa'} | Esto busca con el parametro que le pasaste una key del mismo valor para retornarnos el contenido de ese valor

#Cambiar valores mediante la key especifica

my_first_dict["Nombre"] = "Juan" #Esto nos permite cambiar el contenido que se encuentra dentro de una key especifica
print(my_first_dict["Nombre"]) # ----> Output: Juan

my_first_dict["Pais"] = "Peru" #Esto te crea un nuevo key:valor si es que no encuentra una key de el mismo valor que le estas pasando
print(my_first_dict) # ----> Output: {'Nombre': 'Juan', 'Edad': 15, 'Curso': 'Python', 'Pais': 'Peru'}

#Eliminar un elemento especifico dentro un diccionario
del my_first_dict["Pais"] #Esto te crea el key con su valor que hayas pasado como parametro
print(my_first_dict) # ----> Output: {'Nombre': 'Juan', 'Edad': 15, 'Curso': 'Python'}

#Obetener un listado de todos los items dentro del diccionario
print(my_first_dict.items())

#Obtener todas las keys de nuestro diccionario
print(my_first_dict.keys())

#Obtener todos los values almacenado dentro de las keys de nuestro diccionario
print(my_first_dict.values())

#Funcion basica con diccionarios

my_new_dict = dict.fromkeys(("Nombre", "Edad", "Curso")) #Esta funcion nos ayuda a crear un diccionario NUEVO con keys que le proporciones sin valores
print(my_new_dict) # ----> Output: {'Nombre': None, 'Edad': None, 'Curso': None}

my_new_dict = dict.fromkeys(my_second_dict) #Esta forma nos ayuda a poder utilizar las mismas keys de otro diccionario pero esta vez no tendran valores
print(my_new_dict) # ----> Output: {'Frutas': None, 'Lenguajes': None}

my_new_dict = dict.fromkeys(my_second_dict, "Hello Python") #Esta forma damos valores predeterminados a todas las keys que se crearan automaticamente
print(my_new_dict) # ----> Output: {'Frutas': 'Hello Python', 'Lenguajes': 'Hello Python'}