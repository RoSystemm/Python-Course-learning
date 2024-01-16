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

print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age))
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age))

#Utilizando f para incluir variables dentro de un string
print(f'Mi nombre es {name} {surname} y mi edad es {age}')

#Desenpaquetando caracteres
text = "Python"
a, b, c, d, e, f = text

print(a, b, c, d, e, f)

#Dividir Strings
text_slice = text[1]
print(text_slice)

text_slice = text[1:3]
print(text_slice)

text_slice = text[:]
print(text_slice)

text_slice = text[0:6:2]
print(text_slice)

text_slice = text[1:]
print(text_slice)

text_slice = text[-2]
print(text_slice)

#Voltear un string 
reverse_str = text[:: -1]
print(reverse_str)

#Funciones

print(text.capitalize())

print(text.casefold())

print()
