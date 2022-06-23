import sys
from matplotlib import pyplot as plt
import networkx as nx
import pandas as pd

grafo = '''
A1nC,A2nC,4
A1nC,A3nC,3
A1nC,A1n2,9
A1n2,A1n4,3
A1nC,A1n3,19
A1n3,A1n4,13
A1n2,A1n3,34
A2nC,A3nC,55
A2nC,A2n1,64
A2n1,A2n3,77
A2n3,A2n5,85
A2nC,A2n2,24
A2n2,A2n4,4
A2n4,A2n5,5
A3nC,A3n1,8
A3n1,A3n4,3
A3n4,A3n7,4
A3nC,A3n2,5
A3n2,A3n3,66
A3n2,A3n5,59
A3n5,A3n7,33
A3nC,A3n3,99
'''

plotgraf = nx.Graph()
for line in grafo.strip().split('\n'):
  (n1, n2, w) = line.split(',')
  plotgraf.add_edge(n1, n2, weight=float(w))

nx.draw_networkx(plotgraf)
plt.show()

print("")
print("betweenness")
print(nx.betweenness_centrality(plotgraf))
betweenness = nx.betweenness_centrality(plotgraf)
print("")
print("relevant betweenness")
print(sorted(betweenness.items(), reverse= True, key=lambda x: x[1])[:5])

print("")
print("closeness")
print(nx.closeness_centrality(plotgraf))
closeness = nx.closeness_centrality(plotgraf)
print("")
print("relevant closeness")
print(sorted(closeness.items(), reverse= True, key=lambda x: x[1])[:5])
