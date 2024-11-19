from datetime import datetime
import locale #es una libreria para definir el lenguaje en el que estas trabajando
#Pedir al usuario su fecha de nacimiento, ejemplo: 17 may 1989
#Usar strptime()

fecha = input("introduce tu fecha de nacimiento:  ")
print(fecha)

fecha_obj = datetime.strptime(fecha, "%d %b %Y" )   
#Para imprimir la fecha en formato castellano, con el %b son las 3 primeras letras del mes

#Imprime en formato YYYY-mm-dd
print(fecha_obj.strftime("%Y-%m-%d"))

ahora = datetime.today()

if fecha_obj <= ahora:
    print("Fecha valida")

else:
    print("Fecha incorrecta")





