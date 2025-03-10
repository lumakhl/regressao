# Alex Seródio, Luma Kühl, Matheus Losi e Thiago Angioletti

import matplotlib.pyplot as plt
import utils
import numpy
import gerador_graficos

# g) 0.058709346973616884 -> melhor é utilizando como parametro n = 8
# k) 6273104.076547174 -> neste caso é utilizando como parametro n = 3

# Calculo de Erro Quadratico Minimo
def eqm(y, n):
    residuo = (y-n)**2
    return sum(residuo)/len(y)

# Dados
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5,
     2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 5.1, 5.2]
y = [0.25806, 0.50855, 0.79357, 0.55773, 0.99226, 1.1906, 0.78639, 0.76164, 1.014, 1.1021, 1.2656, 1.3991, 1.0176, 1.226, 1.7865, 1.0267, 1.9284, 1.722, 1.4625, 1.5248, 1.1466, 1.3221, 1.7716, 1.2925, 1.1966, 0.83007, 1.0044, 1.0514, 1.0141,
     0.63476, 0.50856, 1.0296, -0.020635, 0.72742, 0.65775, 0.4454, -0.34381, -0.26796, -0.2765, -0.0080382, -0.62025, -0.09705, -0.76481, -0.26241, -0.45743, -0.19848, -0.27865, -0.096203, -0.10524, -0.64829, -0.26018, -0.728, -0.85291]

# Separa em treinamento e teste
corte = int(len(y)*0.1)-1
xTreinamento = []
yTreinamento = []
xTeste = []
yTeste = []

for key, i in enumerate(y):
    if key > corte:
        xTreinamento.append(x[key])
        yTreinamento.append(y[key])
    else:
        xTeste.append(x[key])
        yTeste.append(y[key])

# Função para fazer polyfit de acordo com dados passados
def p(x, y, i):
    return numpy.polyfit(x, y, i)


# Função para gerar os gráficos
def gerarGrafico(x, y, title):
    plt.scatter(x, y)

    # Desenhando o polinomio para cada um dos n's
    plt.plot(x, numpy.polyval(p(x, y, 1), x), 'r')
    plt.plot(x, numpy.polyval(p(x, y, 2), x), 'g')
    plt.plot(x, numpy.polyval(p(x, y, 3), x), 'k')
    plt.plot(x, numpy.polyval(p(x, y, 8), x), 'y')
    plt.title(title)
    plt.show()


# Calculando EQM para todos os dados
print('EQM para todos os dados:')
print(eqm(y, numpy.polyval(p(x, y, 1), x)))
print(eqm(y, numpy.polyval(p(x, y, 2), x)))
print(eqm(y, numpy.polyval(p(x, y, 3), x)))
print(eqm(y, numpy.polyval(p(x, y, 8), x)))
# Grafico dispersao para todos os dados
gerarGrafico(x, y, "Regrassão Polinomial")

# i)
# Grafico com dados de treinamento
gerarGrafico(xTreinamento, yTreinamento, "Regrassão Polinomial - Treinamento")

# j)
# Calculando EQM para dados de teste
print('EQM para todos os dados de teste:')
print(eqm(y, numpy.polyval(p(xTeste, yTeste, 1), x)))
print(eqm(y, numpy.polyval(p(xTeste, yTeste, 2), x)))
print(eqm(y, numpy.polyval(p(xTeste, yTeste, 3), x)))
print(eqm(y, numpy.polyval(p(xTeste, yTeste, 8), x)))
