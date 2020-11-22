# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:19:47 2020

@author: danie
"""


import pandas as pd
import matplotlib.pyplot as plt

curtir = pd.read_csv('Curtir/analisesentimentos.csv', delimiter=",")
amei = pd.read_csv('Amei/analisesentimentos.csv', delimiter=",")
uau = pd.read_csv('Uau/analisesentimentos.csv', delimiter=",")
grr = pd.read_csv('Grr/analisesentimentos.csv', delimiter=",")
triste = pd.read_csv('Triste/analisesentimentos.csv', delimiter=",")
haha = pd.read_csv('Haha/analisesentimentos.csv', delimiter=",")

def calcular_sentimento(text):
    if text < 0.3:
        return 'Negativo'
    elif text > 0.7:
        return 'Positivo'
    else:
        return 'Neutro'

curtir['situacao'] = curtir['resultado'].apply(calcular_sentimento)
amei['situacao'] = amei['resultado'].apply(calcular_sentimento)
uau['situacao'] = uau['resultado'].apply(calcular_sentimento)
grr['situacao'] = grr['resultado'].apply(calcular_sentimento)
triste['situacao'] = triste['resultado'].apply(calcular_sentimento)
haha['situacao'] = haha['resultado'].apply(calcular_sentimento)

curtir['cat_id'] = 1
amei['cat_id'] = 2
haha['cat_id'] = 3
uau['cat_id'] = 4
triste['cat_id'] = 5
grr['cat_id'] = 6

curtir['cat_nome'] = 'Curtir'
amei['cat_nome'] = 'Amei'
haha['cat_nome'] = 'Haha'
uau['cat_nome'] = 'Uau'
triste['cat_nome'] = 'Triste'
grr['cat_nome'] = 'Grr'

dadosunidos = pd.DataFrame(curtir)
dadosunidos = dadosunidos.append(amei)
dadosunidos = dadosunidos.append(haha)
dadosunidos = dadosunidos.append(uau)
dadosunidos = dadosunidos.append(triste)
dadosunidos = dadosunidos.append(grr)

dadosunidos.to_csv('analisesentimentos.csv')
      
haha['situacao'].value_counts().plot(kind = 'barh')
amei['situacao'].value_counts().plot(kind = 'barh')
