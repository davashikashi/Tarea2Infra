import ctypes

#carga de la libreria
fun = ctypes.CDLL("./libmultescalar.so")

#definiendo el tipo de argumentos y resultado
fun.vectorScalarMultiply.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_int]
fun.vectorScalarMultiply.restype = None

#creando el vector a usar

vector =[]
escalar = 2
tamaño = 20 
#10000000
resultado = 0

for i in range(1,tamaño+1):
    vector.append(i)

# Convertir lista de Python a un array de ctypes
vector_c = (ctypes.c_double * len(vector))(*vector)
resultado_c = (ctypes.c_double * len(vector))()

# Llamando a la función
fun.vectorScalarMultiply(vector_c, escalar, resultado_c, tamaño)

# Mostrando resultados
print("Original:", list(vector_c))
print("nuevo:", list(resultado_c))