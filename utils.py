import math
import matplotlib
import numpy

def media(x):
        return sum(x)/len(x)

def correlacao(X,Y):
    soma = 0
    divisao = 0
    r = 0

    somaX = 0
    somaY = 0

    for i in range(len(X)):
        soma += (X[i] - media(X)) * (Y[i] - media(Y)) 
        somaX += (X[i] - media(X)) ** 2
        somaY += (Y[i] - media(Y)) ** 2
    r = soma / math.sqrt(somaX * somaY)   
    return r


def B0(X,Y):
    return (media(Y) - (B1(X,Y)*media(X)))

def B1(X,Y):
    soma = 0
    somaX = 0

    for i in range(len(X)):
        soma += (X[i] - media(X)) * (Y[i] - media(Y)) 
        somaX += (X[i] - media(X)) ** 2
    return soma / somaX

def regressao(X,Y):
        regrassao = []
        for i in range(len(X)):
                regrassao.append(coeficienteRegressao(X,Y,i))
        return regrassao

def coeficienteRegressao(X,Y,i):
        return B0(X,Y) + (B1(X,Y) * X[i])

def regmultipla(y,X):
        return numpy.matmul(X, B(X,y))
        
def B(X,y):
        matrizT = numpy.transpose(X)
        matrizInversa = numpy.linalg.inv(numpy.matmul(matrizT, X))

        matrizTY = numpy.matmul(matrizT,y)
        return numpy.matmul(matrizInversa,matrizTY)
       

                
x1 = [10,8,13,9,11,14,6,4,12,7,5]
y1 = [8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]

x2 = [10,8,13,9,11,14,6,4,12,7,5]
y2 = [9.14,8.14,8.47,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]     

x3 = [8,8,8,8,8,8,8,8,8,8,19] 
y3 = [6.58,5.76,7.71,8.84,8.47,7.04,5.25,5.56,7.91,6.89,12.50]

x4 = [164,246,310,328,426,580,590,700,721,820,918,930]
y4 = [50,75,90,100,130,160,180,200,220,250,280,300]


    


    