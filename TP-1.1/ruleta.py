import matplotlib.pyplot as plt
import random
from statistics import *
from math import *
from itertools import *

# Crear una lista vacía para almacenar los resultados de las tiradas
corridas_promedios = []
cantidad_tiradas = 1000


def promedio_por_tirada(cantidad_tiradas):
    tiradas_promedios = []
    resultados = []
    for i in range(cantidad_tiradas):  # for para las tiradas
        # Generamos un número aleatorio entre 0 y 36
        resultado_tirada = random.randint(0, 36)
        resultados.append(resultado_tirada)
        tiradas_promedios.append(mean(resultados))  # Se guarda el promedio luego de cada tirada
    corridas_promedios.append(mean(resultados))
    return tiradas_promedios


def grafica_promedio(tiradas_promedios, cantidad_tiradas):
    plt.plot(range(0, cantidad_tiradas), tiradas_promedios)
    plt.xlabel("Numero de tirada")
    plt.ylabel("Promedio")
    plt.title("Evaluacion del promedio sobre el conjunto de valores aleatorios")


def grafica_promedios(corridas_promedios, cantidad_corridas):
    plt.plot(range(0, cantidad_corridas), corridas_promedios, marker='o', color='r')
    plt.xlabel("Numero de corrida")
    plt.ylabel("Promedio")
    plt.title("Evaluacion de la media aritmetica de cada corrida")
    plt.grid()


def frecuencia_por_tirada(cantidad_tiradas):
    tiradas_frecuencia = []
    resultados = []
    for i in range(cantidad_tiradas):  # for para las tiradas
        # Generamos un número aleatorio entre 0 y 36
        resultado_tirada = random.randint(0, 36)
        resultados.append(resultado_tirada)
        tiradas_frecuencia.append(resultados.count(resultado_tirada) / len(resultados))
    return tiradas_frecuencia


def grafica_frecuencia(tiradas_frecuencia, cantidad_tiradas):
    plt.plot(range(0, cantidad_tiradas), tiradas_frecuencia)
    plt.xlabel("Numero de tirada")
    plt.ylabel("Frecuencia")
    plt.title("Evaluacion de la frecuencia sobre el conjunto de valores aleatorios")


def frecuencia_por_corrida(cantidad_tiradas):
    corridas_frecuencias = []
    resultados = []
    for i in range(cantidad_tiradas):  # for para las tiradas
        # Generamos un número aleatorio entre 0 y 36
        resultado_tirada = random.randint(0, 36)
        resultados.append(resultado_tirada)
    for i in range(0, 36):
        corridas_frecuencias.append(resultados.count(i) / cantidad_tiradas)
    return corridas_frecuencias


def grafica_frecuencias(corridas_frecuencias, cantidad_tiradas):
    plt.plot(range(0, 36), corridas_frecuencias)
    plt.axhline(y=1 / 37, color="gray")
    plt.xlabel("Numeros obtenidos")
    plt.ylabel("Frecuencia")
    plt.title("Evaluacion de la frecuencia sobre el conjunto de valores aleatorios")


def desvio_por_tirada(cantidad_tiradas):
    tiradas_desvio = []
    resultados = []
    for i in range(cantidad_tiradas):  # for para las tiradas
        # Generamos un número aleatorio entre 0 y 36
        resultado_tirada = random.randint(0, 36)
        resultados.append(resultado_tirada)
        tiradas_desvio.append(pstdev(resultados))  # stdev calcula el desvio poblacional
    return tiradas_desvio


def grafica_desvio(tiradas_desvio, cantidad_tiradas):
    plt.plot(range(0, cantidad_tiradas), tiradas_desvio)
    plt.xlabel("Numero de tirada")
    plt.ylabel("Desvio")
    plt.title("Evaluacion del desvio sobre el conjunto de valores aleatorios")


def varianza_por_tirada(cantidad_tiradas):
    tiradas_varianza = []
    resultados = []
    for i in range(cantidad_tiradas):  # for para las tiradas
        # Generamos un número aleatorio entre 0 y 36
        resultado_tirada = random.randint(0, 36)
        resultados.append(resultado_tirada)
        tiradas_varianza.append(pvariance(resultados))
    return tiradas_varianza


def grafica_varianza(tiradas_varianza, cantidad_tiradas):
    plt.plot(range(0, cantidad_tiradas), tiradas_varianza)
    plt.xlabel("Numero de tirada")
    plt.ylabel("Varianza")
    plt.title("Evaluacion de la varianza sobre el conjunto de valores aleatorios")


cantidad_corridas = int(input("Ingrese cantidad de corridas: "))
for j in range(cantidad_corridas):
    grafica_promedio(promedio_por_tirada(cantidad_tiradas), cantidad_tiradas)
plt.show()
grafica_promedios(corridas_promedios, cantidad_corridas)
plt.show()
for j in range(cantidad_corridas):
    grafica_frecuencia(frecuencia_por_tirada(cantidad_tiradas), cantidad_tiradas)
plt.show()
for j in range(cantidad_corridas):
    grafica_frecuencias(frecuencia_por_corrida(cantidad_tiradas), cantidad_tiradas)
plt.show()
for j in range(cantidad_corridas):
    grafica_desvio(desvio_por_tirada(cantidad_tiradas), cantidad_tiradas)
plt.show()
for j in range(cantidad_corridas):
    grafica_varianza(varianza_por_tirada(cantidad_tiradas), cantidad_tiradas)
plt.show()






