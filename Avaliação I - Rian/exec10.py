
import numpy as np
import pandas as pd

tabela_1 = pd.DataFrame({
'Nome':['João', 'João', 'Pedro' , 'Caio'], 
'Telefone': ['12121', '343434', '565656', '787878'], 
'Carros': ['azul', 'preto', 'verde' , 'amarelo']})
print(tabela_1)

tabela_2 = pd.DataFrame({
'Nome':['João', 'Marcelo', 'Thiago' , 'Caio'],  
'Irmãos': ['1', '3', '2' , '2']})
print(tabela_2)

df = pd.merge(tabela_1, tabela_2, how = 'inner', on = 'Nome')
print(df)

print(df.Carros.iloc[2])

print(df.loc[(df.Nome == "João")])

