# Introducción
# Usando range(), imprimir los números de cero a 100, pero en el siguiente formato:
# “numero X”

# for i in range(0,101):
#     print(i)

# for i in range(0,101):
#     print(f"numero {i}")


# Escribir los números pares empezando por 10 hasta 20. El resultado será 10, 12, 14, 16, 18, 20.
# for i in range(10,20,2):
#     print(i)

# Recibes un correo de tu compañero de trabajo a las 4PM un viernes.
# “Muchas gracias por ayudarme. No he tenido tiempo para terminar estas dos tareas antes de irme de vacaciones. ¿Me podrías ayudar?”
# programa para imprimir tu nombre 50 veces
# nombre = input("¿Cúal es tu nombre?")
# i = 50
# for i in range(50):
#     print(nombre)


# Matemáticas
# Ayudar a tu primo/prima para hacer las matemáticas. Hacer las multiplicaciones de 5 usando range(). El resultado será:
# for num in range(0,11):
#     print(f"5 X {num} = {5* num}")

# Marketing
# Hay que hacer un poco de análisis, para tus compañeros de Marketing. 
# El producto “ABC Widget” vale 10 euros con 51 centimos. Si vendemos 2 productos, ganaremos 21,02 euros. 
# Si vendemos 3, 4 y 5? Mostrar las ganancias para cada supuesta venta, usando range().
# precio = 10.51
# for i in range(1,5):
#     print(f"ganancia con {i} producto es: {precio * i} ")

# Contar
# accion = input("¿Introducir el texto 'up' para contar en positivo desde cero o teclear 'down' para contar en negativo?")

# numeros_de_veces = int(input("¿Cuantas veces quieres repetir?"))

# La respuesta debería ser:
# 0, 1, 2, 3, 4 ….hasta numeros_de_veces para la accion up. 
# 4, 3, 2, 1, 0 desde numeros_de_veces, para la opcion down. 
""" accion = input("¿Introducir el texto 'up' para contar en positivo desde cero o teclear 'down' para contar en negativo?")
numeros_de_veces = int(input("¿Cuantas veces quieres repetir?"))
if accion == "up":
    for i in range(0,numeros_de_veces,1):
        print(i)
elif accion == "down":
    for i in range(numeros_de_veces,0,-1):
        print(i)
else:
    print("opcion erronea, Introducir el texto 'up' para contar en positivo desde cero o teclear 'down' para contar en negativo")        
 """

# Contar el tiempo
# Quieres comprobar el tiempo de ejecución de un programa que imprime un texto 100_000_000 veces a la pantalla. 
# Usando el módulo time, y el método perf_counter, contar el tiempo de ejecución.
# import time
# start = time.perf_counter() #comenzar
# print(start)

# for i in range(100_000):
#     pass
# end = time.perf_counter() # terminar
# print(f"Elapsed time: {end - start}")    

# Blast Off!
# Crear un programa en Python que haga una cuenta regresiva desde 10 hasta 1, 
# y luego imprima el mensaje "¡Despegue!" al final, 
# simulando el lanzamiento de un cohete al espacio. 
# Usar el módulo time para que cuente más lento.
import time
for i in range(10,0,-1):
        print(f"Cuenta atrás: {i}")
        time.sleep(1)
    
print("Despegue!!!") 