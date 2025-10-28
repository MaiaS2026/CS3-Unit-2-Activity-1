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
budget_lookup = pd.Series(data=df['budget'].values, index=budget_df['title'])
print(budget_lookup.head())

# First define the condition to be checked
condition = (budget_lookup.index == 'A Movie') | (budget_lookup.index == 'B Movie')
budget_lookup_A_B = budget_lookup[condition]
print(budget_lookup['Avatar'])

# PART C!!!
# Convert runtime to numeric
df['runtime'] = pd.to_numeric(df['runtime'])
# Filter movies between 10 and 180 minutes
df_filtered = df[(df['runtime'] >= 10) & (df['runtime'] <= 180)]
# Create the Series indexed by runtime
movies_by_runtime = pd.Series(df_filtered['title'].values, index=df_filtered['runtime'])
# Sort by runtime
movies_by_runtime = movies_by_runtime.sort_index()
# Print the Series
print(movies_by_runtime)
movies_by_runtime = pd.Series(df['title'].values, index=df['runtime'])
movies_by_runtime = movies_by_runtime.sort_index()
print(movies_by_runtime.loc[154])

# PART D
df_highly_voted = df[df.vote_count > 20]
df_high_rated = df_highly_voted[df_highly_voted.vote_average > 8]
df_high_rated[['title', 'vote_average', 'vote_count']].head()
print(df_high_rated)