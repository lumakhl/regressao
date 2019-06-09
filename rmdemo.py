import matplotlib.pyplot as plt
import utils
import utils_multipla
from mpl_toolkits import mplot3d

def gerarGrafico(x,y):

    plt.scatter(x,y)
    plt.plot(x,utils.regressao(x,y))
    plt.title("Regressão Linear Multipla" + "Coeficiente de Correlação " + str(utils.correlacao(x,y)) + " Coeficiente de Regressão " + str(utils.B1(x,y)))
    plt.show()

def gerarGrafico3d(x,y,z):
    ax = plt.axes(projection='3d') 

    ax.scatter3D(x,y,z)

    ax.plot(utils_multipla.x_tamanho, utils_multipla.x_quartos, utils.regmultipla(utils_multipla.y,utils_multipla.X))

    plt.show()

gerarGrafico3d(utils_multipla.x_tamanho, utils_multipla.x_quartos, utils_multipla.y)
