# Reto - IVA 
# Un cliente de una empresa de asesoramiento, 
# te han dado una imágen para crear un programa para calcular IVA. 
# Además, necesitan un informe histórico mostrando todos los datos 
# que han introducido los clientes en su calculadora 
# (por ejemplo, Mario hizo un cálculo con 45 euros, Ana hizo con 31 euros, …)


#Manual de usuario:

#Introduzca el precio en euros en la primera caja de texto
#Introduzca el IVA que se desea aplicar al precio
#Como resultado se obtiene el precio sin IVA, el IVA aplicado y el precio con IVA

print("********C A L C U L A D O R A    I V A***************")
precio = float(input("Introduzca el precio en euros: "))
iva = int(input("Introduzca el IVA a aplicar: "))

calculoiva = (precio * iva) / 100
total = precio + calculoiva

print("****************************************************")
print(f"El precio sin IVA es: {precio}")
print(f"El IVA es: {iva}")
print(f"El precio con IVA es: {total}")
print("****************************************************")

#Informe por empleado con el nombre de empleado y los cálculos que ha realizado cada uno
historicos = ["Ana", 34, "Mario", 55, "Sara", 36]


for i in historicos:
    if (isinstance(i, int)):
        print(f"precio con iva:  { i + (i * 21) / 100}")  
    else:
        print(f"{i}")  
        print("*************") 
     