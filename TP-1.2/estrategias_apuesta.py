import random as ran
from turtle import right
import numpy as np
import matplotlib.pyplot as plt
import statistics
from statistics import fmean

res = []
valoresMar = []
valoresDal = []
valoresPar = []
numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


def girarRuleta(num_giros):
    resultados = []

    for i in range(0, num_giros):
        resultados.append(ran.randint(0, 36))

    return resultados


def martingala(res, capInicial, apuesta_min):
    cap_total = []
    a = []
    bolsillo = capInicial - apuesta_min
    apuesta = apuesta_min

    for nro in res:
        a.append(apuesta)
        cap_total.append(bolsillo)
        if (nro in numeros_rojos):
            bolsillo += apuesta * 2
            apuesta = apuesta_min
        else:
            apuesta = apuesta * 2
            bolsillo -= apuesta
    return cap_total, a


def dalembert(res, capInicial, unidad_base):
    cap_total = []
    a = []
    bolsillo = capInicial - unidad_base
    apuesta = unidad_base

    for nro in res:

        a.append(apuesta)
        cap_total.append(bolsillo)

        if (nro in numeros_rojos):
            bolsillo += apuesta * 2
            if (apuesta != unidad_base):
                apuesta -= unidad_base
            bolsillo -= apuesta
        else:
            apuesta += unidad_base
            bolsillo -= apuesta

    return cap_total, a


def Paroli(res, capInicial, unidad_base):
    cap_total = []
    a = []
    cont = 0
    bolsillo = capInicial - unidad_base
    apuesta = unidad_base

    for nro in res:

        a.append(apuesta)
        cap_total.append(bolsillo)

        if (nro in numeros_rojos):
            bolsillo += apuesta * 2
            cont += 1
            if (cont == 3):
                cont = 0
                apuesta = unidad_base
            else:
                apuesta *= 2
            bolsillo -= apuesta
        else:
            cont = 0
            apuesta = unidad_base
            bolsillo -= apuesta

    return cap_total, a


def calcularFR(res, giros, simu):
    fr = []
    for j in range(0, simu):
        fr.append([])
        for i in range(0, giros):
            fr[j].append(0)
        cont = 0
        for i in range(1, giros + 1):
            if (res[j][i - 1] in numeros_rojos):
                cont += 1
            fr[j][i - 1] += cont / i

    fr.append([])
    for i in range(0, giros):
        acc = 0
        for j in range(0, simu):
            acc += fr[j][i]
        fr[simu].append(acc / simu)

    return fr


def graficar(valores, capInicial, apuesta_min, giros, simu, title):
    fig, ax = plt.subplots(2)
    x = []
    fig.suptitle(title, fontsize=24)
    for i in range(giros):
        x.append(i)
    ax[0].axhline(y=capInicial, color='black', label="Capital \ninicial")
    ax[0].axhline(y=0, color='red')
    ax[0].set_xlabel("Tiradas")
    ax[0].set_ylabel("Capital")
    ax[1].axhline(y=apuesta_min, color='black', label="Apuesta \nminíma")
    ax[1].set_xlabel("Tiradas")
    ax[1].set_ylabel("Apuestas")
    for i in range(0, simu * 2):
        if (i % 2 == 0):
            ax[0].plot(valores[i])
        else:
            ax[1].scatter(x, valores[i], s=5)
    ax[0].legend(bbox_to_anchor=(1.11, 0.6), ncol=2)
    ax[1].legend(bbox_to_anchor=(1.12, 0.6), ncol=2)
    plt.show()


def graficarFR(fr, simu):
    fig, ax = plt.subplots(2)
    fig.suptitle("Frecuencias relativas números rojos", fontsize=24)
    ax[0].axhline(y=18 / 37, color='black', label="Frecuencia \nesperada")
    ax[0].set_ylabel("Frecuencias relativas")
    ax[0].set_xlabel("Tiradas")
    ax[1].axhline(y=18 / 37, color='black', label="Frecuencia \nesperada")
    ax[1].set_ylabel("Frecuencia relativa promedio")
    ax[1].set_xlabel("Tiradas")

    for i in range(0, simu):
        ax[0].plot(fr[i])
    ax[1].plot(fr[simu])
    ax[0].legend(bbox_to_anchor=(1.12, 0), ncol=2)
    ax[0].set_ylim(0, 1)
    ax[1].set_ylim(0, 1)
    plt.show()


simu = int(input('Ingresar cantidad de simulaciones: '))
giros = int(input('Ingresar cantidad de tiradas: '))
capInicial = int(input('Ingresar capital disponible: '))
apuesta_min = int(input('Ingresar apuesta mínima: '))

for i in range(0, simu):
    res.append(girarRuleta(giros))
    valoresMar.extend(martingala(res[i], capInicial, apuesta_min))
    valoresDal.extend(dalembert(res[i], capInicial, apuesta_min))
    valoresPar.extend(Paroli(res[i], capInicial, apuesta_min))

fr = calcularFR(res, giros, simu)
graficarFR(fr, simu)
graficar(valoresMar, capInicial, apuesta_min, giros, simu, "El sistema Martingala")
graficar(valoresDal, capInicial, apuesta_min, giros, simu, "El sistema D'Alembert")
graficar(valoresPar, capInicial, apuesta_min, giros, simu, "El sistema Paroli")


