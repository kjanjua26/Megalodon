"""
Some exploratory data analysis to check the data distribution.
"""
import glob, os
import matplotlib.pyplot as plt
from typing import List, Dict
#plt.style('fivethirtyeight')

basepath = "/Users/Janjua/Desktop/Projects/Megalodon/Finegrained-Images/data/"

list_of_species: List = [x for x in glob.glob(basepath + "*")]
species_count: Dict = {}
print('Total species are: ', len(list_of_species))

for ix, specie in enumerate(list_of_species):
    

