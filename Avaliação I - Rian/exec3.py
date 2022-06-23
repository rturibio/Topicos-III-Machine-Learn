
import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.randint(low=0,high=100,size=(5,5)))
print(data)

np.savetxt('exec3.txt', data, fmt="%d", comments='')
print('\n')

df = pd.read_csv('exec3.txt', sep=" ",header=None)
print(df)

sum =0

for x in range (len(df)):
    for y in range (len(df[x])):
        if x == y:
            sum = sum + df[x][y]

print("Traco: ")
print(sum)