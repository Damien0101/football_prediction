import pandas as pd

df = pd.read_csv('data/dataset.csv')
teams = df['HomeTeam'].unique()

print(teams)

