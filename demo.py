# Alex Seródio, Luma Kühl, Matheus Losi e Thiago Angioletti
import math
import matplotlib
import numpy
import matplotlib.pyplot as plt

# 3) O terceiro dataset não é apropriada para regressão pelo formato dos seus dados que parecem ter pouca relação

# Dados
x1 = [10,8,13,9,11,14,6,4,12,7,5]
y1 = [8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]

x2 = [10,8,13,9,11,14,6,4,12,7,5]
y2 = [9.14,8.14,8.47,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]     

x3 = [8,8,8,8,8,8,8,8,8,8,19] 
y3 = [6.58,5.76,7.71,8.84,8.47,7.04,5.25,5.56,7.91,6.89,12.50]

x4 = [164,246,310,328,426,580,590,700,721,820,918,930]
y4 = [50,75,90,100,130,160,180,200,220,250,280,300]

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

# Gerar gráfico de dispersão
def gerarGrafico(x,y):

    plt.scatter(x,y)
    plt.plot(x,regressao(x,y))
    plt.title("Regressão Linear" + "Coeficiente de Correlação " + str(correlacao(x,y)) + " Coeficiente de Regressão " + str(B1(x,y)))
    plt.show()

gerarGrafico(x1, y2)
gerarGrafico(x2, y2) 
gerarGrafico(x3, y3)
gerarGrafico(x4, y4)


    


    