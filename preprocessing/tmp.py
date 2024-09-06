import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import seaborn as sns


df = pd.read_csv('data/dataset.csv')


new_df =df.drop(['Div','B365H','B365D','B365A','BWH','BWD','BWA','WHH','WHD',
         'WHA', 'HTR','MaxH','MaxD', 'MaxA', 'B365>2.5', 'B365<2.5', 'Max>2.5',
         'Max<2.5', 'AHh','B365AHH', 'B365AHA', 'PAHH', 'PAHA', 'MaxAHH',
         'MaxAHA', 'AvgAHH', 'AvgAHA', 'B365CH', 'B365CD', 'B365CA', 'BWCH',
         'BWCD', 'BWCA','PSCH', 'PSCD', 'PSCA', 'WHCH', 'WHCD', 'WHCA', 'MaxCH',
         'MaxCD', 'MaxCA', 'AvgCH', 'AvgCD', 'AvgCA', 'B365C>2.5', 'B365C<2.5', 
         'PC>2.5', 'PC<2.5', 'MaxC>2.5', 'MaxC<2.5', 'AvgC>2.5', 'AvgC<2.5', 'AHCh',
            'B365CAHH', 'B365CAHA', 'PCAHH', 'PCAHA', 'MaxCAHH', 'MaxCAHA', 'AvgCAHH',
            'AvgCAHA', 'P>2.5', 'Avg>2.5', 'Avg<2.5'], axis=1)
new_df.dropna(inplace=True)

ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False).set_output(transform='pandas')
ohetransform = ohe.fit_transform(new_df[['FTR']])
new_df = pd.concat([new_df, ohetransform], axis=1)


numeric_columns = new_df.select_dtypes(include=[np.number]).columns
data = new_df[numeric_columns].drop(columns=[],errors='ignore')

corr_matrix = data.corr(method='pearson')

plt.figure(figsize=(20, 20))
heatmap = sns.heatmap(corr_matrix, 
                      cmap = 'icefire',
                      annot=True,
                       fmt = '.2f',
                        linewidths=.5,
                        cbar_kws={"shrink": .8},
                        annot_kws={"size": 10})

plt.title('Correlation Heatmap')
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

plt.show()
new_df.to_csv('data/cleaned_dataset.csv', index=False)