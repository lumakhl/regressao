#import necessary modules
import csv

X = []
y = []

x_quartos = []
x_tamanho = []

def ler_csv():
    with open('.\data.csv','rt')as f:
        data = csv.reader(f)
        for row in data: 
            t = [int(row[0]),int(row[1])]
            X.append(t)
            y.append(float(row[2].replace('e+05','')))

ler_csv()

for item in X:
    x_tamanho.append(item[0])
    x_quartos.append(item[1])


            