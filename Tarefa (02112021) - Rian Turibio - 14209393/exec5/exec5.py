import numpy as np
import pandas as pd
# Generate some random data
data1 = pd.DataFrame(np.random.random((2, 2)))
print('Matriz Random 1')
print(data1)
print('\n')
data2 = pd.DataFrame(np.random.random((2, 2)))
print('Matriz Random 2')
print(data2)

res = data1 * data2
print('\n')
print('Matriz Resultado')
print(res)