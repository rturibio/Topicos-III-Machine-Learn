import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(20).reshape((4, 5)),
index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
columns=[['SC', 'SC', 'RS', 'RS', 'PR'],
['Verde', 'Vermelho', 'Verde', 'Vermelho', 'Verde']])
frame.index.names = ['Chave1', 'Chave2']
frame.columns.names = ['Estado', 'Cor']
print(frame)
