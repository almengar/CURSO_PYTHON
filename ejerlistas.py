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
""" vocal = True
listacaracter = ["k", "y", "e", "f", "i"]
listavocales = ["a", "e", "i", "o", "u"]
for i in listacaracter:
    for j in listavocales:
        if listacaracter(i) == listavocales(j):
            print(f"el caracter {listacaracter(i)} es una vocal")
            print(vocal)
        else:
            vocal = False
            print(f"el caracter {listacaracter(i)} es una consonante")
            print(vocal) """

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

""" Ana = ["saco", "cantimplora"]
Carlos = ["tienda", "comida"]
Maria = ["botas", "ropa"]

for i in Ana:
    print(f"Equipamiento de Ana: {i}") 
for j in Carlos:
    print(f"Equipamiento de Carlos: {j}") 
for k in Maria:
    print(f"Equipamiento de Maria: {k}") 
z = Ana + Carlos + Maria
print(z) """

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
compras.insert(2, "limones")
print(compras)