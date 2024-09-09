import sqlite3

conn = sqlite3.connect('db.db')
cur = conn.cursor()

teams = """
    CREATE TABLE Teams (
        TeamID INTEGER PRIMARY KEY AUTOINCREMENT,
        TeamName VARCHAR(50) NOT NULL
    );
"""

matches = """
    CREATE TABLE Matches (
        MatchID INTEGER PRIMARY KEY AUTOINCREMENT,
        Date TEXT NOT NULL,
        Time TEXT NOT NULL,
        HomeTeamID INTEGER,
        AwayTeamID INTEGER,
        FOREIGN KEY (HomeTeamID) REFERENCES Teams(TeamID),
        FOREIGN KEY (AwayTeamID) REFERENCES Teams(TeamID)
    );
"""

stats = """
    CREATE TABLE Stats (
        StatID INTEGER PRIMARY KEY AUTOINCREMENT,
        MatchID INTEGER,
        FTHG INT,     
        FTAG INT,     
        HTHG INT,   
        HTAG INT,     
        HS INT,
        `AS` INT,       
        HST INT,     
        AST INT,    
        HF INT,      
        AF INT,     
        HC INT,       
        AC INT,
        HY INT,       
        AY INT,    
        HR INT,       
        AR INT,       
        FOREIGN KEY (MatchID) REFERENCES Matches(MatchID)
    );
"""

odds = """
    CREATE TABLE Odds (
        OddsID INTEGER PRIMARY KEY AUTOINCREMENT,
        MatchID INTEGER,
        PSH DECIMAL(5,2),    
        PSD DECIMAL(5,2),    
        PSA DECIMAL(5,2),    
        AvgH DECIMAL(5,2),   
        AvgD DECIMAL(5,2),   
        AvgA DECIMAL(5,2),   
        FOREIGN KEY (MatchID) REFERENCES Matches(MatchID)
    );
"""

results = """
    CREATE TABLE Results (
        ResultID INTEGER PRIMARY KEY AUTOINCREMENT,
        MatchID INTEGER,
        PSH DECIMAL(5,2),    
        PSD DECIMAL(5,2),    
        PSA DECIMAL(5,2),  
        AvgH DECIMAL(5,2),  
        AvgD DECIMAL(5,2),  
        AvgA DECIMAL(5,2),   
        FOREIGN KEY (MatchID) REFERENCES Matches(MatchID)
    );
"""

cur.execute(teams)
cur.execute(matches)
cur.execute(stats)
cur.execute(odds)
cur.execute(results)

conn.commit()
conn.close()
