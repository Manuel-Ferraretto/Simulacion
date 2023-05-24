import matplotlib.pyplot as plt
from tests import chi_cuadrado
from generadores.middle_square import middle_square
from generadores.GCL import linear_congruential


def dispersion_2d(generador):
    iterador = generador()
    x = [next(iterador)]
    y = []
    for n in iterador:
        x.append(n)
        y.append(n)
    x.pop()

    ax = plt.axes()
    ax.set_xlabel('Xi')
    ax.set_ylabel('X(i+1)')
    ax.scatter(x, y)
    plt.show()


#dispersion_2d(middle_square)
dispersion_2d(linear_congruential)
