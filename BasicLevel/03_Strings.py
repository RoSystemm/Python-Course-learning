### STRINGS ###

var_string = 'Hello'
second_var_string = 'Mor'

#Strings con saltos
new_var_string = 'Este texto tiene un salto de \n linea'
print(new_var_string)

tab_string = '\t Este texto tiene tabulacion'
print(tab_string)

scap_string = '\t Este texto es \n raro'
print(scap_string)

#Formateo de strings
name, surname, age = 'Luis', 'Fabiano', 15

print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age)) # ----> Output: Mi nombre es Luis Fabiano y mi edad es 15
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age)) # ----> Output: Mi nombre es Luis Fabiano y mi edad es 15

#Utilizando f para incluir variables dentro de un string
print(f'Mi nombre es {name} {surname} y mi edad es {age}') # ----> Output: Mi nombre es Luis Fabiano y mi edad es 15

#Desenpaquetando caracteres
text = "Python"
a, b, c, d, e, f = text

print(a, b, c, d, e, f) # ----> Output: P y t h o n

#Dividir Strings
text_slice = text[1] 
print(text_slice) # ----> Output: y

text_slice = text[1:3]
print(text_slice) # ----> Output: yt

text_slice = text[:]
print(text_slice) # ----> Output: python

text_slice = text[0:6:2] # ----> Output: Pto
print(text_slice)

text_slice = text[1:] # ----> Output: ython
print(text_slice)

text_slice = text[-2] # ----> Output: o
print(text_slice)

#Voltear un string 
reverse_str = text[:: -1] # ----> Output: nohtyP
print(reverse_str)

#Funciones
print(text.capitalize()) # ----> Esta funcion pone la primera letra en Mayuscula | Output: Python

print(text.casefold()) # ----> Esta funcion devuelve el string convertido en minuscula | Output: python

print(text.upper()) # ----> Esta funcion pone la palabra en Mayuscula completamente | Output: PYTHON

print(text.count('y')) # ----> Esta funcion cuenta cuantas veces se repite el elemento que le pasas como parametro en la palabra | Output: 1

print(text.isnumeric()) # ----> Esta funcion comprueba si el string es numerico o no devuelve un booleano | Output: False

print(text.isupper()) # ----> Esta funcion comprueba si el string esta en mayuscula  | Output: False

print(text.islower()) # ----> Esta funcion comprueba si el string esta en minuscula | Output: False

print(text.lower()) # ----> método devuelve una cadena donde todos los caracteres están en minúsculas se ignoran los símbolos y los números. | Output: python

print(text.startswith('Py')) # ----> Esta funcion comprueba si el string comienza con ciertas letras y devuelve un booleano  | Output: True