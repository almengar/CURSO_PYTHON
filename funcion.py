
def sobremi(nombre, edad):
    print(f"tu nombre es {nombre}")
    print(f"tu edad es {edad}")

#main program
if __name__=="__main__":
    sobremi("Ché", 48) 
    sobremi("Alberto", 42) 
          
def hola():
    """
    Esta funcion imprime hola
    """
    print("Hola")
    x = 10
    y = 11
    result = x + y
    return result
    

""" print(help(hola))   #Para poder ver el comentario que he escrito en la funcion
print(hola.__doc__) #Para poder ver el comentario que he escrito en la funcion """

res = hola()    #llamada a la función que guarda el resultado


 



