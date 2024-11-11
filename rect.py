# Programa para calcular el area de un rectángulo

# largo = float(input("Introduce el largo del rectángulo"))
# ancho = float(input("Introduce el ancho del rectángulo"))
import sys
#Por defecto coge los campos como string asi que hay que convertirlos a entero
largo = int(sys.argv[1])
ancho = int(sys.argv[2])


area = largo * ancho
#print("El area del rectángulo es: ", area )
print(f"El area es {area}")

