import pandas as pd

df = pd.read_csv ('books.csv')

to_drop = ['Edition Statement','Place of Publication','Title','Author','Flickr URL','Publisher', 'Corporate Author', 'Corporate Contributors',
           'Former owner', 'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks']

df.drop(columns=to_drop, inplace=True)

df.loc[1905:, 'Date of Publication'].head(10)
df['Date of Publication'].head(15)
regex = r'^(\d{4})' # to find any 4 digits at the beginning
date_num = df['Date of Publication'].str.extract(regex, expand=False)
date_num.head(15)
df['Date of Publication'] = pd.to_numeric(date_num, downcast='integer')
df['Date of Publication'].dtype
df = df[df['Date of Publication'].isnull() != True]
print(df)