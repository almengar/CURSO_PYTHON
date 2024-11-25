s ="    122,python,es,64,un,777,lenguaje,222,de,55,66,789,programación,y,me,82,gusta   "  
a = s.strip()

b = a.split(",")
c = []
for palabra in b:
    if not palabra.isnumeric():
        c.append(palabra)
d = " ".join(c)
d
e = d.capitalize()
e


texto = """     Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. 
Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. 
Cuando contratamos nuevos empleados. 
Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. 
Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. 
Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        """


#Contar las veces que la palabra Python aparece en el texto...y si a veces aparece en el texto con mayusculas y minusculas - Python, python

texto.lower().count("python")

#Encontrar la ubicación (numero/indice de carácter) donde esta la primera ocurrencia de la palabra Python. 
texto.find("Python")
texto[46:52]  #Comprueba que de la posicion 46 a la 52 esta la palabra "Python"

#¿Y la segunda ocurrencia de la palabra Python?
a = texto.find("Python", 47)
texto[148: 154]

#¿La palabra 'código' está en el texto? Usar if ... in ...:

if "código" in texto:
     print("si")
#Reemplazar Python por PYTHON
texto2 = texto.replace("Python", "PYTHON")
print(texto2)


#Cambiar la letra de todo el texto a "lO MÁS IMPORTANTE QUE NOS HA MANTENIDO EN pYTHON... " - no usar replace
texto3 = texto.swapcase().strip()
print(texto3)



#Encriptado
#Usando ord() y chr(), se puede, fácilmente, encriptar texto. 
#Por ejemplo, sumando 1 a la letra “A”, hace que sea más difícil descifrar una letra. 
#Crear un programa para encriptar un texto del usuario, y luego descifrarlo.

texto = "Hola"
#cifrar 
for i in texto:
    print(ord(i)+1)

#Descifrar
numeros = [73, 112, 109, 98]
for i in numeros:
    print("--------")
    print(chr(i-1))

