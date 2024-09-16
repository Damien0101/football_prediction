import streamlit as st
import pandas as pd
import pickle

# Set the page config
st.set_page_config(
    page_title="Jupiler Pro League Dashboard", 
    page_icon="🐂", 
    layout="centered", 
    initial_sidebar_state="expanded")


st.markdown("<img src='https://upload.wikimedia.org/wikipedia/fr/7/7b/Jupiler_Pro_League.png' width='200' style='display: block; margin: 0 auto;'>" , unsafe_allow_html=True)

# Main title
st.title("Welcome to the JPL Dashboard")

# Subtitle
st.subheader("Explore team stats and performance insights!")

# Brief Introduction
st.markdown("""
This dashboard provides real-time insights and detailed statistics from the Jupiler Pro League. 
Dive into team performance metrics, view leaderboard rankings, and explore various statistics on team averages and match results to predict future outcomes.
""")

st.markdown("### Explore the Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('⚽ Match Predictions'):
        st.switch_page('pages/1_⚽_Matches.py')

with col2:
    if st.button('🏆 Stats Leaderboard'):
        st.switch_page('pages/2_🏆_Leaderboard.py')

with col3:
    if st.button('📈 Complete Stats'):
        st.switch_page('pages/3_📈_Complete_Stats.py')



# Highlight some features
st.markdown("""
### Key Features:
- **Match Predictions:** Predict match outcomes based on historical data.
- **Stats Leaderboard:** Get insights into team performance over the last 10 games.
- **Team Insights:** Detailed breakdowns of team performances.
""")


st.markdown("---")
st.write("### Team Members 👨‍👨‍👦‍👦")
st.write("""
         This project was developed by a team of 4 talented data enthusiasts:

- [Damien Compère](https://github.com/servietsky0) - Data Engineer
- [Ben Ozfirat](https://github.com/benozfirat) - Data Analyst
- [Ness Gira](https://github.com/ness015618) - Data Engineer
- [Volodymyr Vysotskyi](https://github.com/vvvladimir65) - Data Analyst
""")