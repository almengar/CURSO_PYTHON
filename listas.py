# x = range(10,16)
# print(list(x))

# x = range(12,22,3)
# print(list(x))

# x = range(100,-10,-10)
# print(list(x))

# print(x[0])
# print(x[5])

#Como crear una lista con elementos distintos
# x = 6
# y = 7
# z = "Hola"
# a = True

x = [7, 8, "Agur", True] #Lista, es mutable por lo que se pueden cambiar los valores

y = (7, 8, "Agur", True) #tuple, es inmutable por lo que NO se pueden cambiar los valores, cib orden

Z = {6, 7, "Hola", True} #set, es inmutable, sin orden, no se pueden duplicar valores 

x.append(4)
x.append("Mario")

print(x)
print(x[-1]) #Muestra el primer elemento de la tabla
""" print(dir(x)) #para saber todos los comandos que existen para aplicar a la variable X """

print(x[:3]) #Muestro los 3 primeros valores
y = print(x[3:6])#Muestro del tercer al sexto valor

print(x[1:6:3]) #Muestra del primer al sexto valor con un salto de tres elementos

#bucle para mostrar una lista de frutas
""" frutas = ["kiwis", "manzanas", "naranjas"]
for f in frutas:    
    print(f) """