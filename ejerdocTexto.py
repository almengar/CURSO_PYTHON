f = open("abc.txt", "r") #para abrir un archivo como lectura

print(f.encoding) # saca el tipo de encoding del archivo
print(f.name) # saca el nombre del archivo
print(f.closed)  # Es un boolean, si el archivo esta abierto o cerrado

s = f.readline() #para leer linea por linea
print(s)
s = f.readline() #para leer linea por linea
print(s)

for l in f.readlines():  #para leer todo, usara un bucle
    print(l)


print(f.read())    
f.close()  #para cerrar el archivo

