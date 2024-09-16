import pandas as pd
import numpy as np


df = pd.read_csv('data/stats_preaverage.csv')

def get_average_stats(df, num_games):
    teams = df['HomeTeam'].unique()  
    all_team_stats = []  

    for team in teams:
        team_stats = {'team': team}   
        team_games = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)].head(num_games)
        actual_num_games = max(1, len(team_games))  

        home_games = team_games[team_games['HomeTeam'] == team]
        away_games = team_games[team_games['AwayTeam'] == team]

        team_stats[f'{num_games}_AGS'] = (
            (home_games['FTHG'].sum() + away_games['FTAG'].sum()) / actual_num_games
        )
        team_stats[f'{num_games}_AGC'] = (
            (home_games['FTAG'].sum() + away_games['FTHG'].sum()) / actual_num_games
        )
        team_stats[f'{num_games}_AGD'] = (
            team_stats[f'{num_games}_AGS'] - team_stats[f'{num_games}_AGC']
        )
        team_stats[f'{num_games}_AS'] = (
            (home_games['HS'].sum() + away_games['AS'].sum()) / actual_num_games
        )
        team_stats[f'{num_games}_AST'] = (
            (home_games['HST'].sum() + away_games['AST'].sum()) / actual_num_games
        )
        team_stats[f'{num_games}_AF'] = (
            (home_games['HF'].sum() + away_games['AF'].sum()) / actual_num_games
        )
        team_stats[f'{num_games}_AC'] = (
            (home_games['HC'].sum() + away_games['AC'].sum()) / actual_num_games
        )
        team_stats[f'{num_games}_AY'] = (
            (home_games['HY'].sum() + away_games['AY'].sum()) / actual_num_games
        )
        team_stats[f'{num_games}_AR'] = (
            (home_games['HR'].sum() + away_games['AR'].sum()) / actual_num_games
        )

        
        home_games = df[df['HomeTeam'] == team].head(num_games)
        actual_num_home_games = max(1, len(home_games))  

        team_stats[f'home_average_goals_scored_{num_games}'] = (
            home_games['FTHG'].sum() / actual_num_home_games
        )
        team_stats[f'home_average_goals_conceded_{num_games}'] = (
            home_games['FTAG'].sum() / actual_num_home_games
        )
        team_stats[f'home_average_goal_difference_{num_games}'] = (
            team_stats[f'home_average_goals_scored_{num_games}'] - team_stats[f'home_average_goals_conceded_{num_games}']
        )
        team_stats[f'home_average_shots_{num_games}'] = (
            home_games['HS'].sum() / actual_num_home_games
        )
        team_stats[f'home_average_shots_on_target_{num_games}'] = (
            home_games['HST'].sum() / actual_num_home_games
        )
        team_stats[f'home_average_fouls_{num_games}'] = (
            home_games['HF'].sum() / actual_num_home_games
        )
        team_stats[f'home_average_corners_{num_games}'] = (
            home_games['HC'].sum() / actual_num_home_games
        )
        team_stats[f'home_average_yellow_cards_{num_games}'] = (
            home_games['HY'].sum() / actual_num_home_games
        )
        team_stats[f'home_average_red_cards_{num_games}'] = (
            home_games['HR'].sum() / actual_num_home_games
        )

        
        away_games = df[df['AwayTeam'] == team].head(num_games)
        actual_num_away_games = max(1, len(away_games))  # Prevent division by zero

        team_stats[f'away_average_goals_scored_{num_games}'] = (
            away_games['FTAG'].sum() / actual_num_away_games
        )
        team_stats[f'away_average_goals_conceded_{num_games}'] = (
            away_games['FTHG'].sum() / actual_num_away_games
        )
        team_stats[f'away_average_goal_difference_{num_games}'] = (
            team_stats[f'away_average_goals_scored_{num_games}'] - team_stats[f'away_average_goals_conceded_{num_games}']
        )
        team_stats[f'away_average_shots_{num_games}'] = (
            away_games['AS'].sum() / actual_num_away_games
        )
        team_stats[f'away_average_shots_on_target_{num_games}'] = (
            away_games['AST'].sum() / actual_num_away_games
        )
        team_stats[f'away_average_fouls_{num_games}'] = (
            away_games['AF'].sum() / actual_num_away_games
        )
        team_stats[f'away_average_corners_{num_games}'] = (
            away_games['AC'].sum() / actual_num_away_games
        )
        team_stats[f'away_average_yellow_cards_{num_games}'] = (
            away_games['AY'].sum() / actual_num_away_games
        )
        team_stats[f'away_average_red_cards_{num_games}'] = (
            away_games['AR'].sum() / actual_num_away_games
        )

        all_team_stats.append(team_stats)

    all_team_stats_df = pd.DataFrame(all_team_stats)
    averages = f'data/team_averages_last_{num_games}_games.csv'
    all_team_stats_df.to_csv(averages, index=False)

    return all_team_stats_df


get_average_stats(df, 5)
get_average_stats(df, 10)
get_average_stats(df, 20)
