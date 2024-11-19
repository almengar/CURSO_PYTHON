def sumar(x,y):
    res = x + y
    return res

def restar(x,y):
    res = x - y
    return res

def multi(x,y):
    res = x * y
    return res

def dividir(x,y):
    res = x / y
    return res

def square(x,y):
    res = x ** y
    return res

#main program

if __name__=="__main__":
    print("===============================")
    print("Programa para hacer matematicas")
    print("===============================")

    x = int(input("¿introduce el primer numero:  "))
    y = int(input("¿introduce el segundo numero:  "))

    opcion = input("¿que operacion quieres hacer?, suma, resta, multi, divi o square:  ")

    if opcion == "suma":
        resultado=sumar(x,y)
        print(f"el resultado es: {resultado}")
    elif opcion == "resta":
        resultado=restar(x,y)
        print(f"el resultado es: {resultado}")
    elif opcion == "multi":
        resultado=multi(x,y)
        print(f"el resultado es: {resultado}")
    elif opcion == "divi":
        resultado=dividir(x,y)
        print(f"el resultado es: {resultado}")
    elif opcion == "square":
        resultado=square(x,y)
        print(f"el resultado es: {resultado}")
    else:
        print("opcion incorrecta") 


