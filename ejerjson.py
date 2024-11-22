import json

accion = '{"nombre": "Repsol", "precio": 5}'  #se convierte a string
print(type(accion))

#convertir en diccionario
a = json.loads(accion)  #se importa el texto
print(type(a))

#usar el texto para json
b = json.dumps({"nombre":"Hola"})
print(type(b))