### OPERADORES ###

### OPERADORES ARITMETICOS ###

#Operadores Basicos
suma = 3 + 4 
print(suma) # ----> Output: 7

resta = 4 - 3
print(resta) # ----> Output: 1

multiplicacion = 3 * 3
print(multiplicacion) # ----> Output: 9

division = 10/5
print(division) # ----> Output: 2.0

#Operadores Raros
resto = 10 % 2 
print(resto) # ----> Output: 1

exponente = 10 ** 2 
print(exponente) # ----> Output: 100

dvexacta = 10 // 6 
print(dvexacta) # ----> Output: 1

#Contatenar con + los 'str'
print('Hello ' + 'World!') # ----> Hello World!

#Concatenar 'str' con 'int'
print('Hello ' + str(5)) # ----> Output: Hello 5

#Imprimir multiples veces con los operadores
print('Hello ' * (4*2)) # ----> Output: Hello Hello Hello Hello Hello Hello Hello Hello

#Imprimir multiples veces con numeros float
float_var = 1.5 * 4
print('Hello ' * int(float_var)) # ----> Output: Hello Hello Hello Hello Hello Hello



### OPERADORES COMPARATIVOS ###


#Operadores Basicos
print(3 > 2) # ----> Output: True

print(4 < 10) # ----> Output: True

print(5 <= 10) # ----> Output: True

print(3 >= 2) # ----> Output: True

print(3 == 4) # ----> Output: False

print(3 != 5) # ----> Output: True

#Comparar Multiplemente 
print(3 < 5 > 3) # ----> Output: True

#Comparar strings
print('HelloWorld' > 'HelloPython') # ----> Output: True

print('HelloWorld' < 'HelloPython') # ----> Output: False

print('HelloWorld' <= 'HelloPython') # ----> Output: False

print('HelloWorld' >= 'HelloPython') # ----> Output: True

print('HelloWorld' == 'HelloPython') # ----> Output: False

print('HelloWorld' != 'HelloPython') # ----> Output: True



### OPERADORES LOGICOS ###

print(3 != 5 and 'HelloWorld' > 'HelloPython') # ----> Output: True
print(3 != 5 or 'HelloWorld' > 'HelloPython') # ----> Output: True
print(not(3 != 5)) # ----> Output: False

#Multiples Operaciones logicos
print(3 != 5 or ('HelloWorld' > 'HelloPython' and 'HelloWorld' >= 'HelloPython')) # ----> Output: True

