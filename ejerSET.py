sucriptores_existentes = {'alice@example.com', 'ana@example.com', 'bob@example.com'}
sucriptores_nuevos = {'peter@example.com', 'carlos@example.com', 'bob@example.com'}

print(sucriptores_existentes | sucriptores_nuevos) #listado de suscriptores sin duplicados, primera forma
correos = sucriptores_existentes.union(sucriptores_nuevos)#listado de suscriptores sin duplicados, segunda forma
print(correos)


x = sucriptores_nuevos.difference(sucriptores_existentes) #listado de suscriptores que no existían antes
print(x)


#ejercicio: convertir lista en SET para quitar los duplicados y luego volver a convertir en una lista
empleados = ['alice@example.com', 'ana@example.com', 'bob@example.com','juan@example.com', 'bob@example.com']

print(list(set(empleados)))  # se convierte la lista a SET para poder quitar los valores duplicados y después se convierte 
                             # en una lista

 