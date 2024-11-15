# i = 0
# while i<10:
#     print(f"Hola:  {i}")
#     i = i + 1
# print("Fin de while: " + str(i))    


# i = 0
# while i<10:
#     print(f"Hola:  {i}")
#     if i == 5:
#         """ break """  #para salir del bucle
        
#         continue #para seguir a la siguiente instruccion
#     i = i + 1

# i = 0
# while i<10:
#     print(f"Hola:  {i}")
    
#     i = i + 1
# else:
#     print("ELSE")


# Actividades básicas de while:

# 1)Imprimir los valores desde 50 hasta 100. 

""" x = 50
while x <= 100:
    print(f"valor {x}")
    x = x + 1

# 2)Desde 5, imprimir los valores 5 a 20, pero excluye 12.

x = 5
while x <= 20:
    if x != 12:
        print(f"valor {x}")
    x = x + 1 """
       
# 3)Preguntar al usuario por números hasta que el usuario introduzca “q” para quit. 
# Sumar los valores e imprimir el resultado final. (PRIMERA FORMA)

# num = input("introduzca  un número o 'q' para salir")
# total = 0
# while num != "q":
#     total = total + int(num)
#     num = input("introduzca  un número o 'q' para salir")
      
   
# print(f"La suma de valores es: {total}")


# 3)Preguntar al usuario por números hasta que el usuario introduzca “q” para quit. 
# Sumar los valores e imprimir el resultado final. (SEGUNDA FORMA)
total = 0
""" while True:
    num = input("introduzca  un número o 'q' para salir:  ")
    if num == "q":
        break
    else:
        total = total + int(num)    
print(f"el total  es:  {total}")
 """
#Imprimir todos los números de 0 a 99 excluyendo(10, 20, 30, 40, 50, 60, 70, 80, 90)

""" num = 0
while num <100:
    if num  not in (10, 20, 30, 40, 50, 60, 70, 80, 90):
        print(num)
    num = num + 1 """
        
    
# Usando un bucle WHILE, crear un programa para conseguir el siguiente resultado. 
# En este caso el usuario ha intentado varias veces, 
# y hasta que coinciden las contraseñas, el programa sigue pidiendo.


password = input("introduzca  la contraseña:  ")
password2 = input("introduzca  de nuevo la contraseña:  ")

while password != password2:
    print("las contraseñas no coinciden, hacerlo de nuevo")
    password = input("introduzca  la contraseña:  ")
    password2 = input("introduzca  de nuevo la contraseña:  ")

print("contraseña correcta")
