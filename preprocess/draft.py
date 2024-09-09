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

        

    return team_stats



df = pd.read_csv('data/cleaned_dataset.csv')



rows = []
for i in range(len(df)):
    home_team = df.iloc[i].HomeTeam
    away_team = df.iloc[i].AwayTeam
    
    Home_stats_5 = get_stats(df.iloc[i:], [home_team], 'home', 5)
    Away_stats_5 = get_stats(df.iloc[i:], [away_team], 'away', 5)
    Home_stats_10 = get_stats(df.iloc[i:], [home_team], 'home', 10)
    Away_stats_10 = get_stats(df.iloc[i:], [away_team], 'away', 10)
    Home_stats_20 = get_stats(df.iloc[i:], [home_team], 'home', 20) 
    Away_stats_20 = get_stats(df.iloc[i:], [away_team], 'away', 20)
    
    # Create a dictionary to store the stats for the current row
    row_stats = {
        'HomeTeam': home_team,
        'AwayTeam': away_team,
        'home_average_goals_scored_5': Home_stats_5['home_average_goals_scored_5'],
        'home_average_goals_conceded_5': Home_stats_5['home_average_goals_conceded_5'],
        'home_average_goal_difference_5': Home_stats_5['home_average_goal_difference_5'],
        'home_win_rate_5': Home_stats_5['home_win_rate_5'],
        'home_draw_rate_5': Home_stats_5['home_draw_rate_5'],
        'home_loss_rate_5': Home_stats_5['home_loss_rate_5'],
        'home_shots_per_game_5': Home_stats_5['home_shots_per_game_5'],
        'home_shots_on_target_per_game_5': Home_stats_5['home_shots_on_target_per_game_5'],
        'home_shots_conceded_per_game_5': Home_stats_5['home_shots_conceded_per_game_5'],
        'home_shots_on_target_conceded_per_game_5': Home_stats_5['home_shots_on_target_conceded_per_game_5'],
        'home_corners_per_game_5': Home_stats_5['home_corners_per_game_5'],
        'home_corners_conceded_per_game_5': Home_stats_5['home_corners_conceded_per_game_5'],
        'home_fouls_per_game_5': Home_stats_5['home_fouls_per_game_5'],
        'home_fouls_conceded_per_game_5': Home_stats_5['home_fouls_conceded_per_game_5'],
        'home_yellow_cards_per_game_5': Home_stats_5['home_yellow_cards_per_game_5'],
        'home_yellow_cards_conceded_per_game_5': Home_stats_5['home_yellow_cards_conceded_per_game_5'],
        'home_red_cards_per_game_5': Home_stats_5['home_red_cards_per_game_5'],
        'home_red_cards_conceded_per_game_5': Home_stats_5['home_red_cards_conceded_per_game_5'],
        'away_average_goals_scored_5': Away_stats_5['away_average_goals_scored_5'],
        'away_average_goals_conceded_5': Away_stats_5['away_average_goals_conceded_5'],
        'away_average_goal_difference_5': Away_stats_5['away_average_goal_difference_5'],
        'away_win_rate_5': Away_stats_5['away_win_rate_5'],
        'away_draw_rate_5': Away_stats_5['away_draw_rate_5'],
        'away_loss_rate_5': Away_stats_5['away_loss_rate_5'],
        'away_shots_per_game_5': Away_stats_5['away_shots_per_game_5'],
        'away_shots_on_target_per_game_5': Away_stats_5['away_shots_on_target_per_game_5'],
        'away_shots_conceded_per_game_5': Away_stats_5['away_shots_conceded_per_game_5'],
        'away_shots_on_target_conceded_per_game_5': Away_stats_5['away_shots_on_target_conceded_per_game_5'],
        'away_corners_per_game_5': Away_stats_5['away_corners_per_game_5'],
        'away_corners_conceded_per_game_5': Away_stats_5['away_corners_conceded_per_game_5'],
        'away_fouls_per_game_5': Away_stats_5['away_fouls_per_game_5'],
        'away_fouls_conceded_per_game_5': Away_stats_5['away_fouls_conceded_per_game_5'],
        'away_yellow_cards_per_game_5': Away_stats_5['away_yellow_cards_per_game_5'],
        'away_yellow_cards_conceded_per_game_5': Away_stats_5['away_yellow_cards_conceded_per_game_5'],
        'away_red_cards_per_game_5': Away_stats_5['away_red_cards_per_game_5'],
        'away_red_cards_conceded_per_game_5': Away_stats_5['away_red_cards_conceded_per_game_5'],
        'home_average_goals_scored_10': Home_stats_10['home_average_goals_scored_10'],
        'home_average_goals_conceded_10': Home_stats_10['home_average_goals_conceded_10'],
        'home_average_goal_difference_10': Home_stats_10['home_average_goal_difference_10'],
        'home_win_rate_10': Home_stats_10['home_win_rate_10'],
        'home_draw_rate_10': Home_stats_10['home_draw_rate_10'],
        'home_loss_rate_10': Home_stats_10['home_loss_rate_10'],
        'home_shots_per_game_10': Home_stats_10['home_shots_per_game_10'],
        'home_shots_on_target_per_game_10': Home_stats_10['home_shots_on_target_per_game_10'],
        'home_shots_conceded_per_game_10': Home_stats_10['home_shots_conceded_per_game_10'],
        'home_shots_on_target_conceded_per_game_10': Home_stats_10['home_shots_on_target_conceded_per_game_10'],
        'home_corners_per_game_10': Home_stats_10['home_corners_per_game_10'],
        'home_corners_conceded_per_game_10': Home_stats_10['home_corners_conceded_per_game_10'],
        'home_fouls_per_game_10': Home_stats_10['home_fouls_per_game_10'],
        'home_fouls_conceded_per_game_10': Home_stats_10['home_fouls_conceded_per_game_10'],
        'home_yellow_cards_per_game_10': Home_stats_10['home_yellow_cards_per_game_10'],
        'home_yellow_cards_conceded_per_game_10': Home_stats_10['home_yellow_cards_conceded_per_game_10'],
        'home_red_cards_per_game_10': Home_stats_10['home_red_cards_per_game_10'],
        'home_red_cards_conceded_per_game_10': Home_stats_10['home_red_cards_conceded_per_game_10'],
        'away_average_goals_scored_10': Away_stats_10['away_average_goals_scored_10'],
        'away_average_goals_conceded_10': Away_stats_10['away_average_goals_conceded_10'],
        'away_average_goal_difference_10': Away_stats_10['away_average_goal_difference_10'],
        'away_win_rate_10': Away_stats_10['away_win_rate_10'],
        'away_draw_rate_10': Away_stats_10['away_draw_rate_10'],
        'away_loss_rate_10': Away_stats_10['away_loss_rate_10'],
        'away_shots_per_game_10': Away_stats_10['away_shots_per_game_10'],
        'away_shots_on_target_per_game_10': Away_stats_10['away_shots_on_target_per_game_10'],
        'away_shots_conceded_per_game_10': Away_stats_10['away_shots_conceded_per_game_10'],
        'away_shots_on_target_conceded_per_game_10': Away_stats_10['away_shots_on_target_conceded_per_game_10'],
        'away_corners_per_game_10': Away_stats_10['away_corners_per_game_10'],
        'away_corners_conceded_per_game_10': Away_stats_10['away_corners_conceded_per_game_10'],
        'away_fouls_per_game_10': Away_stats_10['away_fouls_per_game_10'],
        'away_fouls_conceded_per_game_10': Away_stats_10['away_fouls_conceded_per_game_10'],
        'away_yellow_cards_per_game_10': Away_stats_10['away_yellow_cards_per_game_10'],
        'away_yellow_cards_conceded_per_game_10': Away_stats_10['away_yellow_cards_conceded_per_game_10'],
        'away_red_cards_per_game_10': Away_stats_10['away_red_cards_per_game_10'],
        'away_red_cards_conceded_per_game_10': Away_stats_10['away_red_cards_conceded_per_game_10'],
        'home_average_goals_scored_20': Home_stats_20['home_average_goals_scored_20'],
        'home_average_goals_conceded_20': Home_stats_20['home_average_goals_conceded_20'],
        'home_average_goal_difference_20': Home_stats_20['home_average_goal_difference_20'],
        'home_win_rate_20': Home_stats_20['home_win_rate_20'],
        'home_draw_rate_20': Home_stats_20['home_draw_rate_20'],
        'home_loss_rate_20': Home_stats_20['home_loss_rate_20'],
        'home_shots_per_game_20': Home_stats_20['home_shots_per_game_20'],
        'home_shots_on_target_per_game_20': Home_stats_20['home_shots_on_target_per_game_20'],
        'home_shots_conceded_per_game_20': Home_stats_20['home_shots_conceded_per_game_20'],
        'home_shots_on_target_conceded_per_game_20': Home_stats_20['home_shots_on_target_conceded_per_game_20'],
        'home_corners_per_game_20': Home_stats_20['home_corners_per_game_20'],
        'home_corners_conceded_per_game_20': Home_stats_20['home_corners_conceded_per_game_20'],
        'home_fouls_per_game_20': Home_stats_20['home_fouls_per_game_20'],
        'home_fouls_conceded_per_game_20': Home_stats_20['home_fouls_conceded_per_game_20'],
        'home_yellow_cards_per_game_20': Home_stats_20['home_yellow_cards_per_game_20'],
        'home_yellow_cards_conceded_per_game_20': Home_stats_20['home_yellow_cards_conceded_per_game_20'],
        'home_red_cards_per_game_20': Home_stats_20['home_red_cards_per_game_20'],
        'home_red_cards_conceded_per_game_20': Home_stats_20['home_red_cards_conceded_per_game_20'],
        'away_average_goals_scored_20': Away_stats_20['away_average_goals_scored_20'],
        'away_average_goals_conceded_20': Away_stats_20['away_average_goals_conceded_20'],
        'away_average_goal_difference_20': Away_stats_20['away_average_goal_difference_20'],
        'away_win_rate_20': Away_stats_20['away_win_rate_20'],
        'away_draw_rate_20': Away_stats_20['away_draw_rate_20'],
        'away_loss_rate_20': Away_stats_20['away_loss_rate_20'],
        'away_shots_per_game_20': Away_stats_20['away_shots_per_game_20'],
        'away_shots_on_target_per_game_20': Away_stats_20['away_shots_on_target_per_game_20'],
        'away_shots_conceded_per_game_20': Away_stats_20['away_shots_conceded_per_game_20'],
        'away_shots_on_target_conceded_per_game_20': Away_stats_20['away_shots_on_target_conceded_per_game_20'],
        'away_corners_per_game_20': Away_stats_20['away_corners_per_game_20'],
        'away_corners_conceded_per_game_20': Away_stats_20['away_corners_conceded_per_game_20'],
        'away_fouls_per_game_20': Away_stats_20['away_fouls_per_game_20'],
        'away_fouls_conceded_per_game_20': Away_stats_20['away_fouls_conceded_per_game_20'],
        'away_yellow_cards_per_game_20': Away_stats_20['away_yellow_cards_per_game_20'],
        'away_yellow_cards_conceded_per_game_20': Away_stats_20['away_yellow_cards_conceded_per_game_20'],
        'away_red_cards_per_game_20': Away_stats_20['away_red_cards_per_game_20'],
        'away_red_cards_conceded_per_game_20': Away_stats_20['away_red_cards_conceded_per_game_20'],
    }
    rows.append(row_stats)

new_df = pd.DataFrame(rows)
print(new_df.head())
new_df.to_csv('data/final_stats.csv', index=False)




