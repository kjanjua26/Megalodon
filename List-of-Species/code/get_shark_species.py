"""
This is the script to get shark species from Wikipedia.
We have scrapped the list of shark species from this Wikipedia page article.
Link: https://en.wikipedia.org/wiki/List_of_sharks
This is only for educational and research purposes.
"""

import glob, os, tqdm
import requests, re, time
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
from selenium import webdriver

basepath = '/Users/Janjua/Desktop/Projects/Megalodon/List-of-Species/data/'

def page(url, header) -> BeautifulSoup:
    req = Request(url, headers=header)
    webpage = urlopen(req).read()
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')

url = "https://en.wikipedia.org/wiki/List_of_sharks"
header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
soup = page(url, header)

list_of_species = soup.find('div', attrs={'class': 'mw-parser-output'})
headers = soup.find_all('span', attrs={'class': 'mw-headline'})

for ix, headline in enumerate(headers):
    head = headline.text
    if "sharks" in head:
        print(ix, head)

list_of_sharks = (list_of_species.text.split('Alphabetic sort[edit]')[-1].split('See also[edit]')[0])
list_of_sharks = list_of_sharks.split('\n')
species_list = open(os.path.join(basepath + 'species_list_extensive.txt'), 'w+')

for ix, shark in enumerate(list_of_sharks):
    if len(shark) > 1:
        species_list.write(shark + '\n')
        print(ix, shark)

species_list.close()