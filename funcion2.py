def hacer_cafe(precio, tipo_de_cafe="café", tamano="normal"): #estoy pasando a la función los valores de los parametros por defecto
    print(f"Hemos hecho {tipo_de_cafe} {tamano}")

def mensaje_de_bienvenida():
    print("Hola buenos días")
    producto = input("que quieres tomar?")
    return producto

#main program

if __name__=="__main__":
    producto = "cafe"
    if producto in("café", "cafe"):
        hacer_cafe(2.5, tamano="grande", tipo_de_cafe="cafe con leche")
        hacer_cafe(2.5,"cortado", "normal")       
        hacer_cafe(8.6,"cafe con leche", "pequeño")    
        hacer_cafe(5.5)
        mensaje_de_bienvenida()