# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px



# Streamlit configuration: Set up the page title and icon
st.set_page_config(page_title="Leaderboard", page_icon="🏆")

button_html = """
<a href="http://localhost:8501" style="display: block; text-align: center; margin: 0 auto;">
    <img src='https://upload.wikimedia.org/wikipedia/fr/7/7b/Jupiler_Pro_League.png' width='200' style='display: block; margin: 0 auto;'>
</a>
"""

st.markdown(button_html, unsafe_allow_html=True)

# Display the header of the app
st.markdown("<h1 style='text-align: center;'>Stats Leaderboard 🏆 </h1>", unsafe_allow_html=True)



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





# Best Offense over the last 10 games
st.subheader('Best offense over the last 10 games (Goals Scored)')

fig3 = df_last_10[['team', '10_AGS']].sort_values('10_AGS', ascending=False).head(3)
fig3 = fig3.rename(columns={'team': 'Teams', '10_AGS': 'Average Goals Scored'})
fig3['Average Goals Scored'] = fig3['Average Goals Scored'].round(2)
df_top3 = fig3.head(3)
df_top3['Rank'] = [1.5, 1, 0.5]
df_top3_podium = [df_top3.iloc[1], df_top3.iloc[0], df_top3.iloc[2]]

fig3 = px.bar(df_top3_podium, x='Teams', y="Rank", text="Average Goals Scored",
                color=['#C0C0C0', "#FFD700", '#CD7F32'],
                height=600, width=800)
fig3.update_layout(yaxis=dict(range=[0, 3]), showlegend=False)
st.plotly_chart(fig3)

#Best Defense over the last 10 games
st.subheader('Best Defense over the last 10 games (Goal Conceded)')

fig4 = df_last_10[['team', '10_AGC']].sort_values('10_AGC', ascending=True).head(3)
fig4 = fig4.rename(columns={'team': 'Teams', '10_AGC': 'Average Goals Conceded'})
fig4['Average Goals Conceded'] = fig4['Average Goals Conceded'].round(2)
df_top3 = fig4.head(3)
df_top3['Rank'] = [1.5, 1, 0.5]
df_top3_podium = [df_top3.iloc[1], df_top3.iloc[0], df_top3.iloc[2]]

fig4 = px.bar(df_top3_podium, x='Teams', y="Rank", text="Average Goals Conceded",
                color=['#C0C0C0', "#FFD700", '#CD7F32'],
                height=600, width=800)
fig4.update_layout(yaxis=dict(range=[0, 3]), showlegend=False)
st.plotly_chart(fig4)


# Most Shots on Target over the last 10 games
st.subheader('Most Shots on Target over the last 10 games')

fig5 = df_last_10[['team', '10_AST']].sort_values('10_AST', ascending=False).head(3)
fig5 = fig5.rename(columns={'team': 'Teams', '10_AST': 'Average Shots on Target'})
fig5['Average Shots on Target'] = fig5['Average Shots on Target'].round(2)
df_top3 = fig5.head(3)
df_top3['Rank'] = [1.5, 1, 0.5]
df_top3_podium = [df_top3.iloc[1], df_top3.iloc[0], df_top3.iloc[2]]

fig5 = px.bar(df_top3_podium, x='Teams', y="Rank", text="Average Shots on Target",
                color=['#C0C0C0', "#FFD700", '#CD7F32'],
                height=600, width=800)
fig5.update_layout(yaxis=dict(range=[0, 3]), showlegend=False)
st.plotly_chart(fig5)


# Most Corner Kicks over the last 10 games
st.subheader('Most Corner Kicks over the last 10 games')

fig6 = df_last_10[['team', '10_AC']].sort_values('10_AC', ascending=False).head(3)
fig6 = fig6.rename(columns={'team': 'Teams', '10_AC': 'Average Corners'})
fig6['Average Corners'] = fig6['Average Corners'].round(2)
df_top3 = fig6.head(3)
df_top3['Rank'] = [1.5, 1, 0.5]
df_top3_podium = [df_top3.iloc[1], df_top3.iloc[0], df_top3.iloc[2]]

fig6 = px.bar(df_top3_podium, x='Teams', y="Rank", text="Average Corners",
                color=['#C0C0C0', "#FFD700", '#CD7F32'],
                height=600, width=800)
fig6.update_layout(yaxis=dict(range=[0, 3]), showlegend=False)
st.plotly_chart(fig6)


# Most Fouls over the last 10 games
st.subheader('Most Fouls over the last 10 games')

fig7 = df_last_10[['team', '10_AF']].sort_values('10_AF', ascending=False).head(3)
fig7 = fig7.rename(columns={'team': 'Teams', '10_AF': 'Average Fouls'})
fig7['Average Fouls'] = fig7['Average Fouls'].round(2)
df_top3 = fig7.head(3)
df_top3['Rank'] = [1.5, 1, 0.5]
df_top3_podium = [df_top3.iloc[1], df_top3.iloc[0], df_top3.iloc[2]]

fig7 = px.bar(df_top3_podium, x='Teams', y="Rank", text="Average Fouls",
                color=['#C0C0C0', "#FFD700", '#CD7F32'],
                height=600, width=800)
fig7.update_layout(yaxis=dict(range=[0, 3]), showlegend=False)
st.plotly_chart(fig7)