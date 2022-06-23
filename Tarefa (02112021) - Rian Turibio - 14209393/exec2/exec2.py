from numpy import genfromtxt
import numpy as np
from numpy import loadtxt

file1 = open('matriz_1.csv', 'rb')
data1 = loadtxt(file1,delimiter = ",")
print(data1)

print("\n")

file2 = open('matriz_2.csv', 'rb')
data2 = loadtxt(file2,delimiter = ",")
print(data2)

a = np.array(data1)
b = np.array(data2)

print("\n")
print("Soma:")
# SE NAO FOR MATRIZES DO MESMO TAMANHO NAO SOMA !!!!!!
#print("Dimensoes Incorretas:")
print (np.add(data1,data2))

print("\n")
print("Multiplicacao:")
print (np.dot(data1,data2))