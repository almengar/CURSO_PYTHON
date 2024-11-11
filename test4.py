#TIPOS DE DATOS

# nombre_alumno = "Hola"      --> tipo de dato string
# x = 45.66788                --> tipo de dato float

# x = 34565                     --> tipo de dato entero
# print(type(x))
# print(isinstance(x,str))      --> es un boolean que pregunta el tipo de dato

""" logged_in = True
if logged_in:
    print("es un entero") """

# nombre = "Maria"

# if nombre == "Maria":
#      print("se llama Maria")

#Tipo de dato MUTABLE, INMUTABLE
# x= 1000
# print(id(x))    --> el id es la posición de memoria donde se guarda la variable X
 

 # Limpia la memoria

""" import gc
x = 1000   
del x   #es un candidato para la recoleccion de basura
gc.collect() #Desencadena manualmente la recoleccion de basura
print("Garbage collection triggered") """

""" x = 12.1
print(id(x))
x = 12.2
print(id(x)) """


# Números
# Convertir x = float(3.145) en un tipo de dato int.

""" x = float(3.145)
y = int(x)
print(y) """

""" x = 5.67e2

print(x) """

#La expresión numero % 2 == 0 se utiliza en Python (y en muchos otros lenguajes de programación) 
#para verificar si un número es par. Usarlo para comprobar si un valor es True o False.

# numero = 5

# if numero % 2 == 0:
#     par = True

# else:
#     par = False

# if par:
#     print(f"el numero {numero} es par") 
# else:
#     print(f"el numero {numero} es impar")   


# Calculadora de Propinas: Escribe un programa que le pida al usuario el total 
# de la cuenta de un restaurante y el porcentaje de propina 
# que quiere dejar. El programa debe calcular cuánto es la propina 
# y mostrar el total a pagar (la cuenta más la propina).
# total_cuenta = float(input("Introduce el total de la cuenta"))
# porcentaje = int(input("Introduce el porcentaje de propina"))

# propina = (total_cuenta * porcentaje) / 100
# final = total_cuenta + propina
# print(f"el total de la cuenta incluyendo la propina es {final}")


# NoneType
# Crea un programa que devuelva None si un número es negativo. Si no, decir que el número es “positivo” Empezar así:
# x = int(input("Introducir un número"))
# if x < 0:
#     print(None)
# ACCESO USUARIO Y CONTRASEÑA

# usuario = "almengar"
# password = "nnnn"
# login_ok = True
# user_name = input("Introducir el usuario")
# user_pass = input("Introducir el password")

# if user_name == "almengar" and user_pass == "nnnn":
     
#      pass
# else:
#     login_ok = False

# if login_ok == True:
#     print("Datos correctos, Bienvenido!!!")   
# else:      
#     print("Datos incorrectos, vuelva a introducir los datos")


""" Range
Usando range(), imprimir los números de cero a 100, pero en el siguiente formato:
“numero X” """

# for x in range((101)):
#     print(f"numero  range  {x}")


""" x, y, z = 5, 10, "Hello"
print(x)
print(y)
print(z) """

""" x = None
if x:
    print("x tiene valor")
else:
    print("x no tiene nada") """

#Para saber la posicion en disco de la variable usar ID
# a = "Hola"
# b = "Hola"
# print(id(a))
# print(id(b))

#Para saber el máximo de decimales de un FLOAT
# import sys
# x =3.66677778444766668888
# print(sys.float_info.max)


""" import sys
i = "Hola Mundo"
print(sys.getrefcount(i))
j = i
print(sys.getrefcount(i))
del j
print(sys.getrefcount(i)) """

# for i in range(5):
#    print(f"Hola {i}")

# for i in range(10,20,2):   --> (inicio, fin, salto entre valores)
#     print(f"Hola {i}")

