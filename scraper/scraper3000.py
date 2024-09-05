import requests
import cloudscraper

scraper = cloudscraper.CloudScraper()
print(scraper.get('https://fr.whoscored.com/'))