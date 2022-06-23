
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({"TAB1": ["A", "A", "A","A", "A", "B", "B", "B", "B", "B"],
                   "TAB2": ["K", "K", "J", "J", "K","K", "J", "J","K","J"],
                   "TAB3": [6, 3, 4, 2, 8, 7, 9, 0, 5, 1]})
print(df)
print("\n")
dfpivot = pd.pivot_table(df, values='TAB3',columns=['TAB2'], index=['TAB1'], aggfunc=np.sum)
print(dfpivot)

dfpivot.plot(kind='bar', title='Grafico de Barras Exec 11')
plt.show()