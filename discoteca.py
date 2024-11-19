def calcular(edad):
    if edad < 18:
        print("Eres menor, no puedes entrar en la discoteca")
    elif edad > 65:
        print("Tenga en cuenta que hay mucho ruido en la discoteca")
    else:
        print("Puede pasar")




if __name__=="__main__":

    edad = int(input("Introduce tu edad:  "))

    resultado = calcular(edad)
    if resultado != None:
        print(resultado)