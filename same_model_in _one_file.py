import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from xgboost import XGBRegressor, XGBClassifier
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    classification_report,
    confusion_matrix
)
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Load data
df = pd.read_csv('data/dataset.csv')

# Columns to keep
columns_to_keep = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA']
df = df[columns_to_keep]

# Remove rows with any NaN values and log how many rows were dropped
rows_before = df.shape[0]
df.dropna(inplace=True)
rows_after = df.shape[0]
print(f"\nRemoved {rows_before - rows_after} rows with NaN values.")

# Check duplicates
duplicates_count = df.duplicated(keep=False).sum()
print(f"\nNumber of duplicate rows: {duplicates_count}")

# Drop duplicates if any
if duplicates_count > 0:
    df = df.drop_duplicates()

# Mapping FTR to numerical values
ftr_mapping = {'H': 0, 'D': 1, 'A': 2}
df['FTR'] = df['FTR'].map(ftr_mapping)

# Features and target variable
X = df.drop(columns=['FTR'])
y = df['FTR']

# Categorical vs numeric features
categorical_features = ['HomeTeam', 'AwayTeam']
numeric_features = ['FTHG', 'FTAG', 'B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA']

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ]
)

# Preprocess data
X_transformed = preprocessor.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Train the classifier
classifier = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
classifier.fit(X_train, y_train)

# Predictions
y_pred = classifier.predict(X_test)

# Cross-validation
cv_scores = cross_val_score(classifier, X_train, y_train, cv=5)
print(f"Mean Cross-Validation Accuracy: {cv_scores.mean():.4f}")

# Classification evaluation
print('\nClassification Evaluation:')
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Regression part
# Normally you would want to keep the test/validation split consistent across the models as mentioned earlier.
# Use the same X_test and y_test
regressor = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
regressor.fit(X_train, y_train)

# Regression predictions
y_reg_pred = regressor.predict(X_test)

# Regression evaluation
mse = mean_squared_error(y_test, y_reg_pred)
mae = mean_absolute_error(y_test, y_reg_pred)
r2 = r2_score(y_test, y_reg_pred)

print(f'\nRegression Evaluation:')
print(f'Mean Squared Error: {mse:.2f}')
print(f'Mean Absolute Error: {mae:.2f}')
print(f'R² Score: {r2:.2f}')