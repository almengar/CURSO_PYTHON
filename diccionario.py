def hello(**kwargs):
    print(type(kwargs))  #se comprueba que es de tipo diccionario
    
    if "ing" in kwargs:
        print(kwargs["ing"])
    if "esp" in kwargs:
        print(kwargs["esp"])
    if "eus" in kwargs:
        print(kwargs["eus"])
    



hello(ing="Hello", esp="Hola", eus="Kaixo")