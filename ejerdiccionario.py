

def enviar_correo(**kwargs):
    print("Enviando correo..")
    print("Recipiente:" + kwargs["recipiente"])
    if "asunto" in kwargs:
        print("asunto:" + kwargs["asunto"])
    if "cuerpo" in kwargs:
        print("cuerpo:" + kwargs["cuerpo"])

   


enviar_correo(recipiente="ckulhan@nazaret.eus", asunto="Hola", cuerpo="Hola, qué tal?")
enviar_correo(recipiente="pablo@nazaret.eus", cuerpo="Hola, qué tal?")