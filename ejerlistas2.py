#ejerDada la siguiente lista, ¿qué esperas recibir con los comandos…?
""" x = [10, 50, 20, "Hola", "Agur", 99]
print(x[2:4])  # (comenzar: terminar: pasos]
print(x[::2]) #hace un salto de 2
print(x[3::]) # se posiciona en la posición 3
print(x[::])     #muestra toda la lista 
print(x[::-1])   #muestra la vista a la inversa    """

# Teniendo 2 listas x, y….¿qué esperas recibir?
""" x = [10, 20, 30, 30, 50]
y = [50, 60, 70, 80]
print(x+y) # concatena las 2 listas anteriores
z = x +y
print(x) #muestra la lista X """


#Ejercicio de lista de alumnos
""" ListaDeAlumnos = ["Jon", "Maria", "Isabel"]
for i in ListaDeAlumnos:
    print(i) """


#Usar TUPLE
""" import timeit
print(timeit.timeit(stmt='("red", "green", "blue")', number=1000000000))
print(timeit.timeit(stmt='["red", "green", "blue"]', number=1000000000)) """


#Ejercicio vocales y consonantes
# Teniendo una lista de caracteres [“k”, “y”, “e”, “f”, “i”], 
# comprobar cada uno de los elementos para ver si es un vocal (vocales = [“a”, “e”, “i” …]). 
# Mostrar True si es vocal y False si es constante.

""" listacaracter = ["k", "y", "e", "f", "i"]
listavocales = ["a", "e", "i", "o", "u"]
for i in listacaracter:
        if i in listavocales:
            print(f"el elemento {i}, True")
        else:
            print(False) """

# vocales(correccion profesor)
""" letras = ["a", "b", "e", "f", "o", "x", "c"]

for l in letras:
    if l in ["a", "e", "i", "o", "u"]:
        print(True)
    else: 
        print(False) """

#Ejercicio CAMPING
# Ana, Carlos y Maria van a pasar el fin de semana en un camping en Las Landas. 
# Cada uno traerá diferentes cosas (saco de dormir, tienda, cantimplora, …). 
# Mostrar el equipamiento de cada uno, y al final, el equipamiento de todos. 
# Probablemente traerán una o más tiendas. 
# Al final, contar el número de tiendas que han traído todos.

""" Ana = ["saco", "cantimplora", "tienda"]
Carlos = ["tienda", "comida"]
Maria = ["botas", "ropa", "tienda"]

equipamiento = Ana + Carlos + Maria """

""" print(", ".join(equipamiento)) """ #para poder imprimir las listas seguidas separados de una coma

""" print(Ana.count("tienda")) """  #cuenta las veces que aparece la tienda en la lista Ana
""" for i in Ana:
    print(f"Equipamiento de Ana: {i}") 
for j in Carlos:
    print(f"Equipamiento de Carlos: {j}") 
for k in Maria:
    print(f"Equipamiento de Maria: {k}") 
z = Ana + Carlos + Maria
print(z)
cont = 0
for i in z:
    if i == "tienda":
        cont = cont + 1

print(f"la tienda aparece  {cont} veces")

print(z.count("tienda")) """  # con esta sentencia se cuentan todos los elementos de la lista que son TIENDA

#Ejercicio Camping(Version profesor)
""" maria = ["tienda", "linterna", "saco de dormir"]
ana = ["linterna", "brújula", "cuchillo"]   
carlos =  ["saco de dormir", "mochila", "cantimplora"] 

equipamiento = maria + ana + carlos
# Mostrar el equipamiento de cada persona
print("Equipamiento de cada persona:")
print(f"Maria lleva {maria}")
print(f"Ana lleva {', '.join(ana)}")  # ojo!
print(f"Carlos lleva {carlos}")

# Mostrar la lista única de todos los objetos
print("Lista de todos los objetos:")
print(", ".join(equipamiento))

contarTiendas = 0
for i in equipamiento:
    if i in "tienda":
        contarTiendas += 1
print(f"Al final, tenemos {contarTiendas} tienda(s)") """

#Crear una lista para gestionar tu compra. Por ejemplo, 

# Añadir “galletas” y “zumo” a la lista de compras
# Mostrar todo la lista
# Mostrar el segundo y tercer elemento
# Mostrar los últimos 2 elementos - “galletas” y “zumo”
# Cambiar “zumo” por “zumo de naranja”
# Quitar la última compra que has añadido a la lista
# Insertar “limones” en una posición del medio de la lista
# Mostrar la lista en orden alfabético	
compras = ["platanos", "manzanas", "leche"]
compras.append("galletas")
compras.append("zumo")
print(compras)
print(compras[1:3])
print(compras[3::])

compras[4] = "zumo de naranja"
print(compras)
compras.remove("zumo de naranja")
print(compras)
compras.insert(2, "limones")   #Se añade un elemento en el centro de la lista
compras.sort()
print(compras)

#*****************************************************************************************

""" frutas = ["kiwi", "manzana", "naranja"]
for fruta in frutas:
    print(fruta)

frutas.append("mandarina")

for fruta in frutas:
    print(fruta)

x, *y = frutas   #coge primero el primer elemento y luego el resto de elementos de la lista
*x, y, z = frutas
print(x)
print(y)
#print(dir(frutas)) """
#*****************************************************************************************
""" 
rgb = (145, 54, 11)
coordenadas = (123, 5)  # coordenadas X e Y """


# Gestión de una tienda
# Se podría extender la idea de arriba para crear una aplicación 
# para gestionar la compra de productos en una tienda.

ProductosEspeciales = ["Manzanas", "Zumos", "Leche"]
Productos = ["Huevos", "Lechuga", "Atun"]
TotalProductos = ProductosEspeciales + Productos

print("**************MENU**************")
print("opcion 1: Ver todos los productos")
print("opcion 2: Hacer una compra")
print("opcion 3: Borrar un producto")
print("********************************")     

opcion = int(input("Elige opción"))

if opcion == 1:
    print("\n".join(TotalProductos))
elif opcion == 2:
    print("********************************") 
    for i in TotalProductos:
        if i in ProductosEspeciales:
            print(f"{i}: precio 10 euros/kilo")
        else:
            print(f"{i}: precio 12 euros/kilo")
    
    print("********************************")  

    
    continuar = True 
    importe = float(input("Introduzca el importe que va a dar"))
    total = 0

    while continuar or importe > 10:
        compra = input("¿Qúe producto vas a comprar?")

        if compra in TotalProductos:
            print("El producto esta en el listado")
            if compra in ProductosEspeciales:
                total = total + 10
            else: 
                total = total + 12
                importe = importe - total
            if importe < 10:
                print("Importe insuficiente")
                exit()
                print(f"El producto adquirido es: {compra} ")
                print(f"El cambio es: {importe} euros")
       

                respuesta = print("¿Desea seguir comprando? SI/NO")
                if respuesta == "SI":
                    continuar = True
                elif respuesta == "NO":
                    continuar = False
                    exit()
                else:
                    print("Opción incorrecta")
                    exit()
        else:
            print("El producto no esta en el listado")
        




elif opcion == 3:
    producto_eliminar = input("¿Qúe producto vas a eliminar?")
    if producto_eliminar in TotalProductos:
        print("producto eliminado")
        TotalProductos.remove(producto_eliminar)
        print(TotalProductos)
    else:
        input("No tenemos este producto")
       

    