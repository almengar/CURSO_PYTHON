

def calcular_precio(precio):
    precio = precio * 2
    return precio

def cambiar_lista_precios(lista_de_precios):
    lista_de_precios.append(3)
    print(lista_de_precios)
    return lista_de_precios

#main program

if __name__=="__main__":
    precio = 5
    x = calcular_precio(precio)
    print(x)  #Muestra 10
    print(precio)  #Muestra 5

    lista_de_precios = [1, 5, 8]
    
    cambiar_lista_precios(lista_de_precios)
    print(lista_de_precios)

