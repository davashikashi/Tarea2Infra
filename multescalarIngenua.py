import timeit

vector = []
escalar = 2
tamaño = 10000000

#creando los elementos del vector
for i in range(1,tamaño+1):
    vector.append(i)

#creación de la funcion 
def vector_scalar_multiply(vector, scalar):
    result = []
    for element in vector:
        result.append(element * scalar)
    return result

# Ejemplo de uso y analisis de tiempo

startingTime = timeit.default_timer()

resultado = vector_scalar_multiply(vector, escalar)

endingTime = timeit.default_timer()

print("el tiempo es de: ", endingTime - startingTime)

#print("original: ",vector)
#print("resultado:", resultado)
