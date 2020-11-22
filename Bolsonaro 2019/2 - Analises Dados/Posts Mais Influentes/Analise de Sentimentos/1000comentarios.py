# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:23:27 2020

@author: danie
"""


import pandas as pd
from unicodedata import normalize
import string  

base = pd.read_csv('dados.csv', delimiter=";")

base = base.sort_values(by='like_count', ascending=False)
base.dropna(subset = ["message"], inplace=True)
base.drop_duplicates(subset = ["message"], inplace=True)

base2 = base.head(1000)

def remover_acentos(txt):
     return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
 
def remove_punctuations(text):
    for punctuation in string.punctuation:
        if punctuation != "#":
            text = text.replace(punctuation, ' ')
    return text

base2["message"] = base2['message'].apply(remove_punctuations)
base2["message"] = base2['message'].apply(remover_acentos)
base2['message'] = base2['message'].str.lower()

base2.to_csv('comentariosinfluentes.csv', encoding='UTF-8')

