import streamlit as st
import pandas as pd
import plotly.express as px

# 
df = pd.read_csv('data/dataset.csv')


# User selects home team
home_team = st.selectbox('Select Home Team', options=df['HomeTeam'].unique())

# User selects away team
away_team = st.selectbox('Select Away Team', options=df['AwayTeam'].unique())

# Filter Data for Selected Teams
home_team_data = df[df['HomeTeam'] == home_team]
away_team_data = df[df['AwayTeam'] == away_team]

# Calculate totals
home_total = home_team_data.shape[0]
away_total = away_team_data.shape[0]

# Count Wins, Losses, Draws for Home Team
home_number_win = home_team_data[home_team_data['FTR'] == 1].shape[0]
home_number_loss = home_team_data[home_team_data['FTR'] == -1].shape[0]
home_number_draw = home_team_data[home_team_data['FTR'] == 0].shape[0]

# Count Wins, Losses, Draws for Away Team
away_number_win = away_team_data[away_team_data['FTR'] == 1].shape[0]
away_number_loss = away_team_data[away_team_data['FTR'] == -1].shape[0]
away_number_draw = away_team_data[away_team_data['FTR'] == 0].shape[0]


# Prepare Data for Plotting
teams = [home_team, away_team]
data = {
    'Team': teams,
    'Totals': [home_total, away_total],
    'Wins': [home_number_win, away_number_win],
    'Losses': [home_number_loss, away_number_loss],
    'Draws': [home_number_draw, away_number_draw]
}

# Create DataFrame for Plotly
plot_data = pd.DataFrame(data)

# Melt the DataFrame to make it suitable for Plotly Express
plot_data_melted = plot_data.melt(id_vars='Team', value_vars=['Totals', 'Wins', 'Losses', 'Draws'])

# Create a bar chart using Plotly Express
fig = px.bar(plot_data_melted, x='Team', y='value', color='variable',
             title='Home and Away Record',
             labels={'value': 'Number of Matches'},
             barmode='group')

# Display the Plotly chart in Streamlit
st.plotly_chart(fig)