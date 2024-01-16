### SETS ###

#Declarar sets
my_first_set = set()
my_second_set = {}

#Asignando Valores a los sets

my_first_set = {"Fabiano", "RoSystem", 25}
my_second_set = {"Luis", "Developer", 15}

#imprimir sets
print(my_first_set) # ----> Output: {'RoSystem', 25, 'Fabiano'}
print(my_second_set) # ----> Output: {'Luis', 'Developer', 15}

#Conocer el tipo set
print(type(my_first_set)) # ----> Output: Tipo = 'set' | Debemos recordar que los sets no son una estructura ordenada

#Calcular la longitud de los sets
print(len(my_first_set)) # ----> Output: 3

#Busquedas de elementos dentro de los sets
print("Fabiano" in my_first_set) # ----> Output: True

print("Fabiano" in my_second_set) # ----> Output: False

#Funciones BASICAS con sets
my_first_set.add("Developer") #Esta funcion agrega un elemento en una posicion aleatoria y desordeanada dentro de un set | Recuerda que un set no admite 2 elementos con el mismo valor
print(my_first_set) # ----> Output: {25, 'Developer', 'RoSystem', 'Fabiano'}

my_first_set.remove("Fabiano") #Esta funcion elimina el elemento que le pasemos como parametro dentro de un set
print(my_first_set) # ----> Output: {{25, 'RoSystem', 'Developer'}

my_new_set = my_first_set.union(my_second_set) #Esta funcion une 2 sets en uno solo
print(my_new_set) # ----> Output: {'Developer', 'RoSystem', 25, 'Luis', 15}

print(my_new_set.difference(my_first_set)) # ----> Output: {'Luis', 15} | Esta funcion solo muestra los elementos de el segundo set

my_first_set.clear() #Esta funcion limpia totalmente el set
print(my_first_set) # ----> Output: set()

#Pasar de un set (Estructura desordenada) a una lista (Estructura ordenada) y poder usar todas las demas funciones
my_second_set = list(my_second_set)
print(type(my_second_set)) # ----> Output: Tipo = 'list'
print(my_second_set) # ----> Output: ['Developer', 'Luis', 15]

#Eliminar variables que contengan sets
del my_first_set # ----> Esto elimina la variable y se queda sin asignacion es decir ya deja de tener valor
del my_second_set # ----> Esto elimina la variable y se queda sin asignacion es decir ya deja de tener valor


