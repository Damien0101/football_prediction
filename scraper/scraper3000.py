import cloudscraper
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup as bs
import pandas as pd

scraper = cloudscraper.create_scraper()
response = scraper.get('https://www.football-data.co.uk/belgiumm.php').content

soup = bs(response, 'html.parser')

csv_links = [link.get('href') for link in soup.find_all('a', href=True, string='Jupiler League')]

for i, csvf in enumerate(csv_links):
    url = f'https://www.football-data.co.uk/{csvf}'
    response = scraper.get(url)
    
    file_name = f'data/dataset{i+1}.csv'
    with open(file_name, 'wb') as file:
        file.write(response.content)

# 2019 - 25 same columns before noope 

for i in range(30+1):
    df = pd.read_fwf(f'data/dataset{i}.csv')
    print(df.columns)
    print(i)





'''scraper = cloudscraper.create_scraper()
response = scraper.get('https://fr.whoscored.com/')

html = HTMLParser(response.text)

print(html)'''
