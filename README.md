# Tarea2Infra

se ha creado la libreria dinamica con este comando en consola "gcc -mavx -fPIC -shared -o libmultescalar.so multescalar.c" para poder habilitar el uso de avx en mi maquina

para poder ver los tiempos de ejecucion de cada caso simplemente toca correr cada archivo .py

multescalar.py = caso de manejo avx en libreria dinamica

multescalarIngenua.py = implementacion ingenua 

multescalarNumpy = implementacion libreria Numpy

para modificar el tamaño del vector solo es necesario modificar "tamaño" dentro de cada archivo .py

el analisis de tiempo se realizo con timeit

para ver si el programa fucniona solo hay que descomentar las lineas print para cada caso en .py
