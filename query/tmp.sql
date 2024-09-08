--test
insert into teams (TeamName) values ('standarddebruge');

select * from teams
where TeamName = 'standarddebruge';

insert into teams (TeamName) values ('Team A');
insert into teams (TeamName) values ('Team B');
insert into teams (TeamName) values ('Team C');

insert into matches (Date, Time, HomeTeamID, AwayTeamID) values ('2023-09-15', '18:00', 1, 2);
insert into matches (Date, Time, HomeTeamID, AwayTeamID) values ('2023-09-16', '20:00', 3, 1);

select * from Teams
select * from Matches

select 
    matches.MatchID,
    teams.TeamName as HomeTeam,
    away.TeamName as AwayTeam,
    matches.Date,
    matches.Time
from 
    matches
join 
    teams on matches.HomeTeamID = teams.TeamID
join 
    teams as away on matches.AwayTeamID = away.TeamID;
