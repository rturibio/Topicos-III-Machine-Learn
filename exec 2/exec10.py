from numpy import genfromtxt
import numpy as np
from numpy import loadtxt
import csv
import pandas as pd

df = pd.read_csv("games-data.csv")
print(df)
print("\n")

sum1 = df['critics'].sum()
print ('Soma das Criticas: ' + str(sum1))
mean1 = df['critics'].median()
print ('Media de criticas: ' + str(mean1))
print("\n")

sum2 = df['score'].sum()
print ('Soma do score: ' + str(sum2))
mean2 = df['score'].median()
print ('Media do score: ' + str(mean2))
print("\n")

max1 = df['score'].max()
min1 = df['score'].min()
print ('Score Maximo: ' + str(max1))
print ('Score Minimo: ' + str(min1))
print("\n")
