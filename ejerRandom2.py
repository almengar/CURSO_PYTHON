import random

v1 = random.random()
print(int(v1 * 100))

v2 = random.randint(0,100)
print(v2)


# Eres profesor y tienes una lista de alumnos. 
# ¿Qué función del módulo random podrías usar para sacar un alumno aleatoriamente de la lista?
# nombres= ['Arturo','Julio','Dani','Aurora','Roberto','Martina']
# ¿Qué cambios harías para engañar a uno de los alumnos, siempre sacando su nombre, aunque lo produzca aleatoriamente?
nombres= ['Arturo','Julio','Dani','Aurora','Roberto','Martina']

x = random.choices(nombres, [10, 1, 1, 1, 1, 1], k=1) #para engañar y sacar siempre un nombre, primera forma
print(x)
random.seed(42) #para engañar y sacar siempre un nombre, segunda forma
elemento = random.choice(nombres) #saca un alumno aleatoriamente de la lista
print(elemento)

#Comprobar que es lo que se obtiene como resultado:

import math as m
x = 15.6547

print("================================")
print(m.ceil(x)) #redondea hacia arriba
print(m.floor(x)) #redondea hacia abajo

print(m.pow(4, 3)) #la potencia 4 al cubo
print(m.gcd(6, 9)) #maximo comun divisor
print(m.factorial(4)) #saca el factorial de 4

print(m.e)   #El valor de EULER que es una constante
print(m.pi)  #saca el numero PI

print("================================")

#Calcular la media de las notas de los alumnos
notas = [2, 6, 7, 3, 7, 8, 6]
suma = 0
for i in notas:
    suma = suma + i
print(f"La media es: {suma/len(notas)}")