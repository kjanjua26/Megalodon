"""
Some exploratory data analysis to check the data distribution.
"""
import glob, os
import matplotlib.pyplot as plt
from typing import List, Dict
plt.style.use('fivethirtyeight')

basepath = "/Users/Janjua/Desktop/Projects/Megalodon/Finegrained-Images/data/"

list_of_species: List = [x for x in glob.glob(basepath + "*")]
species_count: Dict = {}
print('Total species are: ', len(list_of_species))

for ix, specie in enumerate(list_of_species):
    imgs = [x for x in glob.glob(specie + "/*.jpg".format(specie))]
    name = specie.split('/')[-1].split(' Shark')[0]
    species_count[name] = len(imgs)

plt.xticks(fontsize=5, rotation=70)
plt.bar(species_count.keys(), species_count.values())
plt.show()