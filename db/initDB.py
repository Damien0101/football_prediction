import sqlite3

conn = sqlite3.connect('db/database.db')
cur = conn.cursor()

teams = """
    CREATE TABLE Teams (
        TeamID INT IDENTITY(1,1) PRIMARY KEY,
        TeamName VARCHAR(50) NOT NULL
    );
"""

matches = """
    CREATE TABLE Matches (
        MatchID INT IDENTITY(1,1) PRIMARY KEY,
        Date NOT NULL,
        Time NOT NULL,
        HomeTeamID INT,
        AwayTeamID INT,
        FOREIGN KEY (HomeTeamID) REFERENCES Teams(TeamID),
        FOREIGN KEY (AwayTeamID) REFERENCES Teams(TeamID)
    );
"""

stats = """
    CREATE TABLE Stats (
        StatID INT INDENTITY(1,1) PRIMARY KEY,
        MatchID INT,
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
        OddsID INT IDENTITY(1,1) PRIMARY KEY,
        MatchID INT,
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
        ResultID INT IDENTITY(1,1) PRIMARY KEY,
        MatchID INT,
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