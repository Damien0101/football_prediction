import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import pickle
from sklearn.preprocessing import OneHotEncoder
from PIL import Image
import io
import os 
import base64 
pd.options.display.max_columns = 50

st.set_page_config(page_title="Football Match Prediction", page_icon=":soccer:")

button_html = """
<a href="https://footballpredict.streamlit.app/" style="display: block; text-align: center; margin: 0 auto;">
    <img src='https://upload.wikimedia.org/wikipedia/fr/7/7b/Jupiler_Pro_League.png' width='200' style='display: block; margin: 0 auto;'>
</a>
"""

st.markdown(button_html, unsafe_allow_html=True)

def get_odds(probabilities):
    return round(1 / probabilities, 2)

def get_prediction_label(probabilities):
    home_win_prob = probabilities[0]
    draw_prob = probabilities[2]
    away_win_prob = probabilities[1]
    max_prob = max(home_win_prob, draw_prob, away_win_prob)
    if max_prob == home_win_prob:
        return 'Home Win'
    elif max_prob == draw_prob:
        return 'Draw'
    else:
        return 'Away Win'

def resize_image(image_path, size=(150, 150)):

    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found or is a directory: {image_path}")
    
    try:
        with Image.open(image_path) as img:

            img = img.resize(size, Image.Resampling.LANCZOS)
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            return buf.getvalue()
    except Exception as e:
        print(f"Error resizing image: {e}")
        raise

def get_image_path(team_name):
    placeholder_image_path = 'utils/images/logos/placeholder.png'
    image_path = f'utils/images/logos/{team_name}.png'

    try:
        team_logo = resize_image(image_path)
    except FileNotFoundError:
        try:
            team_logo = resize_image(placeholder_image_path)
        except Exception as e:
            print(f"Error loading placeholder image: {e}")
            team_logo = None
    
    return team_logo, placeholder_image_path


df_stats = pd.read_csv('data/averages_predict.csv')
futures_matchs = pd.read_csv('data/future_matches.csv')

def get_stats_for_future_matches(futures_matchs, df_stats):
    futures_stats = []
    for index, row in futures_matchs.iterrows():
        home_team = row['HomeTeam']
        away_team = row['AwayTeam']
        

        home_stats = df_stats[(df_stats['HomeTeam'] == home_team) | (df_stats['AwayTeam'] == home_team)]
        away_stats = df_stats[(df_stats['HomeTeam'] == away_team) | (df_stats['AwayTeam'] == away_team)]


        if not home_stats.empty:
            home_stats_row = home_stats.iloc[0]
        else:
            home_stats_row = pd.Series(dtype='float64')  

        if not away_stats.empty:
            away_stats_row = away_stats.iloc[0]
        else:
            away_stats_row = pd.Series(dtype='float64')  

        row_stats = {
            'HomeTeam': home_team,
            'AwayTeam': away_team,
            'head_to_head_games': home_stats_row.get('head_to_head_games', 0),
            'head_to_head_goals_scored_home_team': home_stats_row.get('head_to_head_goals_scored_home_team', 0),
            'head_to_head_goals_conceded_home_team': home_stats_row.get('head_to_head_goals_conceded_home_team', 0),
            'head_to_head_goals_scored_away_team': away_stats_row.get('head_to_head_goals_scored_away_team', 0),
            'head_to_head_goals_conceded_away_team': away_stats_row.get('head_to_head_goals_conceded_away_team', 0),
            'home_average_goals_scored_5': home_stats_row.get('home_average_goals_scored_5', 0),
            'home_average_goals_conceded_5': home_stats_row.get('home_average_goals_conceded_5', 0),
            'home_average_goal_difference_5': home_stats_row.get('home_average_goal_difference_5', 0),
            'away_average_goals_scored_5': home_stats_row.get('away_average_goals_scored_5', 0),
            'away_average_goals_conceded_5': home_stats_row.get('away_average_goals_conceded_5', 0),
            'away_average_goal_difference_5': home_stats_row.get('away_average_goal_difference_5', 0),
            'home_average_goals_scored_10': home_stats_row.get('home_average_goals_scored_10', 0),
            'home_average_goals_conceded_10': home_stats_row.get('home_average_goals_conceded_10', 0),
            'home_average_goal_difference_10': home_stats_row.get('home_average_goal_difference_10', 0),
            'away_average_goals_scored_10': home_stats_row.get('away_average_goals_scored_10', 0),
            'away_average_goals_conceded_10': home_stats_row.get('away_average_goals_conceded_10', 0),
            'away_average_goal_difference_10': away_stats_row.get('away_average_goal_difference_10', 0),
            'home_average_goals_scored_20': home_stats_row.get('home_average_goals_scored_20', 0),
            'home_average_goals_conceded_20': home_stats_row.get('home_average_goals_conceded_20', 0),
            'home_average_goal_difference_20': home_stats_row.get('home_average_goal_difference_20', 0),
            'away_average_goals_scored_20': away_stats_row.get('away_average_goals_scored_20', 0),
            'away_average_goals_conceded_20': away_stats_row.get('away_average_goals_conceded_20', 0),
            'away_average_goal_difference_20': away_stats_row.get('away_average_goal_difference_20', 0),
        }

        futures_stats.append(row_stats)

    return pd.DataFrame(futures_stats)


model = pickle.load(open('utils/model/logistic_regression_model.pkl', 'rb'))
preprocessor = pickle.load(open('utils/model/onehot_encoder.pkl', 'rb'))


futures_stats = get_stats_for_future_matches(futures_matchs, df_stats)


categorical_features = ['HomeTeam', 'AwayTeam']
futures_stats_encoded = preprocessor.transform(futures_stats[categorical_features])
futures_stats_encoded = pd.DataFrame(futures_stats_encoded, columns=preprocessor.get_feature_names_out(categorical_features))
futures_stats = pd.concat([futures_stats.drop(columns=categorical_features), futures_stats_encoded], axis=1)


probabilities = model.predict_proba(futures_stats)
predictions = [get_prediction_label(prob) for prob in probabilities]


st.markdown("<h1 style='text-align: center;'>Matches ⚽ </h1>", unsafe_allow_html=True)

days = sorted(futures_matchs['day'].unique())
select_day = st.selectbox('Select a day:', days)
day_matches = futures_matchs[futures_matchs['day'] == select_day].reset_index(drop=True)


st.header(f"Matches for Day {select_day}")


for index, row in day_matches.iterrows():
    HomeTeam = row['HomeTeam']
    AwayTeam = row['AwayTeam']
    home_team_logo, placeholder_image_path = get_image_path(HomeTeam)
    away_team_logo, _ = get_image_path(AwayTeam)

    with st.expander(f"Match {index + 1}: {HomeTeam} vs {AwayTeam}"):
        col1, col2, col3 = st.columns([1, 0.2, 1])

        with col1:
            if home_team_logo:
                home_team_logo_base64 = base64.b64encode(home_team_logo).decode()
                st.markdown(
                    f'<div style="text-align: right;"><img src="data:image/png;base64,{home_team_logo_base64}" width="150" /></div>',
                    unsafe_allow_html=True
                )
            else:
                st.write("Image not available")

        with col2:
            st.markdown(
                "<h2 style='text-align: center; margin-top: 30px;'>vs</h2>", 
                unsafe_allow_html=True
            )

        with col3:
            if away_team_logo:
                away_team_logo_base64 = base64.b64encode(away_team_logo).decode()
                st.markdown(
                    f'<div style="text-align: left;"><img src="data:image/png;base64,{away_team_logo_base64}" width="150" /></div>',
                    unsafe_allow_html=True
                )
            else:
                st.write("Image not available")

        home_win_prob = probabilities[index][0]
        draw_prob = probabilities[index][2]
        away_win_prob = probabilities[index][1]

        # Calculate odds
        home_win_odds = get_odds(home_win_prob)
        draw_odds = get_odds(draw_prob)
        away_win_odds = get_odds(away_win_prob)

        fig = go.Figure(data=[
            go.Bar(
                y=[''],
                x=[probabilities[index][0]],
                name='Home Win',
                orientation='h',
                marker=dict(color='#003566')
            ),
            go.Bar(
                y=[''],
                x=[probabilities[index][2]],
                name='Draw',
                orientation='h',
                marker=dict(color='#fcd5ce')
            ),
            go.Bar(
                y=[''],
                x=[probabilities[index][1]],
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

        table = {
            'Match': f"{row['HomeTeam']} vs {row['AwayTeam']}",
            'Home Win': f"{probabilities[index][0]:.2f}",
            'Draw': f"{probabilities[index][2]:.2f}",
            'Away Win': f"{probabilities[index][1]:.2f}",
            'Prediction': predictions[index]

        }

        odds = {
            'Match': f"{row['HomeTeam']} vs {row['AwayTeam']}",
            'Home Win': home_win_odds,
            'Draw': draw_odds,
            'Away Win': away_win_odds
        }
        
        st.write(pd.DataFrame([table]).set_index('Match'))
        st.write(pd.DataFrame([odds]).set_index('Match'))