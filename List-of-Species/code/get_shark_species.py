"""
This is the script to get shark species from Wikipedia.
We have scrapped the list of shark species from this Wikipedia page article.
Link: https://en.wikipedia.org/wiki/List_of_sharks
This is only for educational and research purposes.
"""

import glob, os, tqdm
import requests, re
import BeautifulSoup as bs4
