import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt

#pd.set_option('display.max_columns', 0)

path = open('2015_USPTOf.json')
data = json.load(path)

dataframe = pd.DataFrame.from_dict(data)

for index, row in dataframe['Subclass_labels'].items():
    for c in row:
        if c not in dataframe:
            dataframe[c] = 0
        dataframe.loc[index, c] = 1

dataframe_tograph = dataframe.drop(['Subclass_labels', 'Abstract', 'Title', 'No'], axis=1)
toplot_sorted = dataframe_tograph.sum().sort_values(ascending=False).head(10)
plt.figure()
toplot_sorted.plot(kind='barh')


path.close()