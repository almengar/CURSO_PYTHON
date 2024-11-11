# Contar
""" accion = input("¿Introducir el texto 'up' para contar en positivo desde cero o teclear 'down' para contar en negativo?")

numeros_de_veces = int(input("¿Cuantas veces quieres repetir?"))

if accion == 'up':
    for i in range(numeros_de_veces + 1):
        print(f"{i}")

elif accion == 'down':
     for i in range(numeros_de_veces - 1,0,-1):
         print(f"{i}")
else:
    input("Acción errónea, Introducir el texto 'up' para contar en positivo desde cero o teclear 'down' para contar en negativo?") """

# Animaciones - Coche en movimiento - https://emojipedia.org/
# Queremos mostrar un coche en movimento, conduciendo desde la izquierda del Terminal hasta la final. Incrementar los espacios

import time
car = "\U0001F697" 

distancia = 10
for posicion in range(distancia)
    print(" " * posicion, end=" ") #Con end lo que hace es evitar el salto de linea
    print(car, end="\r") #Con \r el cursor vuelve al principio
    time.sleep(0.5) #tiempo de pausa

