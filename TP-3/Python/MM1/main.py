import statistics
import matplotlib as plt
from clases import Parameters
from metodos import *

def graficar(lista, titulo, p: Parameters, n):
    x, y = zip(*[x for x in lista])
    plt.title(titulo.format(n,p.mean_interarrival,p.mean_service))
    plt.plot(x, y, markersize=1, lw=1,color='b')
    plt.grid(True)
    plt.show()

def main():
    runs = 10
    mean_service = 1
    mean_interrarrival_ratio = 1.25
    q_limit = 1000
    num_delays_required = 100


    clientes_cola = []
    clientes_sistema = []
    tiempo_prom_cola = []
    tiempo_prom_sist = []
    uso_servidor = []
    frec_rechazos = []
    mean_interrarival = mean_service * mean_interrarrival_ratio
    params = Parameters(mean_interrarival, mean_service, num_delays_required, q_limit)

    for i in range(runs):
        system = ejecutar_simulacion(params)
        reporte(system, params)

        rta = estadisticas_finales(system, params)
        clientes_sistema.append(rta[0])  # Num promedio clientes en el sistema
        clientes_cola.append(rta[1])  # Num promedio clientes en cola
        tiempo_prom_sist.append(rta[2])  # Tiempo promedio de espera en el sistema
        tiempo_prom_cola.append(rta[3])  # Tiempo promedio de espera en la cola
        uso_servidor.append(rta[4])  # Utilizacion del servidor
        frec_rechazos.append(rta[5])  # Frecuencia de denegacion de servicio

    prom_clientes_cola = []
    prom_clientes_sistema = []
    prom_uso_servidor = []
    prom_demora_cola = []
    prom_demora_sist = []

    for i in range(runs):
        prom_clientes_cola.append([i, statistics.mean(clientes_cola[:i + 1])])
        prom_demora_cola.append([i, statistics.mean(tiempo_prom_cola[:i + 1])])
        prom_clientes_sistema.append([i, statistics.mean(clientes_sistema[:i + 1])])
        prom_demora_sist.append([i, statistics.mean(tiempo_prom_sist[:i + 1])])

        prom_uso_servidor.append([i, statistics.mean(uso_servidor[:i + 1])])

    # Graficar resultados
    graficar(prom_clientes_cola,
             "Número promedio de clientes en la cola para {} simulaciones con Tasa de arribo = {} y de servicio = {}",
             params, runs)
    graficar(prom_demora_cola,
             "Tiempo promedio de espera en la cola para {} simulaciones con Tasa de arribo = {} y de servicio = {}",
             params, runs)
    graficar(prom_clientes_sistema,
             "Número promedio de clientes en el sistema para {} simulaciones con Tasa de arribo = {} y de servicio = {}",
             params, runs)
    graficar(prom_demora_sist,
             "Tiempo promedio de espera en el sistema para {} simulaciones con Tasa de arribo = {} y de servicio = {}",
             params, runs)
    graficar(prom_uso_servidor,
             "Tiempo promedio de utilizacion del servidor para {} simulaciones con Tasa de arribo = {} y de servicio = {}",
             params, runs)