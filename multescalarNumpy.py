import numpy as np
import timeit

def vector_scalar_multiply(vector, scalar):
    return vector * scalar

vector = []
escalar = 2
tamaño = 10000000

# Creando los elementos del vector
for i in range(1, tamaño + 1):
    vector.append(i)

# Convirtiendo la lista de Python a un array de NumPy
vectorNumpy = np.array(vector)

# Multiplicación escalar utilizando NumPy

startingTime = timeit.default_timer()

resultado = vector_scalar_multiply(vectorNumpy, escalar)

endingTime = timeit.default_timer()

#viendo resultado de vectores y tiempo

#print("Vector original:", vectorNumpy)
#print("Resultado:", resultado)

print("El tiempo es de: ", endingTime - startingTime)