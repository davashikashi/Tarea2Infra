import ctypes
import timeit

#carga de la libreria
fun = ctypes.CDLL("./libmultescalar.so")

#definiendo el tipo de argumentos y resultado
fun.vectorScalarMultiply.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_int]
fun.vectorScalarMultiply.restype = None

#creando el vector a usar

vector =[]
escalar = 2
tamaño = 10000000

for i in range(1,tamaño+1):
    vector.append(i)

# Convertir lista de Python a un array de ctypes
vector_c = (ctypes.c_double * len(vector))(*vector)
resultado_c = (ctypes.c_double * len(vector))()

#tomamos el tiempo solo cuando se hace la multiplicacion escalar
startingTime = timeit.default_timer()
# Llamando a la función
fun.vectorScalarMultiply(vector_c, escalar, resultado_c, tamaño)

endingTime = timeit.default_timer()

# Mostrando resultados vectores y tiempo

#print("Original:", list(vector_c))
#print("nuevo:", list(resultado_c))

print("El tiempo total fue de: ", endingTime - startingTime)