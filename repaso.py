# Actividades de repaso
# Preguntar al usuario por su salario. 
# Multiplicar el salario que introduce el usuario por 10, 
# explicándole que podría ganar tanta cantidad si fuera experto en Python

""" salario = float(input("Introduce tu salario:  "))
print(salario)
multi = salario * 10
print(f"el resultado es: {(multi:.3f)}, con esto serias experto en Python") """

#Preguntar al usuario por 2 números. Sumarlos y mostrar el resultado.
""" num1 = int(input("Introduce un número:  "))
num2 = int(input("Introduce un número:  "))
suma = num1 + num2 """
""" print(f"el resultado de la suma es: {suma}")
print(type(suma)) #para saber el tipo de dato
print(id(suma)) #para saber la ubicación en memoria """

""" if (isinstance(suma)): 
     print("la variable es un string")
else:
     print("la variable  NO es un string") """


# La acción de SANTANDER va cambiando de 3.1453, 2.987 y 3.5. 
# Una aplicación de mainframe con la que compartes datos solo quiere saber el número entero, 
# por ejemplo, 3, 2, 3. Mostrar los datos de la acción en el formato que pueda usar el mainframe.
numeros = [3.1453, 2.987, 3.5 ]
for i in numeros:
    print(int(i))
    print(round(i))

import math
print(math.floor(3.4))   #para redondear hacia abajo
print(math.ceil(4.4))    #para redondear hacia arriba


