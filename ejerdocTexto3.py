# Actividad
# Usando este repositorio de github, https://github.com/itsfoss/text-files, 
# leer los datos de los archivos, practicando lo que has visto anteriormente en la demostración. 
# Por ejemplo, leer todo de una vez, leer línea a línea, agregar una línea al texto, ….


""" with open("agatha.txt", "r") as f: """  #lee un archivo de una sola vez
"""   s = f.read() """


""" print(s)  """


""" with open("agatha.txt", "r") as f: """  #lee linea a linea
"""  for l in f.readlines():
        print(l) """

""" with open("agatha2.txt", "a") as f: """  #Para escribir en el archivo un salto de linea, hay que poner un nombre de fichero
                                     #que no exista
"""   f.write(s + "  \n") """ #escribe una linea en blanco


# Con los empleados, imprimir su nombre completo y correo electrónico:
# https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv
FILE_NAME = "empleados.csv"
output = ""
with open(FILE_NAME, "r") as f:
     linea = f.readline()
     for linea in f.readlines(): 
        lista = linea.split(",")
        output = output + "NAME: " + lista[1] + " "
        output = output + "LASTNAME: " + lista[2] + " "
        output = output + "EMAIL: " + lista[3] 
        output = output + "\n"
     print(output)
     OUTPUT_FILE = "output.txt"
     with open(OUTPUT_FILE, "w") as f:
         f.write(output)
         


    
         
