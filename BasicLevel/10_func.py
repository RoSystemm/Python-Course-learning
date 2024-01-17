### FUNCIONES ###

#Definiendo una funcion
def my_first_function():
    print('Nuestra primera funcion')

#Llamando a nuestra primera funcion
my_first_function()

#Pasando parametros a una funcion
def sumvalues(a, b):
    return a + b #Retornando la suma

print(sumvalues(1, 9))

#Pasanado de parametro un str

def SayName(name):
    return f"Hola tu nombre es: {name}"

print(SayName('Valentino'))

#Funcion con parametro por defecto
def SayName(name, rango = 'noob'): #Esto define un valor por defecto que si no le pasas ningun parametro se ejecutara con el valor por defecto
    return f"Hola tu nombre es: {name} y tu rango es: {rango}"

print(SayName('Valentino'))

#Funcion para printear muchos textos sin limites
def PrintTexts(*texts):
    for text in texts:
        print(text)

PrintTexts('Hola', 'Python')

#Funcion para pasar a mayuscula cada str que le pasemos

def str_mayus(*texts):
    for text in texts:
        print(text.upper())
str_mayus('hola', 'este es un texto en upper', 'funcion automatica')

