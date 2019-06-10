# Alex Seródio, Luma Kühl, Matheus Losi e Thiago Angioletti
import matplotlib.pyplot as plt
import numpy
import math
from mpl_toolkits import mplot3d
import csv

# Matriz para as váriaveis independentes
X = []

# Matriz para variável dependente
y = []

# Matriz com variável independente qtde de quartos
x_quartos = []

# Matriz com variável independente tamanho
x_tamanho = []

# Obtém os dados lendo arquivo CSV
def ler_csv():
    with open('.\data.csv','rt')as f:
        data = csv.reader(f)
        for row in data: 
            t = [int(row[0]),int(row[1])]
            X.append(t)
            y.append(float(row[2].replace('e+05','')))

# Lê arquivo csv
ler_csv()

# Adiciona para matriz de valores independentes
for item in X:
    x_tamanho.append(item[0])
    x_quartos.append(item[1])

# Calcula media de itens de uma matriz
def media(x):
        return sum(x)/len(x)

# Calcula correlação
def correlacao(X,Y):
    soma = 0
    divisao = 0
    r = 0

    somaX = 0
    somaY = 0

    # Para cada item X faz o calculo de somatorio
    for i in range(len(X)):
        # calcula a multiplicação de X[i] - media de X por Y[i] - media de Y    
        soma += (X[i] - media(X)) * (Y[i] - media(Y)) 
        # calcula a multiplicação de X[i] - media de X elevado ao quadrado
        somaX += (X[i] - media(X)) ** 2
        # calcula a multiplicação de Y[i] - media de Y elevado ao quadrado
        somaY += (Y[i] - media(Y)) ** 2
   
    #  Σ(x−x̄)(y−ȳ) / √(Σ(x−x̄)2  Σ(y−ȳ)2)        
    r = soma / math.sqrt(somaX * somaY)   
    return r

# Calcula 𝛽0 = 𝑦̄ − β1𝑥̄ 
def B0(X,Y):
    return (media(Y) - (B1(X,Y)*media(X)))

# Calcula 𝛽1= Σ(x−x̄)(y−ȳ)/Σ(x−x̄)2
def B1(X,Y):
    soma = 0
    somaX = 0

    # Para cada item X faz o calculo de somatorio  
    for i in range(len(X)):
        # calcula a multiplicação de X[i] - media de X por Y[i] - media de Y 
        soma += (X[i] - media(X)) * (Y[i] - media(Y)) 
        # calcula a multiplicação de X[i] - media de X elevado ao quadrado        
        somaX += (X[i] - media(X)) ** 2
    return soma / somaX

# Calcula reta de regressão 𝑦̂=𝛽0+𝛽1𝑥 
def regressao(X,Y):
        regrassao = []
        for i in range(len(X)):
                regrassao.append(coeficienteRegressao(X,Y,i))
        return regrassao

# Calcula coeficiente de regressão
def coeficienteRegressao(X,Y,i):
        return B0(X,Y) + (B1(X,Y) * X[i])

# 𝛽= (Xt X)-1 Xty 
# Calcula Regressão Linear Multipla utilizando a multiplicação de matrizes de numpy
def regmultipla(y,X):
        return numpy.matmul(X, B(X,y))
        
def B(X,y):
        # Cria matriz transposta de X
        matrizT = numpy.transpose(X)

        # Gera a matriz inversa resultante da multiplicação de X transposta e X
        matrizInversa = numpy.linalg.inv(numpy.matmul(matrizT, X))

        # Gera uma nova matriz resultante da multiplicação da matriz transposta de X por Y
        matrizTY = numpy.matmul(matrizT,y)
        return numpy.matmul(matrizInversa,matrizTY)

def gerarGrafico(x,y):
    plt.scatter(x,y)
    plt.plot(x,regressao(x,y))
    plt.title("Regressão Linear")
    plt.show()

def gerarGrafico3d(x,y,z):
    ax = plt.axes(projection='3d') 

    ax.scatter3D(x,y,z)
    ax.plot(x, z, regmultipla(y,X),'k')
    plt.show() 

gerarGrafico(x_tamanho,y)
gerarGrafico(x_quartos,y)

gerarGrafico3d(x_tamanho, x_quartos, y)
