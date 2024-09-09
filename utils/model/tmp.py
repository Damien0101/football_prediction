import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multioutput import MultiOutputClassifier
from tqdm import tqdm
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

df = pd.read_csv('data/final_stats.csv')

# Use OneHotEncoder to create boolean columns of categorical columns
ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False).set_output(transform="pandas")
ohetransform = ohe.fit_transform(df[['HomeTeam', 'AwayTeam']])
df = pd.concat([df,ohetransform],axis=1).drop(columns=['HomeTeam', 'AwayTeam'])

targets_to_predict=['FTR_D','FTR_A','FTR_H']
#Create a list of models to try
models = {
    'GradientBoostingClassifier': GradientBoostingClassifier(),
    'RandomForestClassifier': RandomForestClassifier(),
    'LogisticRegression': LogisticRegression(max_iter=1000),
    'DecisionTreeClassifier': DecisionTreeClassifier(),
    'KNeighborsClassifier': KNeighborsClassifier()
}
# Split the data and target
X = df.drop(targets_to_predict, axis=1)
y = df[targets_to_predict]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
for model_name, model in tqdm(models.items()):
    multioutputmodel = MultiOutputClassifier(model, n_jobs=-1)
    multioutputmodel.fit(X_train, y_train)
    predictions = multioutputmodel.predict(X_test)
    accuracy = multioutputmodel.score(X_test, y_test)
    print(f'{model_name} accuracy: {accuracy}')