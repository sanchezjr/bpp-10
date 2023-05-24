#compresión de listas 
cuadrados = []
for i in range(10):
    cuadrados.append(i**2)
    

# nueva_lista = [expresión for elemento in iterable]
'''
nueva_lista: es la lista resultante que se creará a partir de la comprensión.
expresión: es la operación o cálculo que se realizará en cada elemento del iterable.
elemento: es la variable que representa cada elemento del iterable en cada iteración.
iterable: es una secuencia, como una lista, una cadena de texto, una tupla o incluso otro objeto iterable.
'''

cuadrados = [i**2 for i in range(10)]

numeros = [1, 2, 3, 4, 5]

pares = []
for x in numeros:
    if x % 2 == 0:
        pares.append(x)
        
pares = [x for x in numeros if x % 2 == 0]

palabras = ["hola", "python", "comprension", "listas"]
longitudes = [len(palabra) for palabra in palabras]
print(longitudes) 


#funcion map
#map(funcion, iterable)
'''
función: es la función que deseas aplicar a cada elemento del iterable.
iterable: es una secuencia, como una lista, una tupla o incluso otro objeto iterable.
'''
def cuadrados(x):
    return x**2

cuadrados = lambda x: x**2

cuadrados(2)

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados) 

numeros1 = [1, 2, 3, 4, 5]
numeros2 = [10, 20, 30, 40, 50]
suma = list(map(lambda x, y: x + y, numeros1, numeros2))
print(suma)

#filter
#filter(función, iterable)
'''
función: es una función que toma un elemento del iterable como argumento y devuelve un valor booleano (verdadero o falso) indicando si se debe incluir o no ese elemento en el resultado.
iterable: es una secuencia, como una lista, una tupla o incluso otro objeto iterable.

'''
def par(x):
    return x%2==0

numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)


def es_mayor_de_edad(persona):
    return persona["edad"] >= 18

personas = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 16},
    {"nombre": "Pedro", "edad": 19},
    {"nombre": "Laura", "edad": 17}
]

mayores_de_edad = list(filter(es_mayor_de_edad, personas))
print(mayores_de_edad)  

#reduce
#reduce(función, secuencia)
'''
función: es una función que toma dos argumentos y realiza una operación de reducción entre ellos.
secuencia: es una secuencia, como una lista, una tupla o incluso otro objeto iterable.
'''
from functools import reduce
numeros = [1, 2, 3, 4, 5]
suma_aux = reduce(lambda x, y: x + y, numeros)
print(suma_aux)
sum(suma_aux)


#test de clase5