from numpy.random import randn
import numpy as np
np.random.seed(123)
import os
import matplotlib.pyplot as plt
import pandas as pd
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4)
pd.options.display.max_rows = 20
#pd.options.display.float_format = '${:,.2f}'.format

low_memory=False
fec = pd.read_csv('video_games.csv')
#print(fec.info())

#print(fec.iloc[25])

#metadata_publi = fec.Title.unique()
#print(metadata_publi)
#metadata_publi[0]

#print(fec.ReleaseConsole.value_counts()[:20])

#by_occupation = fec.pivot_table('MetricsReviewScore',
#                                index='ReleaseConsole',
#                                columns='MetadataGenres', aggfunc='sum')
#over_50 = by_occupation[by_occupation.sum(1) > 50]
#print(over_50)
#over_50.plot(kind='barh')
#plt.show()

fec_mrbo = fec[fec.ReleaseConsole.isin(['PlayStation 3','Sony PSP'])]
print(fec_mrbo)

#grouped = fec_mrbo.groupby(['ReleaseConsole', 'Publishers'])
#totals = grouped.MetricsUsedPrice.sum().unstack(0).fillna(0)
#totals = totals[totals.sum(1) > 1]
#print(totals)

#percent = totals.div(totals.sum(1), axis=0)
#print(percent[:50])
#percent[:50].plot(kind='bar')
#plt.show()