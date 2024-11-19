
def comprobar_productos(numero_productos):
    match numero_productos:
        case _ if numero_productos > 0 and   numero_productos < 11:
            print("Cantidad de productos correcta")
        case _:
            print("la cantidad de productos no esta entre 1 y 10")


#main program
if __name__=="__main__":
    numero_productos = int(input("Introduce el numero de productos, maximo 10 unidades:  "))
    comprobar_productos(numero_productos)
    
    print(f"Numero de productos introducidos: {numero_productos}")