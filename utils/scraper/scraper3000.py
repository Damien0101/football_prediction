import cloudscraper
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup as bs
import pandas as pd


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


def save_csv_files(csv_links: list[str], save_dir: str = 'data/') -> None:
    """ Downloads CSV files from the provided links and saves them locally. """
    for i, csv_link in enumerate(csv_links[:8]):
        url = f'https://www.football-data.co.uk/{csv_link}'
        response = scraper.get(url)
        file_name = f'{save_dir}dataset{i+1}.csv'
        with open(file_name, 'wb') as file:
            file.write(response.content)


url = 'https://www.football-data.co.uk/belgiumm.php'
soup = fetch_and_parse_html(url)
csv_links = extract_csv_links(soup)
save_csv_files(csv_links)



''' # get all the columns name from the csvs
with open('col_name.txt', 'a', newline='') as csv:
    for i in range(30):
        df = pd.read_fwf(f'dataa/dataset{i+1}.csv')
        col = list(df.columns)
        csv.write(f'\n csv n°{i+1} \n {col}\n')
'''



