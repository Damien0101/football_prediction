import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import seaborn as sns


df = pd.read_csv('data/dataset.csv')


new_df =df.drop(['Div','Date','Time','B365H','B365D','B365A','BWH','BWD','BWA','WHH','WHD',
         'WHA', 'HTR','MaxH','MaxD', 'MaxA', 'B365>2.5', 'B365<2.5', 'Max>2.5',
         'Max<2.5', 'AHh','B365AHH', 'B365AHA', 'PAHH', 'PAHA', 'MaxAHH',
         'MaxAHA', 'AvgAHH', 'AvgAHA', 'B365CH', 'B365CD', 'B365CA', 'BWCH',
         'BWCD', 'BWCA','PSCH', 'PSCD', 'PSCA', 'WHCH', 'WHCD', 'WHCA', 'MaxCH',
         'MaxCD', 'MaxCA', 'AvgCH', 'AvgCD', 'AvgCA', 'B365C>2.5', 'B365C<2.5', 
         'PC>2.5', 'PC<2.5', 'MaxC>2.5', 'MaxC<2.5', 'AvgC>2.5', 'AvgC<2.5', 'AHCh',
            'B365CAHH', 'B365CAHA', 'PCAHH', 'PCAHA', 'MaxCAHH', 'MaxCAHA', 'AvgCAHH',
            'AvgCAHA', 'P>2.5', 'Avg>2.5', 'Avg<2.5'], axis=1)
new_df.dropna(inplace=True)

new_df['FTR'] = new_df['FTR'].map({'H': 1, 'D': 0, 'A': -1})

new_df.to_csv('data/cleaned_dataset.csv', index=False)