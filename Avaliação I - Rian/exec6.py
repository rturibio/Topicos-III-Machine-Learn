
import pandas as pd

df1 = {'A': [0, 1, 2, 3],
        'B': [4, 5, 6, 7]}

df1 = pd.DataFrame(df1)
print (df1)

df2 = {'A': [0, 1, 2, 3],
        'C': [15, 16, 17, 18]}

df2 = pd.DataFrame(df2)
print (df2)

df = df1.merge(df2, how='left', on='A')
print(df)

print(df.B.iloc[2])
print(df.loc[df.C == 17])