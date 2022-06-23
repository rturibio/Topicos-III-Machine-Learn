import numpy as np
import pandas as pd

data = pd.read_csv('ex6.csv', chunksize=2000)
for chunk in data:
    print(chunk)
    i=0
    if (i == 0):
        chunk.to_csv('chunk_exec6(1).txt')
        i = i+1
        if (i == 1):
         chunk.to_csv('chunk_exec6(2).txt')    
         i = i+1
         if (i == 2):
             chunk.to_csv('chunk_exec6(3).txt')
             i = i+1
             if (i == 3):
                chunk.to_csv('chunk_exec6(4).txt')
                i = i+1
                if (i == 4):
                 chunk.to_csv('chunk_exec6(5).txt')