
import pandas as pd
import numpy as np

df = pd.read_csv('movie.csv', error_bad_lines=False, header=None , delimiter=';')
print(df)

df2 = df

df2m = pd.DataFrame(df2[2].str.split('|').tolist(), columns=['A','B','C','D','E','F'])
print(df2m)

merge1 = df.join(df2m)
print(merge1)

print(merge1.loc[merge1['A'] == 'Drama'])

print(merge1.loc[66])