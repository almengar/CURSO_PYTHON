
def adivinar(numero, solucion):
        
    if numero == solucion:
        print("Muy bien has adivinado el numero!!!!!!!")
        exit()
    elif numero < solucion:
        print("El numero a adivinar es mayor")
     
       
    elif numero > solucion:
        print("El numero a adivinar es menor")
        
        
        
def bienvenida():
    print("================================================")
    print("Juego de adivinar un numero")
    print("------------------------------------------------")
    print("Intenta adivinar un numero entre 1 y 10")
    print("================================================")  
       

#main program
if __name__=="__main__":
    
    intentos = 1
    solucion = 5
    max_intentos = 3
    
    bienvenida()
    
    while intentos <= max_intentos:

        numero = int(input("Introduce un numero, a ver si adivinas entre 1 y 10:  "))
        adivinar(numero, solucion)
                
        print(f"llevas {intentos} intentos y te quedan {3 - intentos} intentos")
        intentos = intentos + 1
        
    
    print("GAME OVER, te has quedado sin intentos")
        

