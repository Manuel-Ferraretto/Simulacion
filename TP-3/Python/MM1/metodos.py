import math
import random as rn
import sys
import numpy as np
from clases import System, Parameters

cantidad_eventos = 2


def expon(media):
    U = rn.uniform(0, 1)
    return -(media) * math.log(U)


def inicializar(params: Parameters) -> System:
    sistema = System()
    sistema.tiempo = 0
    sistema.ocupado = False
    sistema.num_en_cola = 0
    sistema.ultimo_evento = 0
    sistema.num_clientes_atendidos = 0
    sistema.num_clientes_rechazados = 0
    sistema.total_demoras = 0
    sistema.tiempo_num_en_cola = dict()
    sistema.tiempo_ocupado = 0
    sistema.tipo_proximo_evento = 0
    sistema.tiempo_llegada = np.zeros([params.limite_q + 1])

    sistema.tiempo_proximo_evento = np.zeros([cantidad_eventos + 1])

    sistema.tiempo_proximo_evento[1] = sistema.tiempo + expon(1 / params.media_llegadas)
    sistema.tiempo_proximo_evento[2] = 10 ** 30

    return sistema


def tiempos(sistema: System):
    sistema.tipo_proximo_evento = 0
    min_tiempo_proximo_evento = 10 ** 29

    for i in range(1, cantidad_eventos + 1):
        if sistema.tiempo_proximo_evento[i] < min_tiempo_proximo_evento:
            min_tiempo_proximo_evento = sistema.tiempo_proximo_evento[i]
            sistema.tipo_proximo_evento = i

    if (sistema.tipo_proximo_evento > 0):
        sistema.tiempo = min_tiempo_proximo_evento

    if sistema.tipo_proximo_evento == 0:
        print("La lista de eventos está vacía en el momento: ", sistema.tiempo, " TipoProximoEvento == 0, error en timing")
        sys.exit()


def actualizar_estadisticas(sistema: System):
    tiempo_desde_ultimo_evento = sistema.tiempo - sistema.ultimo_evento
    sistema.ultimo_evento = sistema.tiempo
    if sistema.num_en_cola not in sistema.tiempo_num_en_cola.keys():
        sistema.tiempo_num_en_cola[sistema.num_en_cola] = 0
    sistema.tiempo_num_en_cola[sistema.num_en_cola] += tiempo_desde_ultimo_evento
    sistema.tiempo_ocupado += sistema.ocupado * tiempo_desde_ultimo_evento


def arribo(sistema: System, params: Parameters):
    sistema.tiempo_proximo_evento[1] = sistema.tiempo + expon(1 / params.media_llegadas)
    if sistema.ocupado:
        if sistema.num_en_cola >= params.limite_q:
            sistema.num_clientes_rechazados += 1
        else:
            sistema.num_en_cola += 1

def salida(sistema: System, params: Parameters):
    if sistema.num_en_cola == 0:
        sistema.ocupado = False
        sistema.tiempo_proximo_evento[2] = 10 ** 30
    else:
        sistema.num_en_cola -= 1
        demora = sistema.tiempo - sistema.tiempo_llegada[1]
        sistema.total_demoras += demora
        # Incrementa el número de clientes retrasados.
        sistema.num_clientes_atendidos += 1
        # Programa partida al finalizar servicio.
        sistema.tiempo_proximo_evento[2] = sistema.tiempo + expon(1 / params.media_servicio)
        for I in range(1, sistema.num_en_cola + 1):
            sistema.tiempo_llegada[I] = sistema.tiempo_llegada[I + 1]


def mostrar(titulo, valor, unidad=None):
    print("{:50}: {} {}".format(titulo, valor, unidad or ""))


def ejecutar_simulacion(params: Parameters) -> System:
    sistema = inicializar(params)

    while sistema.num_clientes_atendidos < params.num_demoras_requeridas:
        tiempos(sistema)
        actualizar_estadisticas(sistema)
        if sistema.tipo_proximo_evento == 1:
            arribo(sistema, params)
        elif sistema.tipo_proximo_evento == 2:
            salida(sistema, params)
    return sistema


def estadisticas_finales(sistema: System, params: Parameters):
    area_total_num_en_cola = sum(num_en_cola * tiempo_en_cola for num_en_cola, tiempo_en_cola in sistema.tiempo_num_en_cola.items())
    promedio_demora_cola = sistema.total_demoras / sistema.num_clientes_atendidos
    promedio_num_cola = area_total_num_en_cola / sistema.tiempo
    promedio_tiempo_sistema = (area_total_num_en_cola + sistema.tiempo_ocupado) / sistema.num_clientes_atendidos
    promedio_num_sistema = (area_total_num_en_cola + sistema.tiempo_ocupado) / sistema.tiempo
    frecuencia_rechazo = sistema.num_clientes_rechazados / (params.num_demoras_requeridas + sistema.num_clientes_rechazados)
    utilizacion_servidor = sistema.tiempo_ocupado / sistema.tiempo

    return [promedio_num_sistema, promedio_num_cola, promedio_tiempo_sistema, promedio_demora_cola, utilizacion_servidor, frecuencia_rechazo]


def reporte(sistema: System, params: Parameters):
    promedio_num_sistema, promedio_num_cola, promedio_tiempo_sistema, promedio_demora_cola, utilizacion_servidor, frecuencia_rechazo = \
        estadisticas_finales(sistema, params)
    tiempo_en_hs = sistema.tiempo / 60
    mostrar("Número promedio de clientes en el sistema (L)", promedio_num_sistema, "clientes/minuto")
    mostrar("Número promedio de clientes en cola (Lq)", promedio_num_cola, "clientes/minuto")
    mostrar("Tiempo promedio de espera en el sistema (W)", promedio_tiempo_sistema, "minutos")
    mostrar("Tiempo promedio de espera en cola (Wq)", promedio_demora_cola, "minutos")
    mostrar("Utilización de servidor", utilizacion_servidor)
    mostrar("Frecuencia de denegación de servicio", frecuencia_rechazo)
    for num_en_cola, tiempo_en_cola in sistema.tiempo_num_en_cola.items():
        frecuencia_num_cola = tiempo_en_cola / sistema.tiempo
        mostrar("Frecuencia de %d clientes en cola" % num_en_cola, frecuencia_num_cola)