

# Trabajas en un restaurante con la siguiente carta. 
# Usar match para crear un programa para mostrar el precio que selecciona el usuario.
# Menú:
# Café: $2.50
# Té: $1.80
# Jugo: $3.00
# Sándwich: $4.50
# Muffin: $2.00


def calcular(producto):
        match producto:
                case "cafe":
                        return 2.50
                case "te":
                        return 1.80
                case "jugo": 
                        return 3.00   
                case "sandwich":
                        return 4.50
                case "muffin":
                        return 2.00
                case _:
                        print("No tenemos ese producto")
                        return None
#main program

if __name__=="__main__":
    producto = input("Introduce el producto del que deseas el precio: ")
    precio = calcular(producto)
    if precio != None:
        print(f"el precio del {producto} es {precio}")
