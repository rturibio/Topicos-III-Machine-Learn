import pandas as pd

df = pd.read_csv ('books.csv')
print("Original 'books.csv' CSV Data: \n")
print(df)

df.drop('Corporate Author', inplace=True, axis=1)
df.drop('Corporate Contributors', inplace=True, axis=1)
df.drop('Former owner', inplace=True, axis=1)
df.drop('Engraver', inplace=True, axis=1)
  
# display 
print("\nCSV Data after deleting the columns':\n")
print(df)
