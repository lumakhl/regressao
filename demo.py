import matplotlib.pyplot as plt
import utils

def gerarGrafico(x,y):

    plt.scatter(x,y)
    plt.plot(x,utils.regressao(x,y))
    plt.title("Regressão Linear" + "Coeficiente de Correlação " + str(utils.correlacao(x,y)) + " Coeficiente de Regressão " + str(utils.B1(x,y)))
    plt.show()

print(utils.regressao(utils.x2, utils.y2))
gerarGrafico(utils.x3, utils.y3)

    
