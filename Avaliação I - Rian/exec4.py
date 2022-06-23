
import pandas as pd
import numpy as np

df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'John'])
                         
print(df)

#'Height': [165, 170, 120, 80, 180, 172, 150],
df1 = pd.DataFrame({'Height': [165, 170, 120, 80, 180, 172, 150]},
                     index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'John'])
print(df1)

result =  df.join(df1)  #pd.concat([df, df1], axis=1, ignore_index=False)
print(result)

info = 0
while (info != 'sair'):
    print("Digite a Coluna ")
    info = int(input())
    print("Digite a linha ")
    info2 = int(input())
    
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if (i == info) & (j == info2):
                print(result.iloc[i,j])
                break