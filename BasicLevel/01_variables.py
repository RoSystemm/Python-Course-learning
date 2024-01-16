### VARIABLES ###

#Formas de nombrar variables
my_string_variable = "Este es mi primera variable"
mystringvariable = "Este es mi primera variable"

#Nombrando nuestras primera variables
my_str_variable = "Este es mi primera variable"

my_int_variable = 25

my_bool_variable = False

#Para poder ver el VALOR que esta almacenado dentro de nuestra variable
print(my_str_variable) # ----> Output: Este es mi primera variable
print(my_int_variable) # ----> Output: 25
print(my_bool_variable) # ----> Output: False

#Concatenar entre variables
print(my_str_variable, my_int_variable) #----> Output: Este es mi primera variable 25
print(my_int_variable, my_bool_variable) #----> Output: 25 False
print(my_int_variable, my_int_variable, my_bool_variable) #----> Output: Este es mi primera variable 25 False

#Concatenar con str definido
print("Esta variable tiene de valor: ", my_int_variable)
print("Esta variable tiene de valor: ", my_bool_variable)

#Transformando Variables

#De tipo 'int' a 'str'
transformation_int_variable = 20
my_first_transformation_variable = str(transformation_int_variable)
print(type(my_first_transformation_variable)) #----> Tipo = 'str'

#De tipo 'str' a 'int'
transformation_str_variable = '15'
my_second_transformation_variable = int(transformation_str_variable)
print(type(my_second_transformation_variable)) #----> Tipo = 'int'


#Poder saber cuantos caracteres tiene un str
print(len(my_str_variable)) # ----> Output: 27


#Nombrar multiples variables en una sola linea
vbool, vint, vstr = False, 11, 'Hola!'
print(vbool, vint, vstr) # ----> Output: False 11 Hola!

#Almacenar informacion introducida por el usuario usando la funcion input()

input("Introduce un numero: ") #Esto funciona pero no almacena el dato

dato_introducido = input("Introduce un numero: ") #Esto si guarda el dato introducido
print(dato_introducido)

#Problema de tipado fuerte con Python

vbool = "Hola" #Esto deberia ser un 'bool' pero al ejecutar no tenemos ningun error
vint = False #Esto deberia ser un 'int' pero al ejecutar no tenemos ningun error
vstr = 15 #Esto deberia ser un 'str' pero al ejecutar no tenemos ningun error

print(vbool, vint, vstr) # ----> Output: Hola False 15

#Nombrando Variables dandoles de valor otras variables

my_new_variable = 25
my_fusion_variable = my_new_variable

print(my_fusion_variable) # ----> Output: 25
