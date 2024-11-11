#Programa para convertir grados Celsius a fahrenheit  (MI  VERSION)

""" grados = float(input("introduce los grados"))

convers= str(input("¿Que tipo de conversion quieres hacer?"))

if convers == 'c':
    res = (grados - 32) * 5/9 
    print(f"La temperatura en Fahrenheit es: {res:.2f}")
elif convers == 'f':
      res = (grados * 9 / 5) + 32  
      print(f"La temperatura en Fahrenheit es: {res:.2f}")
    
else:
     print("Opción incorrecta, tienes que introducir 'c' o 'f'") 
"""
#Programa para convertir grados Celsius a fahrenheit  (VERSION DE CHE)
accion = input("Para convertir de Fahrenheit a Celsius, teclear 'c'. Para Celsius a Fahrenheit, teclear 'f': ")

if accion == "f":
    celsius = float(input("Introduce la temperatura en Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print("La temperatura en Fahrenheit es: %.2f" % fahrenheit)  # Formato de float tradicional
    # print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}")  # formato más actual para usar Python 3.6

elif accion == "c":
    fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 0.5556
    print("La temperatura en Celsius es: %.2f" % celsius)  # Formato de float 

else:
    print("Lo siento. Tienes que introducir 'c' o 'f'")
