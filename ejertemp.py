



#diccionario en python con todos los meses del año y las temperaturas y que haya temperaturas repetidas
temperaturas = {
    "Enero": [5, 3, 2, 0, -1, 2, 4],
    "Febrero": [8, 10, 7, 9, 12, 11],
    "Marzo": [15, 13, 17, 16, 14, 18],
    "Abril": [20, 19, 22, 21, 23],
    "Mayo": [25, 24, 27, 26],
    "Junio": [30, 29, 32, 31],
    "Julio": [35, 34, 33, 36],
    "Agosto": [32, 31, 34, 33],
    "Septiembre": [28, 27, 30, 29],
    "Octubre": [22, 21, 24, 23],
    "Noviembre": [15, 14, 17, 16],
    "Diciembre": [10, 9, 12, 11]
}

#Si no existe da error
if temperaturas.get("Diadfa") == None:
    print("No existe")
else:
    print(temperaturas["Diciembre"])

#Saca todas las temperaturas del verano
for k, v in temperaturas.items():
    if k in ("Junio", "Julio", "Agosto"):
        print(k, v)

#Eliminar marzo del diccionario

del temperaturas["Marzo"]    #primera forma para eliminar del diccionario
#temperaturas.pop("Marzo")   #segunda forma para eliminar del diccionario

for k, v in temperaturas.items():
            print(k, v)
#Mostrar las temperaturas unicas
temperaturas2 = {
    "Enero": 5, 
    "Febrero": 8, 
    "Marzo": 15, 
    "Abril": 20,
    "Mayo": 25,
    "Junio": 31,
    "Julio": 36,
    "Agosto": 33,
    "Septiembre": 29,
    "Octubre": 23,
    "Noviembre": 16,
    "Diciembre": 11
}

temperaturas_unicas = set(temperaturas2.values())
print("temperaturas unicas:", temperaturas_unicas)
          


   






