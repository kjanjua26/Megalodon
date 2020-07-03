"""
This is the script to get shark species images from Google.
We have scrapped the list of shark species from this Wikipedia page article.
Link: https://en.wikipedia.org/wiki/List_of_sharks
This is only for educational and research purposes.
The images are scrapped from Google.
"""

from bs4 import BeautifulSoup
import requests, re, time
import os
from urllib.request import Request, urlopen

basepath_species = '/Users/Janjua/Desktop/Projects/Megalodon/List-of-Species/data/'
basepath_images = '/Users/Janjua/Desktop/Projects/Megalodon/Finegrained-Images/data/'

def page(url, header) -> BeautifulSoup:
    req = Request(url, headers=header)
    webpage = urlopen(req).read()
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')

def download_images_with_query(name):
    query = name.split()
    query = '+'.join(query)
    url = "https://www.google.co.in/search?q="+ query +"&source=lnms&tbm=isch"
    print("URL to fetch from: ", url)
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = page(url, header)
    imgs = soup.find_all('img', attrs={'class': 'rg_i Q4LuWd'})
    print("Len: ", len(imgs))
    count = 0
    for img in imgs:
        count += 1
        if count > 21:
            local_count = 1
            img = str(img)
            imgUrl = img.split('src="')[-1].replace('"', '').replace('/>', '').split(' ')[0]
            try:
                if not os.path.exists(os.path.join(basepath_images, name)):
                    os.makedirs(os.path.join(basepath_images, name))
                with open(os.join(basepath_images, name) + "{}.jpg".format(local_count), 'wb') as f:
                    response = requests.get(imgUrl)
                    f.write(response.content)
            except:
                print("Failed")
            print(imgUrl)
            local_count += 1
            print()

speices_list = open(os.path.join(basepath_species, 'species.txt'), 'r').readlines()
for specie in speices_list:
    download_images_with_query(specie.strip())
    exit()