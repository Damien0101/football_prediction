import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from tqdm import tqdm
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

df = pd.read_csv('data/combined_stats.csv')

# Split the data and target
X = df.drop(['FTR'], axis=1)
y = df['FTR']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train, X_test, y_train, y_test)
model = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=42)
model.fit(X_train, y_train)

prediction = model.predict(X_test)
mae = mean_absolute_error(y_test, prediction)
print(f'Mean Absolute Error: {mae}')
mse = mean_squared_error(y_test, prediction)
print(f'Mean Squared Error: {mse}')
r2 = r2_score(y_test, prediction)
print(f'R2 Score: {r2}')

