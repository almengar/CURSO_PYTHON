import random

#Calcula un numero aleatorio entre 0 y 1
print(random.random())


""" random.seed(42) """ #para fijar el numero random que quiero que saque, siempre sacará el mismo
print(random.randint(10,20))  #Calcula un numero entero aleatorio  entre 10 y 20


numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros) #para que desordena la lista de numeros
print(numeros)

frutas = ["kiwis", "manzanas", "platanos"]
x = random.choice(frutas)  #para que elija aleatoriamente uno de los elementos de la lista FRUTAS
print(x)


""" priorizo unos elementos sobre otros, en este caso 'kiwis' tiene preferencias
                                           el K2 es el numero de elementos que va a mostrar """
x = random.choices(frutas, [6, 5, 1], k=2)
print(x)

#saca numeros del 0 al 100 y muestra 5 elementos a la vez
population = range(0, 100)
x = random.sample(population, 5)
print(x)
