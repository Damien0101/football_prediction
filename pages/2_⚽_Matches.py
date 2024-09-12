import streamlit as st
import pandas as pd
import pickle
from utils.preprocess.draft import get_head_to_head_stats, get_stats
import plotly.graph_objects as go

st.set_page_config(page_title="Matches", page_icon=":soccer:")

# Load model and preprocessor
preprocessor = pickle.load(open('utils/model/onehot_encoder.pkl', 'rb'))
model = pickle.load(open('utils/model/logistic_regression_model.pkl', 'rb'))

def get_stats_for_future_matches(future_df, stats_df):
    futures_stats = []
    for index, row in future_df.iterrows():
        home_team = row['HomeTeam']
        away_team = row['AwayTeam']
        head_to_head_stats = get_head_to_head_stats(stats_df, home_team, away_team)
        Home_stats_5 = get_stats(stats_df, [home_team], 'home', 5)
        Away_stats_5 = get_stats(stats_df, [away_team], 'away', 5)
        Home_stats_10 = get_stats(stats_df, [home_team], 'home', 10)
        Away_stats_10 = get_stats(stats_df, [away_team], 'away', 10)
        Home_stats_20 = get_stats(stats_df, [home_team], 'home', 20)
        Away_stats_20 = get_stats(stats_df, [away_team], 'away', 20)

        row_stats = {
            'HomeTeam': home_team,
            'AwayTeam': away_team,
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
        futures_stats.append(row_stats)
    return pd.DataFrame(futures_stats)


def get_prediction_label(probabilities):
    # Determine the prediction based on the highest probability
    home_win_prob = probabilities[0]
    draw_prob = probabilities[2]
    away_win_prob = probabilities[1]
    max_prob = max(home_win_prob, draw_prob, away_win_prob)
    if max_prob == home_win_prob:
        return f'Home Win'
    elif max_prob == draw_prob:
        return 'Draw'
    else:
        return f'Away Win'
# Load data
df_stats = pd.read_csv('data/dataset.csv')
df_futures_matches = pd.read_csv('data/future_matches.csv')

st.title("Matches")

# Select day
days = sorted(df_futures_matches['Day'].unique())
select_day = st.selectbox('Select a day:', days)
day_matches = df_futures_matches[df_futures_matches['Day'] == select_day].reset_index(drop=True)
matches_stats_df = get_stats_for_future_matches(day_matches, df_stats)

# Process matches data
ohetransform = preprocessor.transform(matches_stats_df[['HomeTeam', 'AwayTeam']])
encoded_matches = pd.concat([matches_stats_df, pd.DataFrame(ohetransform)], axis=1).drop(columns=['HomeTeam', 'AwayTeam'])
predictions = model.predict(encoded_matches)
predictions_proba = model.predict_proba(encoded_matches)

st.header(f"Matches for Day {select_day}")


for index, row in day_matches.iterrows():
    table = []
    with st.expander(f"Match {index + 1}: {row['HomeTeam']} vs {row['AwayTeam']}"):
        st.write(f"Prediction: {get_prediction_label(predictions_proba[index])}")

        fig = go.Figure(data=[
                    go.Bar(
                        y=[''],
                        x=[predictions_proba[index][0]],
                        name='Home Win',
                        orientation='h',
                        marker=dict(color='#003566')
                    ),
                    go.Bar(
                        y=[''],
                        x=[predictions_proba[index][2]],
                        name='Draw',
                        orientation='h',
                        marker=dict(color='#fcd5ce')
                    ),
                    go.Bar(
                        y=[''],
                        x=[predictions_proba[index][1]],
                        name='Away Win',
                        orientation='h',
                        marker=dict(color='#FE5F55')
                    )
                ])
                
        fig.update_layout(
            barmode='stack',
            title='Probability',
            xaxis_title='',
            yaxis_title='',
            xaxis=dict(range=[0, 1],
                       showgrid=False,
                       showticklabels=False),
            showlegend=True,
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='right',
                x=1
            ),
            height=200
        )
        st.plotly_chart(fig)

        table.append({
            'Match': f"{row['HomeTeam']} vs {row['AwayTeam']}",
            'Prediction': get_prediction_label(predictions_proba[index]),
            'Home Win Probability': predictions_proba[index][0],
            'Draw Probability': predictions_proba[index][2],
            'Away Win Probability': predictions_proba[index][1]
        })
        
        probabilities_df = pd.DataFrame(table)

        probabilities_df.set_index('Match', inplace=True)

        # Display the table
        st.write(probabilities_df)
        