

acciones = {"MSFT": 412, "NVDA": 143, "REP": 9}  #es un diccionario porque tiene una estructura CLAVE, VALOR

print(type(acciones))

print(acciones["MSFT"])

for k, v in acciones.items():    #va imprimiendo la clave y valor de cada elemento del SET
    print(k, v)


for k in acciones.keys():   #imprime todas las claves del SET
    print(k)

for v in acciones.values(): #imprime todos los valores del SET
    print(v)


acciones["MSFT"] = 120
acciones["BBVA"] = 170  #Si el elemento no esta, entonces lo inserta
acciones.update({"SANTANDER": 120, "ANA": 200})  #Añade los elementos al SET
print(acciones["MSFT"])
print(acciones)