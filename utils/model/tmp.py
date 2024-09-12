import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
import pickle


# Load the data
df = pd.read_csv('data/final_stats.csv')
matches = df[['HomeTeam', 'AwayTeam']]

# Perform one-hot encoding on categorical features
ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False).set_output(transform="pandas")
ohetransform = ohe.fit_transform(df[['HomeTeam', 'AwayTeam']])
df = pd.concat([df, ohetransform], axis=1).drop(columns=['HomeTeam', 'AwayTeam'])

with open('utils/model/onehot_encoder.pkl', 'wb') as file:
    pickle.dump(ohe, file)

# Define features and target
X = df.drop(['FTR'], axis=1)
y = df['FTR']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)




model = LogisticRegression()

model.fit(X_train, y_train)

with open('utils/model/logistic_regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)
    
y_pred = model.predict(X_test)
y_pred_df = pd.DataFrame(y_pred, columns=['FTR'])
accuracy = accuracy_score(y_test, y_pred)


probabilities = model.predict_proba(X_test)
probabilities_df = pd.DataFrame(probabilities, columns=model.classes_)



results = pd.concat([probabilities_df, y_pred_df], axis=1)
merged_results = pd.merge(matches, results, left_index=True, right_index=True)
print(merged_results.head(25))
