from collections import Counter
import numpy as np
import pandas as pd

file = open("ciência_de_dados.txt", "r")
data = file.read()
words = data.split()

#print('\n')
#print("Letras:")
#print(Counter(data))

print('\n')
print("Palavras:")
print(Counter(words))

print('\n')

df = pd.DataFrame(words)
print(df) 