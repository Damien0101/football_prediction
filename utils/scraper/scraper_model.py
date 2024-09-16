import cloudscraper
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import regex as re


# instantiate the cloudscraper object
scraper = cloudscraper.create_scraper()

def fetch_and_parse_html(url: str) -> bs:
    """ Fetches and parses the HTML content of the webpage. """ 
    response = scraper.get(url)
    return bs(response.content, 'html.parser')


def extract_csv_links(soup: bs, link_text: str = 'Jupiler League') -> list[str]:
    """ Extracts CSV links for the given link text from the soup object. """
    csv_links = [link.get('href') for link in soup.find_all('a', href=True, string=link_text)]
    return csv_links


            
def check_for_update(csv_links: list[str], save_dir: str = '/home/servietske/Desktop/Becode/football_prediction/data/') -> None:
    """ Checks if the CSV files are up to date and updates them if necessary. """
    url = f'https://www.football-data.co.uk/{csv_links[0]}'
    response = scraper.get(url)
    match = re.match(r'\b([0-2][0-9]|3[01])/([0][1-9]|1[0-2])/([0-9]{4})\b', str(response.content))
    return match

    

url = 'https://www.football-data.co.uk/belgiumm.php'
soup = fetch_and_parse_html(url)
csv_links = extract_csv_links(soup)
print(check_for_update(csv_links))











'''def save_csv_files(csv_links: list[str], save_dir: str = '/home/servietske/Desktop/Becode/football_prediction/data/') -> None:
    """ Downloads CSV files from the provided links and saves them locally. """
    url = f'https://www.football-data.co.uk/{csv_links[0]}'
    response = scraper.get(url)

    file_name = f'{csv_links[0][8:].replace("/", "_")}'
    file_names = os.listdir(save_dir)

    if os.path.getsize(f'/home/servietske/Desktop/Becode/football_prediction/data/{file_names[-1]}') == len(response.content):
        print('updating file...')
        with open(file_name, 'wb') as file:
            file.write(response.content)
    else:
        print('file is up to date')

    if csv_links[0] == file_names[-1]:
        print('adding new file...')
        with open(file_name, 'wb') as file:
            file.write(response.content)
    else:  
        print('file is up to date')'''
