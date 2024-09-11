import pandas as pd
import sqlite3

conn = sqlite3.connect('data/database.db')
cur = conn.cursor()

df = pd.read_csv('data/2324_B1.csv')

for index, row in df.iterrows():
    match_id = index + 1
    fthg = row['FTHG']
    ftag = row['FTAG']
    hthg = row['HTHG']
    htag = row['HTAG']
    hs = row['HS']
    as_ = row['AS']
    hst = row['HST']
    ast = row['AST']
    hf = row['HF']
    af = row['AF']
    hc = row['HC']
    ac = row['AC']
    hy = row['HY']
    ay = row['AY']
    hr = row['HR']
    ar = row['AR']
    
    cur.execute("INSERT INTO Stats (MatchID, FTHG, FTAG, HTHG, HTAG, HS, `AS`, HST, AST, HF, AF, HC, AC, HY, AY, HR, AR) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (match_id, fthg, ftag, hthg, htag, hs, as_, hst, ast, hf, af, hc, ac, hy, ay, hr, ar))
       


for index, row in df.iterrows():
    match_id = index + 1
    psh = row['PSH']
    psd = row['PSD']
    psa = row['PSA']
    avgh = row['AvgH']
    avgd = row['AvgD']
    avga = row['AvgA']
    
    cur.execute("INSERT INTO Results (MatchID, PSH, PSD, PSA, AvgH, AvgD, AvgA) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (match_id, psh, psd, psa, avgh, avgd, avga))
    


for index, row in df.iterrows():
    match_id = index + 1
    date = row['Date']
    time = row['Time']
    home_team_id = row['HomeTeam']
    away_team_id = row['AwayTeam']
    
    cur.execute("INSERT INTO Matches (MatchID, Date, Time, HomeTeamID, AwayTeamID) VALUES (?, ?, ?, ?, ?)",
                (match_id, date, time, home_team_id, away_team_id))

'''
team_names = list(set(df['HomeTeam'].unique() + df['AwayTeam'].unique()))    

for team_name in team_names:
    cur.execute("INSERT INTO Teams (TeamName) VALUES (?)", (team_name,))
'''
conn.commit()

