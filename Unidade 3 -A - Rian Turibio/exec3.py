import pandas as pd

df = pd.read_csv ('books.csv')

df.info()

df.index

df.set_index('Identifier', inplace=True)