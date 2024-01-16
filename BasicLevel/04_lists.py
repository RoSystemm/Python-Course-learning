### LISTAS ###

#Declarar listas
my_first_list = list([10, 20, 30, 20, 50])
my_second_list = [15, 25, 35, 45, 55]

#Imprimir listas
print(my_first_list) # ----> Output: [10, 20, 30, 40, 50]
print(my_second_list) # ----> Output: [15, 25, 35, 45, 55]

#Creando listas combinadas
my_other_list = ["Luis", 25, 1.75, "Peru"]
print(my_other_list) # ----> Output: ['Luis', 25, 1.75, 'Peru']

#Conocer el tipo list
print(type(my_other_list)) # ----> Output: Tipo = 'list' | Este tipo es especial para las listas y podemos mezclar los demas tipos dentro de una lista sin errores

#Calcular la longitud de las listas
print(len(my_second_list )) # ----> Output: 5

#Ubicar valores dentro de una lista
print(my_first_list[0]) #Recuerda que una lista comienza desde el i=0 es decir el primer valor es el [0] y asi sucesivamente | Output: 10

print(my_first_list[1]) # ----> Output: 20

print(my_first_list[4]) # ----> Output: 50

#Ubircar valores dentro de una lista en forma negativa
print(my_first_list[-1]) #Recuerda que al buscar elementos de forma negativa es como tomar de inicio el final y contamos como en un recta numerica ...-3 -2 -1 ----> Output: 50

print(my_first_list[-3]) # ----> Output: 30

print(my_first_list[-4]) # ----> Output: 20

#Devolver numero de ocurrencias dentro de una lista usando el metodo .count()
print(my_first_list.count(20)) # ----> Output: 2

print(my_first_list.count(30)) # ----> Output: 1

#Desenpaquetando lista en variables EN ORDEN
name, age, height, country = my_other_list

print(name) # ----> Output: Luis
print(age) # ----> Output: 25
print(height) # ----> Output: 1.75
print(country) # ----> Output: Peru

#Desepaquetando lista en forma que nosostros queramos
name,height, age, country = my_other_list[0], my_other_list[2], my_other_list[1], my_other_list[3]

print(name) # ----> Output: Luis
print(height) # ----> Output: 1.75
print(age) # ----> Output: 25
print(country) # ----> Output: Peru

#Concatenar listas
print(my_first_list + my_other_list) # ----> Output: [10, 20, 30, 20, 50, 'Luis', 25, 1.75, 'Peru']

#Funciones con listas
new_list = [10, "Hello Python", 10, False]

new_list.append('NewElement') #Esta funcion agrega el elemento que pases como parametro al final de la lista
print(new_list) # ----> Output: [10, 'Hello Python', 10, False, 'NewElement']

new_list.insert(1,'NewElement') #Esta funcion recibe 2 parametros el i y el elemento ya que deacuerdo al indice que le pasemos podremos agregar el elemento nuevo en ese lugar
print(new_list) # ----> Output: [10, 'NewElement', 'Hello Python', 10, False, 'NewElement']

new_list.remove("Hello Python") #Esta funcion elimina el elemento que le pases como parametro pero va en orden es decir si hay repetidos solo elimina el primero
print(new_list) # ----> Output: [10, 'NewElement', 10, False, 'NewElement']

new_list.remove(10) #Aca vemos que esta funcion elimina el elemento que le pases como parametro pero va en orden es decir si hay repetidos solo elimina el primero
print(new_list) # ----> Output: ['NewElement', 10, False, 'NewElement']

new_list.pop() #Esta funcion por defecto elimina el ultimo valor de la lista y nos lo devuelve
print(new_list) # ----> Output: ['NewElement', 10, False]

new_list.pop(2) #Pero nos permite introducir el indice como parametro para eliminar el elemento que nosotros queramos y que nos lo devuelva
print(new_list) # ----> Output: ['NewElement', 10]

new_list.reverse() #Esta funcion nos permite voltear la lista
print(new_list) # ----> Output: [10, 'NewElement']

new_int_list = [10, 50, 30, 90] # Solo funciona si son int completamente o str completamente no se puede mezclar
new_str_list = ['A', 'Z', 'X', 'P']  # Solo funciona si son int completamente o str completamente no se puede mezclar

new_int_list.sort() #Esta funcion por defecto nos ordena la lista de menor a mayor valor pero podemos pasarle parametros para que el ordenamiento sea distinto
new_str_list.sort() #Esta funcion por defecto nos ordena la lista de menor a mayor valor pero podemos pasarle parametros para que el ordenamiento sea distinto

print(new_int_list) # ----> Output: [10, 30, 50, 90]
print(new_str_list) # ----> Output: ['A', 'P', 'X', 'Z']

del new_list[1] #Esto nos permite eliminar el elemento de forma definitiva segun el indice que le pasamos como parametro
print(new_list) # ----> Output: ['NewElement']

new_list[0] = 'OtherElement' #Esto nos permite cambiar un elemento pasandole el indice especifico y el nuevo valor
print(new_list) # ----> Output: ['OtherElement']

other_new_List = new_list.copy() #Esto nos permite copiar una lista y guardarla dentro de una variable
print(other_new_List) # ----> Output: ['OtherElement']

new_list.clear() #Esto nos permite limpiar totalmente nuestra lista
print(new_list) # ----> Output: []

#Sublistas mediante indice
print(new_str_list[1:3]) # ----> Output: ['P', 'X']

print(new_str_list[3:4]) # ----> Output: ['Z']

print(new_str_list[1:4]) # ----> Output: ['P', 'X', 'Z']
