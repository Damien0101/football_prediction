import cloudscraper
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

def scrape_match_links_without_scores(url):
    scraper = cloudscraper.create_scraper()
    page = scraper.get(url)
    soup = bs(page.content, 'html.parser')
    
    score_pattern = re.compile(r'\d+-\d+')

    links = [link.get('href') for link in soup.find_all('a', href=True) if not score_pattern.search(link.text)]
    return [i[50:] for i in links if 'journee' in i]

def process_matches(match_links):
    clean_matches = [i.split('/') for i in match_links if i]
    matches = [i for i in clean_matches if i != ['-']]
    day = [i[0] for i in matches]
    day = [int(item.split('-')[1]) for item in day]

    team_a = [i[1] for i in matches]
    team_b = [i[2] for i in matches]
    return day, team_a, team_b

def map_team_names(team_list, mapping):
    return [mapping.get(team, team) for team in team_list]

old_team_names = ['la-gantoise', 'charleroi', 'fc-bruges', 'kv-kortrijk', 'cercle-brugge', 'standard', 
                  'fcv-dender-eh', 'kv-mechelen', 'oh-leuven', 'beerschot', 'anderlecht', 
                  'sint-truiden', 'antwerp', 'union-sg', 'westerlo', 'krc-genk']
new_team_names = ['Gent', 'Charleroi', 'Club Brugge', 'Kortrijk', 'Cercle Brugge', 'Standard', 
                  'Dender', 'Mechelen', 'Oud-Heverlee Leuven', 'Beerschot VA', 'Anderlecht', 
                  'St Truiden', 'Antwerp', 'St. Gilloise', 'Westerlo', 'Genk']

team_name_mapping = dict(zip(old_team_names, new_team_names))

url = 'https://www.walfoot.be/belgique/jupiler-pro-league/calendrier'

match_links = scrape_match_links_without_scores(url)
day, team_a, team_b = process_matches(match_links)

team_a_mapped = map_team_names(team_a, team_name_mapping)
team_b_mapped = map_team_names(team_b, team_name_mapping)

df = pd.DataFrame(data={"day": day, "HomeTeam": team_a_mapped, "AwayTeam": team_b_mapped})
df.to_csv("data/matchs.csv", sep=',', index=False)
