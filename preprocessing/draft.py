import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import seaborn as sns


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


def get_stats(df, teams, num_games):
    stats = {}
    for team in teams:
        team_stats = {
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
        team_games = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)].head(num_games)
        
        # Home games stats
        home_games = team_games[team_games['HomeTeam'] == team]
        away_games = team_games[team_games['AwayTeam'] == team]
        
        # Calculate average stats
        team_stats['average_goals_scored'] = (home_games['FTHG'].sum() + away_games['FTAG'].sum()) / num_games
        team_stats['average_goals_conceded'] = (home_games['FTAG'].sum() + away_games['FTHG'].sum()) / num_games
        team_stats['average_goal_difference'] = team_stats['average_goals_scored'] - team_stats['average_goals_conceded']
        
        # Win, draw, loss rate (home and away)
        total_wins = home_games[home_games['FTR'] == 'H'].shape[0] + away_games[away_games['FTR'] == 'A'].shape[0]
        total_draws = team_games[team_games['FTR'] == 'D'].shape[0]
        total_losses = num_games - total_wins - total_draws
        
        team_stats['win_rate'] = total_wins / num_games
        team_stats['draw_rate'] = total_draws / num_games
        team_stats['loss_rate'] = total_losses / num_games
        
        # Shots, corners, fouls, cards stats
        team_stats['shots_per_game'] = (home_games['HS'].sum() + away_games['AS'].sum()) / num_games
        team_stats['shots_on_target_per_game'] = (home_games['HST'].sum() + away_games['AST'].sum()) / num_games
        team_stats['shots_conceded_per_game'] = (home_games['AS'].sum() + away_games['HS'].sum()) / num_games
        team_stats['shots_on_target_conceded_per_game'] = (home_games['AST'].sum() + away_games['HST'].sum()) / num_games
        team_stats['corners_per_game'] = (home_games['HC'].sum() + away_games['AC'].sum()) / num_games
        team_stats['corners_conceded_per_game'] = (home_games['AC'].sum() + away_games['HC'].sum()) / num_games
        team_stats['fouls_per_game'] = (home_games['HF'].sum() + away_games['AF'].sum()) / num_games
        team_stats['fouls_conceded_per_game'] = (home_games['AF'].sum() + away_games['HF'].sum()) / num_games
        team_stats['yellow_cards_per_game'] = (home_games['HY'].sum() + away_games['AY'].sum()) / num_games
        team_stats['yellow_cards_conceded_per_game'] = (home_games['AY'].sum() + away_games['HY'].sum()) / num_games
        team_stats['red_cards_per_game'] = (home_games['HR'].sum() + away_games['AR'].sum()) / num_games
        team_stats['red_cards_conceded_per_game'] = (home_games['AR'].sum() + away_games['HR'].sum()) / num_games
        
        # Store results
        stats[team] = team_stats
    return stats




df = pd.read_csv('data/cleaned_dataset.csv')
teams = get_teams_count(df, 20)
order = pd.Series(teams).sort_values(ascending=False)
print(order)

stats_last_5 = get_stats(df, order.index, 5)
average_goals_scored_last5 = {team: stats_last_5[team]['average_goals_scored'] for team in stats_last_5}
average_goals_conceded_last5 = {team: stats_last_5[team]['average_goals_conceded'] for team in stats_last_5}
average_goal_difference_last5 = {team: stats_last_5[team]['average_goal_difference'] for team in stats_last_5}
win_rate_last5 = {team: stats_last_5[team]['win_rate'] for team in stats_last_5}
draw_rate_last5 = {team: stats_last_5[team]['draw_rate'] for team in stats_last_5}
loss_rate_last5 = {team: stats_last_5[team]['loss_rate'] for team in stats_last_5}
shots_per_game_last5 = {team: stats_last_5[team]['shots_per_game'] for team in stats_last_5}
shots_on_target_per_game_last5 = {team: stats_last_5[team]['shots_on_target_per_game'] for team in stats_last_5}
shots_conceded_per_game_last5 = {team: stats_last_5[team]['shots_conceded_per_game'] for team in stats_last_5}
shots_on_target_conceded_per_game_last5 = {team: stats_last_5[team]['shots_on_target_conceded_per_game'] for team in stats_last_5}
corners_per_game_last5 = {team: stats_last_5[team]['corners_per_game'] for team in stats_last_5}
corners_conceded_per_game_last5 = {team: stats_last_5[team]['corners_conceded_per_game'] for team in stats_last_5}
fouls_per_game_last5 = {team: stats_last_5[team]['fouls_per_game'] for team in stats_last_5}
fouls_conceded_per_game_last5 = {team: stats_last_5[team]['fouls_conceded_per_game'] for team in stats_last_5}
yellow_cards_per_game_last5 = {team: stats_last_5[team]['yellow_cards_per_game'] for team in stats_last_5}
yellow_cards_conceded_per_game_last5 = {team: stats_last_5[team]['yellow_cards_conceded_per_game'] for team in stats_last_5}
red_cards_per_game_last5 = {team: stats_last_5[team]['red_cards_per_game'] for team in stats_last_5}
red_cards_conceded_per_game_last5 = {team: stats_last_5[team]['red_cards_conceded_per_game'] for team in stats_last_5}
df_goals_scored_last5 = pd.DataFrame.from_dict(average_goals_scored_last5, orient='index', columns=['average_goals_scored_last5'])
df_goals_conceded_last5 = pd.DataFrame.from_dict(average_goals_conceded_last5, orient='index', columns=['average_goals_conceded_last5'])
df_goal_diff_last5 = pd.DataFrame.from_dict(average_goal_difference_last5, orient='index', columns=['average_goal_difference_last5'])
df_win_rate_last5 = pd.DataFrame.from_dict(win_rate_last5, orient='index', columns=['win_rate_last5'])
df_draw_rate_last5 = pd.DataFrame.from_dict(draw_rate_last5, orient='index', columns=['draw_rate_last5'])
df_loss_rate_last5 = pd.DataFrame.from_dict(loss_rate_last5, orient='index', columns=['loss_rate_last5'])
df_shots_per_game_last5 = pd.DataFrame.from_dict(shots_per_game_last5, orient='index', columns=['shots_per_game_last5'])
df_shots_on_target_per_game_last5 = pd.DataFrame.from_dict(shots_on_target_per_game_last5, orient='index', columns=['shots_on_target_per_game_last5'])
df_shots_conceded_per_game_last5 = pd.DataFrame.from_dict(shots_conceded_per_game_last5, orient='index', columns=['shots_conceded_per_game_last5'])
df_shots_on_target_conceded_per_game_last5 = pd.DataFrame.from_dict(shots_on_target_conceded_per_game_last5, orient='index', columns=['shots_on_target_conceded_per_game_last5'])
df_corners_per_game_last5 = pd.DataFrame.from_dict(corners_per_game_last5, orient='index', columns=['corners_per_game_last5'])
df_corners_conceded_per_game_last5 = pd.DataFrame.from_dict(corners_conceded_per_game_last5, orient='index', columns=['corners_conceded_per_game_last5'])
df_fouls_per_game_last5 = pd.DataFrame.from_dict(fouls_per_game_last5, orient='index', columns=['fouls_per_game_last5'])
df_fouls_conceded_per_game_last5 = pd.DataFrame.from_dict(fouls_conceded_per_game_last5, orient='index', columns=['fouls_conceded_per_game_last5'])
df_yellow_cards_per_game_last5 = pd.DataFrame.from_dict(yellow_cards_per_game_last5, orient='index', columns=['yellow_cards_per_game_last5'])
df_yellow_cards_conceded_per_game_last5 = pd.DataFrame.from_dict(yellow_cards_conceded_per_game_last5, orient='index', columns=['yellow_cards_conceded_per_game_last5'])
df_red_cards_per_game_last5 = pd.DataFrame.from_dict(red_cards_per_game_last5, orient='index', columns=['red_cards_per_game_last5'])
df_red_cards_conceded_per_game_last5 = pd.DataFrame.from_dict(red_cards_conceded_per_game_last5, orient='index', columns=['red_cards_conceded_per_game_last5'])



stats_last_10 = get_stats(df, order.index, 10)
average_goals_scored_last10 = {team: stats_last_10[team]['average_goals_scored'] for team in stats_last_10}
average_goals_conceded_last10 = {team: stats_last_10[team]['average_goals_conceded'] for team in stats_last_10}
average_goal_difference_last10 = {team: stats_last_10[team]['average_goal_difference'] for team in stats_last_10}
win_rate_last10 = {team: stats_last_10[team]['win_rate'] for team in stats_last_10}
draw_rate_last10 = {team: stats_last_10[team]['draw_rate'] for team in stats_last_10}
loss_rate_last10 = {team: stats_last_10[team]['loss_rate'] for team in stats_last_10}
shots_per_game_last10 = {team: stats_last_10[team]['shots_per_game'] for team in stats_last_10}
shots_on_target_per_game_last10 = {team: stats_last_10[team]['shots_on_target_per_game'] for team in stats_last_10}
shots_conceded_per_game_last10 = {team: stats_last_10[team]['shots_conceded_per_game'] for team in stats_last_10}
shots_on_target_conceded_per_game_last10 = {team: stats_last_10[team]['shots_on_target_conceded_per_game'] for team in stats_last_10}
corners_per_game_last10 = {team: stats_last_10[team]['corners_per_game'] for team in stats_last_10}
corners_conceded_per_game_last10 = {team: stats_last_10[team]['corners_conceded_per_game'] for team in stats_last_10}
fouls_per_game_last10 = {team: stats_last_10[team]['fouls_per_game'] for team in stats_last_10}
fouls_conceded_per_game_last10 = {team: stats_last_10[team]['fouls_conceded_per_game'] for team in stats_last_10}
yellow_cards_per_game_last10 = {team: stats_last_10[team]['yellow_cards_per_game'] for team in stats_last_10}
yellow_cards_conceded_per_game_last10 = {team: stats_last_10[team]['yellow_cards_conceded_per_game'] for team in stats_last_10}
red_cards_per_game_last10 = {team: stats_last_10[team]['red_cards_per_game'] for team in stats_last_10}
red_cards_conceded_per_game_last10 = {team: stats_last_10[team]['red_cards_conceded_per_game'] for team in stats_last_10}
df_goals_scored_last10= pd.DataFrame.from_dict(average_goals_scored_last10, orient='index', columns=['average_goals_scored_last10'])
df_goals_conceded_last10 = pd.DataFrame.from_dict(average_goals_conceded_last10, orient='index', columns=['average_goals_conceded_last10'])
df_goal_diff_last10 = pd.DataFrame.from_dict(average_goal_difference_last10, orient='index', columns=['average_goal_difference_last10'])
df_win_rate_last10 = pd.DataFrame.from_dict(win_rate_last10, orient='index', columns=['win_rate_last10'])
df_draw_rate_last10 = pd.DataFrame.from_dict(draw_rate_last10, orient='index', columns=['draw_rate_last10'])
df_loss_rate_last10 = pd.DataFrame.from_dict(loss_rate_last10, orient='index', columns=['loss_rate_last10'])
df_shots_per_game_last10 = pd.DataFrame.from_dict(shots_per_game_last10, orient='index', columns=['shots_per_game_last10'])
df_shots_on_target_per_game_last10 = pd.DataFrame.from_dict(shots_on_target_per_game_last10, orient='index', columns=['shots_on_target_per_game_last10'])
df_shots_conceded_per_game_last10 = pd.DataFrame.from_dict(shots_conceded_per_game_last10, orient='index', columns=['shots_conceded_per_game_last10'])
df_shots_on_target_conceded_per_game_last10 = pd.DataFrame.from_dict(shots_on_target_conceded_per_game_last10, orient='index', columns=['shots_on_target_conceded_per_game_last10'])
df_corners_per_game_last10 = pd.DataFrame.from_dict(corners_per_game_last10, orient='index', columns=['corners_per_game_last10'])
df_corners_conceded_per_game_last10 = pd.DataFrame.from_dict(corners_conceded_per_game_last10, orient='index', columns=['corners_conceded_per_game_last10'])
df_fouls_per_game_last10 = pd.DataFrame.from_dict(fouls_per_game_last10, orient='index', columns=['fouls_per_game_last10'])
df_fouls_conceded_per_game_last10 = pd.DataFrame.from_dict(fouls_conceded_per_game_last10, orient='index', columns=['fouls_conceded_per_game_last10'])
df_yellow_cards_per_game_last10 = pd.DataFrame.from_dict(yellow_cards_per_game_last10, orient='index', columns=['yellow_cards_per_game_last10'])
df_yellow_cards_conceded_per_game_last10 = pd.DataFrame.from_dict(yellow_cards_conceded_per_game_last10, orient='index', columns=['yellow_cards_conceded_per_game_last10'])
df_red_cards_per_game_last10 = pd.DataFrame.from_dict(red_cards_per_game_last10, orient='index', columns=['red_cards_per_game_last10'])
df_red_cards_conceded_per_game_last10 = pd.DataFrame.from_dict(red_cards_conceded_per_game_last10, orient='index', columns=['red_cards_conceded_per_game_last10'])



stats_last_20 = get_stats(df, order.index, 20)
average_goals_scored_last20 = {team: stats_last_20[team]['average_goals_scored'] for team in stats_last_20}
average_goals_conceded_last20 = {team: stats_last_20[team]['average_goals_conceded'] for team in stats_last_20}
average_goal_difference_last20 = {team: stats_last_20[team]['average_goal_difference'] for team in stats_last_20}
win_rate_last20 = {team: stats_last_20[team]['win_rate'] for team in stats_last_20}
draw_rate_last20 = {team: stats_last_20[team]['draw_rate'] for team in stats_last_20}
loss_rate_last20 = {team: stats_last_20[team]['loss_rate'] for team in stats_last_20}
shots_per_game_last20 = {team: stats_last_20[team]['shots_per_game'] for team in stats_last_20}
shots_on_target_per_game_last20 = {team: stats_last_20[team]['shots_on_target_per_game'] for team in stats_last_20}
shots_conceded_per_game_last20 = {team: stats_last_20[team]['shots_conceded_per_game'] for team in stats_last_20}
shots_on_target_conceded_per_game_last20 = {team: stats_last_20[team]['shots_on_target_conceded_per_game'] for team in stats_last_20}
corners_per_game_last20 = {team: stats_last_20[team]['corners_per_game'] for team in stats_last_20}
corners_conceded_per_game_last20 = {team: stats_last_20[team]['corners_conceded_per_game'] for team in stats_last_20}
fouls_per_game_last20 = {team: stats_last_20[team]['fouls_per_game'] for team in stats_last_20}
fouls_conceded_per_game_last20 = {team: stats_last_20[team]['fouls_conceded_per_game'] for team in stats_last_20}
yellow_cards_per_game_last20 = {team: stats_last_20[team]['yellow_cards_per_game'] for team in stats_last_20}
yellow_cards_conceded_per_game_last20 = {team: stats_last_20[team]['yellow_cards_conceded_per_game'] for team in stats_last_20}
red_cards_per_game_last20 = {team: stats_last_20[team]['red_cards_per_game'] for team in stats_last_20}
red_cards_conceded_per_game_last20 = {team: stats_last_20[team]['red_cards_conceded_per_game'] for team in stats_last_20}
df_goals_scored_last20 = pd.DataFrame.from_dict(average_goals_scored_last20, orient='index', columns=['average_goals_scored_last20'])
df_goals_conceded_last20 = pd.DataFrame.from_dict(average_goals_conceded_last20, orient='index', columns=['average_goals_conceded_last20'])
df_goal_diff_last20 = pd.DataFrame.from_dict(average_goal_difference_last20, orient='index', columns=['average_goal_difference_last20'])
df_win_rate_last20 = pd.DataFrame.from_dict(win_rate_last20, orient='index', columns=['win_rate_last20'])
df_draw_rate_last20 = pd.DataFrame.from_dict(draw_rate_last20, orient='index', columns=['draw_rate_last20'])
df_loss_rate_last20 = pd.DataFrame.from_dict(loss_rate_last20, orient='index', columns=['loss_rate_last20'])
df_shots_per_game_last20 = pd.DataFrame.from_dict(shots_per_game_last20, orient='index', columns=['shots_per_game_last20'])
df_shots_on_target_per_game_last20 = pd.DataFrame.from_dict(shots_on_target_per_game_last20, orient='index', columns=['shots_on_target_per_game_last20'])
df_shots_conceded_per_game_last20 = pd.DataFrame.from_dict(shots_conceded_per_game_last20, orient='index', columns=['shots_conceded_per_game_last20'])
df_shots_on_target_conceded_per_game_last20 = pd.DataFrame.from_dict(shots_on_target_conceded_per_game_last20, orient='index', columns=['shots_on_target_conceded_per_game_last20'])
df_corners_per_game_last20 = pd.DataFrame.from_dict(corners_per_game_last20, orient='index', columns=['corners_per_game_last20'])
df_corners_conceded_per_game_last20 = pd.DataFrame.from_dict(corners_conceded_per_game_last20, orient='index', columns=['corners_conceded_per_game_last20'])
df_fouls_per_game_last20 = pd.DataFrame.from_dict(fouls_per_game_last20, orient='index', columns=['fouls_per_game_last20'])
df_fouls_conceded_per_game_last20 = pd.DataFrame.from_dict(fouls_conceded_per_game_last20, orient='index', columns=['fouls_conceded_per_game_last20'])
df_yellow_cards_per_game_last20 = pd.DataFrame.from_dict(yellow_cards_per_game_last20, orient='index', columns=['yellow_cards_per_game_last20'])
df_yellow_cards_conceded_per_game_last20 = pd.DataFrame.from_dict(yellow_cards_conceded_per_game_last20, orient='index', columns=['yellow_cards_conceded_per_game_last20'])
df_red_cards_per_game_last20 = pd.DataFrame.from_dict(red_cards_per_game_last20, orient='index', columns=['red_cards_per_game_last20'])
df_red_cards_conceded_per_game_last20 = pd.DataFrame.from_dict(red_cards_conceded_per_game_last20, orient='index', columns=['red_cards_conceded_per_game_last20'])

new_stats_df = pd.concat([df_goals_scored_last5, df_goals_conceded_last5, df_goal_diff_last5, df_win_rate_last5, df_draw_rate_last5, df_loss_rate_last5, df_shots_per_game_last5,
                          df_shots_on_target_per_game_last5, df_shots_conceded_per_game_last5, df_shots_on_target_conceded_per_game_last5, df_corners_per_game_last5, 
                          df_corners_conceded_per_game_last5, df_fouls_per_game_last5, df_fouls_conceded_per_game_last5, df_yellow_cards_per_game_last5, 
                          df_yellow_cards_conceded_per_game_last5, df_red_cards_per_game_last5, df_red_cards_conceded_per_game_last5, df_goals_scored_last10, 
                          df_goals_conceded_last10, df_goal_diff_last10, df_win_rate_last10, df_draw_rate_last10, df_loss_rate_last10, df_shots_per_game_last10, 
                          df_shots_on_target_per_game_last10, df_shots_conceded_per_game_last10, df_shots_on_target_conceded_per_game_last10, df_corners_per_game_last10,
                          df_corners_conceded_per_game_last10, df_fouls_per_game_last10, df_fouls_conceded_per_game_last10, df_yellow_cards_per_game_last10, 
                          df_yellow_cards_conceded_per_game_last10, df_red_cards_per_game_last10, df_red_cards_conceded_per_game_last10, df_goals_scored_last20, 
                          df_goals_conceded_last20, df_goal_diff_last20, df_win_rate_last20, df_draw_rate_last20, df_loss_rate_last20, df_shots_per_game_last20, 
                          df_shots_on_target_per_game_last20, df_shots_conceded_per_game_last20, df_shots_on_target_conceded_per_game_last20, df_corners_per_game_last20, 
                          df_corners_conceded_per_game_last20, df_fouls_per_game_last20, df_fouls_conceded_per_game_last20, df_yellow_cards_per_game_last20, 
                          df_yellow_cards_conceded_per_game_last20, df_red_cards_per_game_last20, df_red_cards_conceded_per_game_last20], axis=1)




# Merge last 5 games stats
df = df.merge(df_goals_scored_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_goals_scored_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_goals_conceded_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_goals_conceded_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_goal_diff_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_goal_diff_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_win_rate_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_win_rate_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_draw_rate_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_draw_rate_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_loss_rate_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_loss_rate_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_shots_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_shots_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_shots_on_target_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_shots_on_target_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_shots_conceded_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_shots_conceded_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_shots_on_target_conceded_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_shots_on_target_conceded_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_corners_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_corners_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_corners_conceded_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_corners_conceded_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_fouls_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_fouls_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_fouls_conceded_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_fouls_conceded_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_yellow_cards_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_yellow_cards_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_yellow_cards_conceded_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_yellow_cards_conceded_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_red_cards_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_red_cards_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

df = df.merge(df_red_cards_conceded_per_game_last5, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last5'))
df = df.merge(df_red_cards_conceded_per_game_last5, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last5'))

# Merge last 10 games stats
df = df.merge(df_goals_scored_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_goals_scored_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_goals_conceded_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_goals_conceded_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_goal_diff_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_goal_diff_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_win_rate_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_win_rate_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_draw_rate_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_draw_rate_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_loss_rate_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_loss_rate_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_shots_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_shots_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_shots_on_target_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_shots_on_target_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_shots_conceded_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_shots_conceded_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_shots_on_target_conceded_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_shots_on_target_conceded_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_corners_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_corners_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_corners_conceded_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_corners_conceded_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_fouls_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_fouls_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_fouls_conceded_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_fouls_conceded_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_yellow_cards_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_yellow_cards_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_yellow_cards_conceded_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_yellow_cards_conceded_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_red_cards_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_red_cards_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

df = df.merge(df_red_cards_conceded_per_game_last10, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last10'))
df = df.merge(df_red_cards_conceded_per_game_last10, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last10'))

# Merge last 20 games stats
df = df.merge(df_goals_scored_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_goals_scored_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_goals_conceded_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_goals_conceded_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_goal_diff_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_goal_diff_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_win_rate_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_win_rate_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_draw_rate_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_draw_rate_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_loss_rate_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_loss_rate_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_shots_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_shots_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_shots_on_target_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_shots_on_target_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_shots_conceded_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_shots_conceded_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_shots_on_target_conceded_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_shots_on_target_conceded_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_corners_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_corners_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_corners_conceded_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_corners_conceded_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_fouls_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_fouls_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_fouls_conceded_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_fouls_conceded_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_yellow_cards_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_yellow_cards_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_yellow_cards_conceded_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_yellow_cards_conceded_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_red_cards_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_red_cards_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.merge(df_red_cards_conceded_per_game_last20, how='left', left_on='HomeTeam', right_index=True, suffixes=('', '_home_last20'))
df = df.merge(df_red_cards_conceded_per_game_last20, how='left', left_on='AwayTeam', right_index=True, suffixes=('', '_away_last20'))

df = df.drop(['HomeTeam', 'AwayTeam'], axis=1)
df.to_csv('data/combined_stats.csv', index=False)
print(df.head())