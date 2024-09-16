import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd


st.set_page_config(page_title="Stats", page_icon=":graph:", layout="wide")

button_html = """
<a href="http://localhost:8501" style="display: block; text-align: center; margin: 0 auto;">
    <img src='https://upload.wikimedia.org/wikipedia/fr/7/7b/Jupiler_Pro_League.png' width='200' style='display: block; margin: 0 auto;'>
</a>
"""

st.markdown(button_html, unsafe_allow_html=True)


def display_aggrid_table(df, title="Table infos", height=400):
    st.write(title)
    gb = GridOptionsBuilder.from_dataframe(df,axis=1)
    gb.configure_pagination()
    gb.configure_side_bar()
    gb.configure_selection('single')
    gb.configure_default_column(resizable=True, supressmenu=True, )
    gb.configure_column("team", width=250)
    gridOptions = gb.build()
    AgGrid(df, gridOptions=gridOptions, height=height, fit_columns_on_grid_load=True)


st.markdown("<h1 style='text-align: center;'>Stats over the last games 📈 </h1>", unsafe_allow_html=True)



st.markdown("""
AGS = Average Goals Scored<br>
AGC = Average Goals Conceded<br>
AGD = Average Goals Difference<br>
AS = Average Shots<br>
AST = Average Shots on Target<br>
AF = Average Fouls<br>
AC = Average Corners<br>
AY = Average Yellow Cards<br>
AR = Average Red Cards<br>
""", unsafe_allow_html=True)

df_last_5 = pd.read_csv('data/team_averages_last_5_games.csv')
df_last_10 = pd.read_csv('data/team_averages_last_10_games.csv')
df_last_20 = pd.read_csv('data/team_averages_last_20_games.csv')

team_in_the_league = ['Dender','Westerlo','Mechelen','Genk','Club Brugge',
                      'Anderlecht','Standard','Charleroi','Gent',
                      'Cercle Brugge','Beerschot VA','Kortrijk',
                      'Antwerp','St Truiden', 'St. Gilloise', 'Oud-Heverlee Leuven']

df_last_5 = df_last_5[df_last_5['team'].isin(team_in_the_league)]
df_last_10 = df_last_10[df_last_10['team'].isin(team_in_the_league)]
df_last_20 = df_last_20[df_last_20['team'].isin(team_in_the_league)]


st.title('Stats over the last 5 games 5️⃣')
df_last_5_filtered = df_last_5[[col for col in df_last_5.columns if col.startswith('team') or col.startswith('5')]]
display_aggrid_table(df_last_5_filtered, title=" ", height=550)

st.title('Stats over the last 10 games 1️⃣0️⃣')
df_last_10_filtered = df_last_10[[col for col in df_last_10.columns if col.startswith('team') or col.startswith('10')]]
display_aggrid_table(df_last_10_filtered, title=" ", height=550)

st.title('Stats over the last 20 games' '2️⃣0️⃣')
df_last_20_filtered = df_last_20[[col for col in df_last_20.columns if col.startswith('team') or col.startswith('20')]]
display_aggrid_table(df_last_20_filtered, title=" ", height=550)





