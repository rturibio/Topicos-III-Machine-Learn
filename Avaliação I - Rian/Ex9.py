
import numpy as np
import pandas as pd

vals = np.random.randint(0,100, size=(12, 4))
index_nivel1 = ['Classe A','Classe A','Classe A','Classe A', 'Classe B','Classe B','Classe B','Classe B', 'Classe C','Classe C','Classe C','Classe C']
index_nivel2 = ['Sub 1', 'Sub 2', 'Sub 3', 'Sub 4','Sub 1', 'Sub 2', 'Sub 3', 'Sub 4','Sub 1', 'Sub 2', 'Sub 3', 'Sub 4']
column_nivel1 = ['Bandeira Vermelha', 'Bandeira Vermelha', 'Bandeira Branca', 'Bandeira Branca']
column_nivel2 = ['Taxa 01', 'Taxa 02', 'Taxa 01', 'Taxa 02']
dataframe = pd.DataFrame(vals, index=[index_nivel1, index_nivel2], columns=[column_nivel1, column_nivel2])



print(dataframe)
print("######## Soma considerando o tipo de subestação (Sub) e tipo de taxa ###########")
print(dataframe.groupby(level=1, axis=0).sum())

print("######## Total em bandeiras brancas e total de vermelhas ####")
print(dataframe.groupby(level=0, axis=1).sum().sum())

print("######## Média considerando o tipo de subestação (Sub) e tipo de taxa ###########")
print(dataframe.groupby(level=1, axis=0).mean())

print("######## Média total (Taxa) em bandeira branca e vermelha ###########")
print(dataframe.groupby(level=0, axis=1).mean().mean())

print("######## Min considerando o tipo de subestação (Sub) e tipo de taxa ###########")
print(dataframe.groupby(level=1, axis=0).min())

print("######## Min geral (Taxa) em bandeira branca e vermelha ###########")
print(dataframe.groupby(level=0, axis=1).min().min())

print("######## Max considerando o tipo de subestação (Sub) e tipo de taxa ###########")
print(dataframe.groupby(level=1, axis=0).max())

print("######## Max geral (Taxa) em bandeira branca e vermelha ###########")
print(dataframe.groupby(level=0, axis=1).max().max())