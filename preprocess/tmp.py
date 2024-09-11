import pandas as pd
import numpy as np



df = pd.read_csv('data/final_stats.csv')

if df['FTR'].dtype == 'object':
    df['FTR_numeric'] = pd.Categorical(df['FTR']).codes
else:
    df['FTR_numeric'] = df['FTR']


numerical_columns = df.select_dtypes(include=np.number).columns
correlation = df[numerical_columns].corr()


pd.set_option('display.max_columns', None) 
print("Correlation with 'FTR_numeric':")
print(correlation['FTR_numeric'])


sup15corr = correlation['FTR_numeric'][abs(correlation['FTR_numeric']) > 0.15]

print("\nColumns with correlation greater than 15% with 'FTR_numeric':")
print(sup15corr)
