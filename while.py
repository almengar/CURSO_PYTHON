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

x = 50
while x <= 100:
    print(f"valor {x}")
    x = x + 1

# 2)Desde 5, imprimir los valores 5 a 20, pero excluye 12.

x = 5
while x <= 20:
    if x != 12:
        print(f"valor {x}")
    x = x + 1
       
# 3)Preguntar al usuario por números hasta que el usuario introduzca “q” para quit. 
# Sumar los valores e imprimir el resultado final. 

num = input("introduzca  un número o 'q' para salir")
total = 0
while num != "q":
    total = total + int(num)
    num = input("introduzca  un número o 'q' para salir")
    
   
   
print(f"La suma de valores es: {total}")