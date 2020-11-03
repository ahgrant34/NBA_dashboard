import pandas as pd

df = pd.read_csv('data/bbref_df.csv')

df = df[df['Player'].notna()]

df.fillna(0, inplace=True)

df.to_csv('data/BBRef_data_clean.csv')

