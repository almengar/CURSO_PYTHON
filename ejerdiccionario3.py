

acciones = {"AENA": 143.75, "BBVA": 6.34, "REP": 14.22, "SAN": 3.324}
print(acciones["BBVA"])

#Añade elementos a la lista
acciones.update({"OHLA": 0.518, "ANE": 34.32, "TEF": 3.811})
print(acciones)
#Saca el total de la suma de los valores
total = 0
for v in acciones.values():
    total = total + v
print(f"el total de la suma de precios es: {total:.2f}")

#Saca el total de la suma de los valores menos los del santander
totalS = 0
for k, v in acciones.items():
    if k != "SAN":
        totalS = totalS + v
        
print(f"El total de la suma de precios sin contar el SANTANDER es: {totalS:.2f}")

#SET con varios valores en cada clave, mostrar al final
acciones2 = {"MSFT": [91.5, 54.1, 76.4], "REP": [7.91, 5.6, 6.7], "BBVA": [6.9]}

for k, values in acciones2.items():
    print(k)
    for i in values:
        print(i)