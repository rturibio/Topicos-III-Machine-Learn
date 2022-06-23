import pandas as pd
import numpy as np

df1 = pd.DataFrame({'Chave': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'Coluna 1': range(7)})
df2 = pd.DataFrame({'Chave': ['a', 'b', 'd'],'Coluna 2': range(3)})
#print(pd.merge(df1, df2))
df3 = pd.DataFrame({'Chave E': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'Coluna 1': range(7)})
df4 = pd.DataFrame({'Chave D': ['a', 'b', 'd'],'Coluna 2': range(3)})
print("Interna")
print(pd.merge(df3, df4, left_on='Chave E', right_on='Chave D'))
print("\n")
print("Externa")
print(pd.merge(df1, df2, how='outer'))