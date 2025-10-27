import pandas as pd
import numpy as np

df = pd.read_csv('movies_metadata_v2.csv', encoding='iso-8859-1').dropna(axis=1, how='all')
print(df.head())
print(df.shape)
print(df.info()) # summary of columns

# Fill in brackets with a CONDITIONAL
budget_df = df[df['budget'] > 1_000_000]
print(budget_df.shape)

# Create the Series + print the rows
budget_lookup = pd.Series(data=df['budget'].values, index=df['title'])
print(budget_lookup.head())

# First define the condition to be checked
condition = (budget_lookup.index == 'A Movie') | (budget_lookup.index == 'B Movie')
budget_lookup_A_B = budget_lookup[condition]
print(budget_lookup_A_B)