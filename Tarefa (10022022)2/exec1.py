import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from scipy.spatial.distance import squareform, pdist

data = pd.read_csv('weka-transacao.csv')
print(data)

dist = pd.DataFrame(squareform(pdist(data[['V1', 'V2']]), 'euclidean'), columns=data.index.values, index=data.index.values)
print(dist)

plt.figure(figsize=(12,5)) 
plt.title("Dendrogram with Single inkage")  
dend = shc.dendrogram(shc.linkage(data[['V1', 'V2']], method='single'), labels=data.index)
plt.show()