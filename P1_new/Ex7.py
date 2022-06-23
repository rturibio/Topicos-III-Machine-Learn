import numpy as np
import pandas as pd

dataframe = pd.DataFrame(np.random.randint(-100,100, size=(500, 4)), columns=['C1', 'C2', 'C3', 'C4'])

defined_number = 72

#Método usando clip
dataframe.clip(lower=-defined_number, upper=defined_number, inplace=True)

#Método por varredura [CASO POR VARREDURA FOSSE O OBJETIVO DO EXERCÍCIO]
#for (columnName, columnData) in dataframe.iteritems():
#    for index, data in enumerate(columnData):
#        if data > defined_number:
#            dataframe[columnName][index] = defined_number
#        elif data < (defined_number*-1):
#            dataframe[columnName][index] = defined_number*-1


for (columnName, columnData) in dataframe.iteritems():
    print("Max para coluna %s: %s" % (str(columnName), str(dataframe[columnName].max())))

for (columnName, columnData) in dataframe.iteritems():
    print("Min para coluna %s: %s" % (str(columnName), str(dataframe[columnName].min())))


print("######## Mínimo por coluna #########")
print(dataframe.min())
print("######## Máximo por coluna #########")
print(dataframe.max())
print("######## Soma por coluna #########")
print(dataframe.sum())
print("######## Média por coluna #########")
print(dataframe.mean())
print("######## Números únicos por coluna #########")
print(dataframe.nunique())
