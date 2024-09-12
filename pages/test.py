import pandas as pd

# Data for future matches
data = {
    'HomeTeam': [
        'Club Brugge', 'Genk', 'Antwerp', 'KV Mechelen', 'Kortrijk', 'Union Saint-Gilloise', 
        'OH Leuven', 'Eupen', 'Anderlecht', 'Gent', 'Standard Liège', 'Cercle Brugge', 
        'Sint-Truiden', 'Charleroi', 'Zulte Waregem', 'Westerlo'
    ],
    'AwayTeam': [
        'Anderlecht', 'Gent', 'Standard Liège', 'Cercle Brugge', 'Sint-Truiden', 'Charleroi', 
        'Zulte Waregem', 'Westerlo', 'Genk', 'Club Brugge', 'Antwerp', 'KV Mechelen', 
        'Kortrijk', 'Union Saint-Gilloise', 'OH Leuven', 'Eupen'
    ],
    'Day': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data/future_matches.csv', index=False)

print(df.head())
