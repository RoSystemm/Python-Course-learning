### CONDICIONALES ###

#Condicional Basica con bool
my_condition = True

if my_condition:
    print("Se ejecuta la condición del if")

#Condicional Basica con int
my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# Condicionales completas con int
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")


# Condicional con strings
my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")