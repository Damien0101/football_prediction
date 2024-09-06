import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_stats(df, teams, team_status, num_games):
    stats = {}
    for team in teams:
        team_stats = {
            str(team_status)+'_average_goals_scored_'+ str(num_games): 0,
            str(team_status)+'_average_goals_conceded_'+ str(num_games): 0,
            str(team_status)+'_average_goal_difference_'+ str(num_games): 0,
            str(team_status)+'_win_rate_'+ str(num_games): 0,
            str(team_status)+'_draw_rate_'+ str(num_games): 0,
            str(team_status)+'_loss_rate_'+ str(num_games): 0,
            str(team_status)+'_shots_per_game_'+ str(num_games): 0,
            str(team_status)+'_shots_on_target_per_game_'+ str(num_games): 0,
            str(team_status)+'_shots_conceded_per_game_'+ str(num_games): 0,
            str(team_status)+'_shots_on_target_conceded_per_game_'+ str(num_games): 0,
            str(team_status)+'_corners_per_game_'+ str(num_games): 0,
            str(team_status)+'_corners_conceded_per_game_'+ str(num_games): 0,
            str(team_status)+'_fouls_per_game_'+ str(num_games): 0,
            str(team_status)+'_fouls_conceded_per_game_'+ str(num_games): 0,
            str(team_status)+'_yellow_cards_per_game_'+ str(num_games): 0,
            str(team_status)+'_yellow_cards_conceded_per_game_'+ str(num_games): 0,
            str(team_status)+'_red_cards_per_game_'+ str(num_games): 0,
            str(team_status)+'_red_cards_conceded_per_game_'+ str(num_games): 0,
        }
        

        # Fetch last num_games where team played as home or away
        team_games = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)].head(num_games)
        
   
        home_games = team_games[team_games['HomeTeam'] == team]
        away_games = team_games[team_games['AwayTeam'] == team]
        
        # Calculate average stats
        team_stats[str(team_status)+'_average_goals_scored_'+ str(num_games)] = (home_games['FTHG'].sum() + away_games['FTAG'].sum()) / num_games
        team_stats[str(team_status)+'_average_goals_conceded_'+ str(num_games)] = (home_games['FTAG'].sum() + away_games['FTHG'].sum()) / num_games
        team_stats[str(team_status)+'_average_goal_difference_'+ str(num_games)] = team_stats[str(team_status)+'_average_goals_scored_'+ str(num_games)] - team_stats[str(team_status)+'_average_goals_conceded_'+ str(num_games)]
        
        # Win, draw, loss rate (home and away)
        total_wins = len(home_games[home_games['FTR'] == 'H']) + len(away_games[away_games['FTR'] == 'A'])
        total_draws = len(home_games[home_games['FTR'] == 'D']) + len(away_games[away_games['FTR'] == 'D'])
        total_losses = len(home_games[home_games['FTR'] == 'A']) + len(away_games[away_games['FTR'] == 'H'])

        team_stats[str(team_status)+'_win_rate_'+ str(num_games)] = total_wins / num_games
        team_stats[str(team_status)+'_draw_rate_'+ str(num_games)] = total_draws / num_games
        team_stats[str(team_status)+'_loss_rate_'+ str(num_games)] = total_losses / num_games
        
        # Shots, corners, fouls, cards stats
        team_stats[str(team_status)+'_shots_per_game_'+ str(num_games)] = (home_games['HS'].sum() + away_games['AS'].sum()) / num_games
        team_stats[str(team_status)+'_shots_on_target_per_game_'+ str(num_games)] = (home_games['HST'].sum() + away_games['AST'].sum()) / num_games
        team_stats[str(team_status)+'_shots_conceded_per_game_'+ str(num_games)] = (home_games['AS'].sum() + away_games['HS'].sum()) / num_games
        team_stats[str(team_status)+'_shots_on_target_conceded_per_game_'+ str(num_games)] = (home_games['AST'].sum() + away_games['HST'].sum()) / num_games
        team_stats[str(team_status)+'_corners_per_game_'+ str(num_games)] = (home_games['HC'].sum() + away_games['AC'].sum()) / num_games
        team_stats[str(team_status)+'_corners_conceded_per_game_'+ str(num_games)] = (home_games['AC'].sum() + away_games['HC'].sum()) / num_games
        team_stats[str(team_status)+'_fouls_per_game_'+ str(num_games)] = (home_games['HF'].sum() + away_games['AF'].sum()) / num_games
        team_stats[str(team_status)+'_fouls_conceded_per_game_'+ str(num_games)] = (home_games['AF'].sum() + away_games['HF'].sum()) / num_games
        team_stats[str(team_status)+'_yellow_cards_per_game_'+ str(num_games)] = (home_games['HY'].sum() + away_games['AY'].sum()) / num_games
        team_stats[str(team_status)+'_yellow_cards_conceded_per_game_'+ str(num_games)] = (home_games['AY'].sum() + away_games['HY'].sum()) / num_games
        team_stats[str(team_status)+'_red_cards_per_game_'+ str(num_games)] = (home_games['HR'].sum() + away_games['AR'].sum()) / num_games
        team_stats[str(team_status)+'_red_cards_conceded_per_game_'+ str(num_games)] = (home_games['AR'].sum() + away_games['HR'].sum()) / num_games

        
        # Store results
        stats[team] = team_stats
    return stats



df = pd.read_csv('data/cleaned_dataset.csv')

for i in range(len(df)):
    home_team = df.iloc[i].HomeTeam
    away_team = df.iloc[i].AwayTeam
    
    Home_stats_5 = get_stats(df.iloc[i:], [home_team], 'Home', 5)
    Away_stats_5 = get_stats(df.iloc[i:], [away_team], 'Away', 5)
    Home_stats_10 = get_stats(df.iloc[i:], [home_team], 'Home', 10)
    Away_stats_10 = get_stats(df.iloc[i:], [away_team], 'Away', 10)
    Home_stats_20 = get_stats(df.iloc[i:], [home_team], 'Home', 20) 
    Away_stats_20 = get_stats(df.iloc[i:], [away_team], 'Away', 20)

    print(Home_stats_5, Away_stats_5, Home_stats_10, Away_stats_10, Home_stats_20, Away_stats_20)

