par = set({2, 4, 6, 8, 10, 12, 13, 14})
print(type(par))

impar = {1, 3, 5, 7, 9, 10, 11 }
print(type(impar))


print(1 in impar)

impar.add(11)   #para añadir un elemento al SET, NO permite duplicados
impar.remove(9) #para borrar un elemento del SET
impar.discard(11) #quita un elemento, lo descarta
print(impar)

print(par | impar)  #Union de los dos SET, entonces muestra todos los elementos sin duplicarse, PRIMERA FORMA


x = par.union(impar) #Union de los dos SET, entonces muestra todos los elementos sin duplicarse, SEGUNDA FORMA
print(x)


