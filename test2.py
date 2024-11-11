 
#  resultado = 51
# if resultado > 80:
#     print("Que bien!!")
#  elif resultado > 60:
#       print("No tan mal")
#  elif resultado > 40:




#       print("MAL!")
#  else:
#       print("muy mal!") 

""" numero = int(input("¿Cual es tu numero favorito?"))

if numero > 0 and numero < 10:
    print("Es entre 1 y 10") """

"""                           ACTIVIDAD1                                
 Preguntar al usuario por su nombre y edad. Mostrar los siguientes mensajes: “[nombre] cumplirás [edad] en tu siguiente cumpleaños.”   ,   “Antes tenías [edad] años”
Agregar su sueldo anual a las preguntas, e imprimirlo también.
"""


# nombre = input("Introduce tu nombre")
# edad = int(input("Introduce tu edad"))
# sueldo = float(input("Introduce tu sueldo anual"))
# edadnew = edad + 1
# edadold = edad - 1
# print(f"{nombre} cumpliras {str(edadnew)} en tu siguiente cumpleaños, antes tenías {str(edadold)}")
# print("Tu sueldo es:  ", sueldo)

"""  ACTIVIDAD2                                
 Crear un programa para conseguir el siguiente resultado en la pantalla, donde pregunta al usuario por sus dos compañeros:
Tus compañeros son Maria y Jon
"""

""" companero1 = input("Introduce el primer compañer@")
companero2 = input("Introduce el segundo compañer@")
print(f"Tus compañeros son {str(companero1)} y {companero2}") """

# ACTIVIDAD3
# Ejecutar este instrucción: 
# print("Hola", 2023, "Agur", 5_000_000_000)

# ACTIVIDAD4
# Tienes este línea de comandos:
# print("Hola", x, ". Tienes", y, "años")
# y quieres conseguir el siguiente output. ¿Qué falta para que funcione el programa?
# Hola Jon . Tienes 32 años
# x = input("Introduce el nombre")
# y = int(input("Introduce la edad"))
# print("Hola", x, ". Tienes", y, "años")

# ACTIVIDAD5
# hijos1 = input("¿Cuántos hijos tienes?")
# print(hijos1*5)
# hijos2 = int(input("¿Cuántos hijos tienes?"))
# print(hijos2*5)

import sys

edad = sys.argv[1]
nombre = sys.argv[2]
print(f"Tienes {edad} años y te llamas {nombre}")

