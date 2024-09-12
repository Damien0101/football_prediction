import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_head_to_head_stats(df, home_team, away_team):
    # Filter games between home_team and away_team
    head_to_head_games = df[((df['HomeTeam'] == home_team) & (df['AwayTeam'] == away_team)) |
                            ((df['HomeTeam'] == away_team) & (df['AwayTeam'] == home_team))]
    num_games = len(head_to_head_games)
    
    # Return default stats if no games found
    if num_games == 0:
        return {
            'head_to_head_games': 0,

            'head_to_head_goals_scored_home_team': 0,
            'head_to_head_goals_conceded_home_team': 0,

            'head_to_head_goals_scored_away_team': 0,
            'head_to_head_goals_conceded_away_team': 0}

    # Calculate statistics for home team
    home_goals_scored = head_to_head_games[head_to_head_games['HomeTeam'] == home_team]['FTHG'].sum() + \
                        head_to_head_games[head_to_head_games['AwayTeam'] == home_team]['FTAG'].sum()
    home_goals_conceded = head_to_head_games[head_to_head_games['HomeTeam'] == home_team]['FTAG'].sum() + \
                          head_to_head_games[head_to_head_games['AwayTeam'] == home_team]['FTHG'].sum()

    # Calculate statistics for away team
    away_goals_scored = head_to_head_games[head_to_head_games['HomeTeam'] == away_team]['FTHG'].sum() + \
                        head_to_head_games[head_to_head_games['AwayTeam'] == away_team]['FTAG'].sum()
    away_goals_conceded = head_to_head_games[head_to_head_games['HomeTeam'] == away_team]['FTAG'].sum() + \
                          head_to_head_games[head_to_head_games['AwayTeam'] == away_team]['FTHG'].sum()

    return {
        'head_to_head_games': num_games,
        'head_to_head_goals_scored_home_team': home_goals_scored,
        'head_to_head_goals_conceded_home_team': home_goals_conceded,
        'head_to_head_goals_scored_away_team': away_goals_scored,
        'head_to_head_goals_conceded_away_team': away_goals_conceded}


def get_stats(df, teams, team_status, num_games):
    for team in teams:
        team_stats = {
            str(team_status)+'_average_goals_scored_'+ str(num_games): 0,
            str(team_status)+'_average_goals_conceded_'+ str(num_games): 0,
            str(team_status)+'_average_goal_difference_'+ str(num_games): 0}
 
        # Fetch last num_games where team played as home or away
        team_games = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)].head(num_games)
        num_games = len(team_games)
        home_games = team_games[team_games['HomeTeam'] == team]
        away_games = team_games[team_games['AwayTeam'] == team]
        if num_games == 0:
            num_games = 1
        # Calculate average stats
        team_stats[str(team_status)+'_average_goals_scored_'+ str(num_games)] = (home_games['FTHG'].sum() + away_games['FTAG'].sum()) / num_games
        team_stats[str(team_status)+'_average_goals_conceded_'+ str(num_games)] = (home_games['FTAG'].sum() + away_games['FTHG'].sum()) / num_games
        team_stats[str(team_status)+'_average_goal_difference_'+ str(num_games)] = team_stats[str(team_status)+'_average_goals_scored_'+ str(num_games)] - team_stats[str(team_status)+'_average_goals_conceded_'+ str(num_games)]

    return team_stats



df = pd.read_csv('data/cleaned_dataset.csv')



rows = []
for i in range(len(df)):
    home_team = df.iloc[i].HomeTeam
    away_team = df.iloc[i].AwayTeam
    FTR = df.iloc[i].FTR

    
    Home_stats_5 = get_stats(df.iloc[i+1:], [home_team], 'home', 5)
    Away_stats_5= get_stats(df.iloc[i+1:], [away_team], 'away', 5)
    Home_stats_10 = get_stats(df.iloc[i+1:], [home_team], 'home', 10) 
    Away_stats_10 = get_stats(df.iloc[i+1:], [away_team], 'away', 10)
    Home_stats_20= get_stats(df.iloc[i+1:], [home_team], 'home', 20)
    Away_stats_20 = get_stats(df.iloc[i+1:], [away_team], 'away', 20)

    head_to_head_stats = get_head_to_head_stats(df.iloc[i+1:], home_team, away_team)

    
    # Create a dictionary to store the stats for the current row
    row_stats = {
        'HomeTeam': home_team,
        'AwayTeam': away_team,
        'FTR': FTR,
        'head_to_head_games': head_to_head_stats['head_to_head_games'],

        'head_to_head_goals_scored_home_team': head_to_head_stats['head_to_head_goals_scored_home_team'],
        'head_to_head_goals_conceded_home_team': head_to_head_stats['head_to_head_goals_conceded_home_team'],

        'head_to_head_goals_scored_away_team': head_to_head_stats['head_to_head_goals_scored_away_team'],
        'head_to_head_goals_conceded_away_team': head_to_head_stats['head_to_head_goals_conceded_away_team'],

        'home_average_goals_scored_5': Home_stats_5['home_average_goals_scored_5'],
        'home_average_goals_conceded_5': Home_stats_5['home_average_goals_conceded_5'],
        'home_average_goal_difference_5': Home_stats_5['home_average_goal_difference_5'],

        'away_average_goals_scored_5': Away_stats_5['away_average_goals_scored_5'],
        'away_average_goals_conceded_5': Away_stats_5['away_average_goals_conceded_5'],
        'away_average_goal_difference_5': Away_stats_5['away_average_goal_difference_5'],

        'home_average_goals_scored_10': Home_stats_10['home_average_goals_scored_10'],
        'home_average_goals_conceded_10': Home_stats_10['home_average_goals_conceded_10'],
        'home_average_goal_difference_10': Home_stats_10['home_average_goal_difference_10'],

        'away_average_goals_scored_10': Away_stats_10['away_average_goals_scored_10'],
        'away_average_goals_conceded_10': Away_stats_10['away_average_goals_conceded_10'],
        'away_average_goal_difference_10': Away_stats_10['away_average_goal_difference_10'],

        'home_average_goals_scored_20': Home_stats_20['home_average_goals_scored_20'],
        'home_average_goals_conceded_20': Home_stats_20['home_average_goals_conceded_20'],
        'home_average_goal_difference_20': Home_stats_20['home_average_goal_difference_20'],

        'away_average_goals_scored_20': Away_stats_20['away_average_goals_scored_20'],
        'away_average_goals_conceded_20': Away_stats_20['away_average_goals_conceded_20'],
        'away_average_goal_difference_20': Away_stats_20['away_average_goal_difference_20'],
 }
    rows.append(row_stats)


new_df = pd.DataFrame(rows)
print(new_df.head())
new_df.to_csv('data/final_stats.csv', index=False)
