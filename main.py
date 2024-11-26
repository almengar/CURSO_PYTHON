# Actividad - terminar este quiz

import random

# Diccionario con preguntas y respuestas - key son preguntas, values son respuestas correctas
quiz_data = {
    "¿En qué película aparece la frase 'Yo soy tu padre'?": "Star Wars",
    "¿Qué película tiene el récord de ser la más taquillera de todos los tiempos (hasta 2024)?": "Avatar",
    "¿Quién dirigió la película 'El laberinto del fauno'?": "Guillermo del Toro",
    "¿Qué película presenta al personaje 'Jack Sparrow'?": "Piratas del Caribe",
    "¿Qué película animada está ambientada en el Día de los Muertos?": "Coco",
}

print("🎥 ¡Bienvenido al Quiz de Películas! 🎥")
print("Responde las siguientes preguntas para poner a prueba tu conocimiento sobre películas.")
print("-" * 50)

preguntas = list(quiz_data.keys()) # convertir los keys en una lista
# usar un método de random para barajar las preguntas
random.shuffle(preguntas)
contACER = 0
for pregunta in preguntas: # bucle para iterar por todas las preguntas
    respuesta = input(pregunta)
    # si su respuesta es igual que la del quiz_data, es correcto!
    # usar .lower() para comprarar
    if respuesta .lower()== quiz_data[pregunta].lower(): 
        print("HAS ACERTADOOOOOO")
        contACER = contACER + 1
    else:
        print("ERRORRRRRR") 
       
     
# al final, mostrar los numeros correctos
print(f"Conseguiste acertar {contACER} de {len(quiz_data)}")   
#Fin de mi programa