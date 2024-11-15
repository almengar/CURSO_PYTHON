# Reto - IVA 
# R E Q U I S I T O S
# Un cliente de una empresa de asesoramiento, 
# te han dado una imágen para crear un programa para calcular IVA. 
# Además, necesitan un informe histórico mostrando todos los datos 
# que han introducido los clientes en su calculadora 
# (por ejemplo, Mario hizo un cálculo con 45 euros, Ana hizo con 31 euros, …)


# M A N U A L   D E    U  S  U  A  R  I  O:

#Introduzca el precio en euros en la primera caja de texto
#Introduzca el IVA que se desea aplicar al precio
#Como resultado se obtiene el precio sin IVA, el IVA aplicado y el precio con IVA

#Retos: En el informe histórico de empleados ha surgido el reto de añadir tanto el nombre del empleado como el cálculo 
#       correspondiente en cada registro

#Descripción historia:
# Como: Crear calculadora
# Quiero: realizar cálculos  de IVA y obtener datos de histórico
# Para que: Agilizar cálculos de los clientes

print("********C A L C U L A D O R A    I V A***************")
precio = float(input("Introduzca el precio en euros: "))
iva = int(input("Introduzca el IVA a aplicar: "))

calculoiva = (precio * iva) / 100
total = precio + calculoiva

print("****************************************************")
print(f"El precio sin IVA es: {precio} euros")
print(f"El IVA es: {calculoiva} euros")
print(f"El precio con IVA es: {total} euros")
print("****************************************************")

print("*********************")
print("**********************************")
print("****************************************************")
print("******  I N F O R M E   H I  S  T  O  R  I  C  O       C  L  I  E  N  T  E  S  ******")
#Informe de histórico por cliente con el nombre del cliente y los cálculos que ha realizado cada uno

#-----------------------------------------------------------------------------------------------
#                                     Plan de pruebas
#-----------------------------------------------------------------------------------------------

#Prueba------------Input--------------------------------------Output esperado----------Output actual----------PASS/FAIL
#   1              cliente Ana ,   importe 34 euros, iva 21           41.14 euros                               OK
#   2              cliente Mario , importe 55 euros, iva 21           66.55 euros                               OK
#   3              cliente Sara ,  importe 36 euros, iva 21           43.56 euros                               OK
#-----------------------------------------------------------------------------------------------------------------------

historicos = ["Ana", 34, "Mario", 55, "Sara", 36]


for i in historicos:
    if (isinstance(i, int)):
        print(f"precio con iva:  { i + (i * 21) / 100} euros")  
        print("")
    else:
        print(f"Cliente: {i}")  
        print("*************") 
        
     