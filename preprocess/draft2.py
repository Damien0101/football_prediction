import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import seaborn as sns

df = pd.read_csv('data/cleaned_dataset.csv')



def get_teams_count(df, num_games):
    count = {}
    for _, row in df.iterrows():
        home_team = row['HomeTeam']
        away_team = row['AwayTeam']
        if home_team in count:
            if count[home_team] < num_games:
                count[home_team] += 1
        else:
            count[home_team] = 1

        if away_team in count:
            if count[away_team] < num_games:
                count[away_team] += 1
        else:
            count[away_team] = 1

    return count

teams_count = get_teams_count(df, 20)
print(teams_count)

# Create a function to get the average stats of home team for n_games

"""def get_avg_stats(df, teams, n_games):
    # Get the average stats of the home team for the last n_games   
    for team in teams:
        home_team_stats =  {
            'average_goals_scored': 0,
            'average_goals_conceded': 0,
            'average_goal_difference': 0,
            'win_rate': 0,
            'draw_rate': 0,
            'loss_rate': 0,
            'shots_per_game': 0,
            'shots_on_target_per_game': 0,
            'shots_conceded_per_game': 0,
            'shots_on_target_conceded_per_game': 0,
            'corners_per_game': 0,
            'corners_conceded_per_game': 0,
            'fouls_per_game': 0,
            'fouls_conceded_per_game': 0,
            'yellow_cards_per_game': 0,
            'yellow_cards_conceded_per_game': 0,
            'red_cards_per_game': 0,
            'red_cards_conceded_per_game': 0,
            'head_to_head_win_last_draw': 0,
            'average_rank': 0
        }
    
    # Fetch last num_games where team played as home or away
    team_games = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)].head(num_games)"""


