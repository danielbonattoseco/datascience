# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:27:06 2020

@author: danie
"""


import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

dados2020 = pd.read_csv('consulta_cand_2020_RJ.csv', encoding='latin-1', delimiter=';', error_bad_lines=False).dropna(subset=['NM_URNA_CANDIDATO']).sort_values(by=['NM_URNA_CANDIDATO'], ascending=True)
dados2016 = pd.read_csv('consulta_cand_2016_RJ.csv', encoding='latin-1', delimiter=';', error_bad_lines=False).dropna(subset=['NM_URNA_CANDIDATO']).sort_values(by=['NM_URNA_CANDIDATO'], ascending=True)
dados2012 = pd.read_csv('consulta_cand_2012_RJ.txt', header=None, encoding='latin-1', delimiter=';', error_bad_lines=False).dropna(subset=[14]).sort_values(by=[14], ascending=True)
dados2008 = pd.read_csv('consulta_cand_2008_RJ.txt', header=None, encoding='latin-1', delimiter=';', error_bad_lines=False).dropna(subset=[14]).sort_values(by=[14], ascending=True)
dados2004 = pd.read_csv('consulta_cand_2004_RJ.txt', header=None, encoding='latin-1', delimiter=';', error_bad_lines=False).dropna(subset=[14]).sort_values(by=[14], ascending=True)
dados2000 = pd.read_csv('consulta_cand_2000_RJ.txt', header=None, encoding='latin-1', delimiter=';', error_bad_lines=False).dropna(subset=[14]).sort_values(by=[14], ascending=True)

def plottotal():
    cor = input('Cor: ').lower()
    categoria = input('Categoria: ')
    termo = input('Termo: ').upper()
    tipo = input('Contains = 1\nStartswith = 2 :')
    cat = []
    lista = []

    if tipo == '1':
        cat.append([2000, round((dados2000[dados2000[14].str.contains(termo)].shape[0] / dados2000.shape[0])*100,3), dados2000[dados2000[14].str.contains(termo)].shape[0]])    
        cat.append([2004, round((dados2004[dados2004[14].str.contains(termo)].shape[0] / dados2004.shape[0])*100,3), dados2004[dados2004[14].str.contains(termo)].shape[0]])
        cat.append([2008, round((dados2008[dados2008[14].str.contains(termo)].shape[0] / dados2008.shape[0])*100,3), dados2008[dados2008[14].str.contains(termo)].shape[0]])
        cat.append([2012, round((dados2012[dados2012[14].str.contains(termo)].shape[0] / dados2012.shape[0])*100,3), dados2012[dados2012[14].str.contains(termo)].shape[0]])
        cat.append([2016, round((dados2016[dados2016['NM_URNA_CANDIDATO'].str.contains(termo)].shape[0] / dados2016.shape[0])*100,3), dados2016[dados2016['NM_URNA_CANDIDATO'].str.contains(termo)].shape[0]])
        cat.append([2020, round((dados2020[dados2020['NM_URNA_CANDIDATO'].str.contains(termo)].shape[0] / dados2020.shape[0])*100,3), dados2020[dados2020['NM_URNA_CANDIDATO'].str.contains(termo)].shape[0]])
        lista.append(dados2000[14][dados2000[14].str.contains(termo)])
        lista.append(dados2004[14][dados2004[14].str.contains(termo)])
        lista.append(dados2008[14][dados2008[14].str.contains(termo)])
        lista.append(dados2012[14][dados2012[14].str.contains(termo)])
        lista.append(dados2016['NM_URNA_CANDIDATO'][dados2016['NM_URNA_CANDIDATO'].str.contains(termo)])
        lista.append(dados2020['NM_URNA_CANDIDATO'][dados2020['NM_URNA_CANDIDATO'].str.contains(termo)])
    elif tipo == '2':
        cat.append([2000, round((dados2000[dados2000[14].str.startswith(termo)].shape[0] / dados2000.shape[0])*100,3), dados2000[dados2000[14].str.startswith(termo)].shape[0]])    
        cat.append([2004, round((dados2004[dados2004[14].str.startswith(termo)].shape[0] / dados2004.shape[0])*100,3), dados2004[dados2004[14].str.startswith(termo)].shape[0]])
        cat.append([2008, round((dados2008[dados2008[14].str.startswith(termo)].shape[0] / dados2008.shape[0])*100,3), dados2008[dados2008[14].str.startswith(termo)].shape[0]])
        cat.append([2012, round((dados2012[dados2012[14].str.startswith(termo)].shape[0] / dados2012.shape[0])*100,3), dados2012[dados2012[14].str.startswith(termo)].shape[0]])
        cat.append([2016, round((dados2016[dados2016['NM_URNA_CANDIDATO'].str.startswith(termo)].shape[0] / dados2016.shape[0])*100,3), dados2016[dados2016['NM_URNA_CANDIDATO'].str.startswith(termo)].shape[0]])
        cat.append([2020, round((dados2020[dados2020['NM_URNA_CANDIDATO'].str.startswith(termo)].shape[0] / dados2020.shape[0])*100,3), dados2020[dados2020['NM_URNA_CANDIDATO'].str.startswith(termo)].shape[0]])
        lista.append(dados2000[14][dados2000[14].str.startswith(termo)])
        lista.append(dados2004[14][dados2004[14].str.startswith(termo)])
        lista.append(dados2008[14][dados2008[14].str.startswith(termo)])
        lista.append(dados2012[14][dados2012[14].str.startswith(termo)])
        lista.append(dados2016['NM_URNA_CANDIDATO'][dados2016['NM_URNA_CANDIDATO'].str.startswith(termo)])
        lista.append(dados2020['NM_URNA_CANDIDATO'][dados2020['NM_URNA_CANDIDATO'].str.startswith(termo)])
    else:
        print('Vacilao')  
    
    while True:
        opcao = input('Acionar outro termo? S/N: ').lower()
        if opcao == 's':
            termo = input('Termo: ').upper()
            tipo = input('Contains = 1\nStartswith = 2 :').lower()
            if tipo == '1':
                cat[0][1] = cat[0][1] + (round((dados2000[dados2000[14].str.contains(termo)].shape[0] / dados2000.shape[0])*100,3))
                cat[1][1] = cat[1][1] + (round((dados2004[dados2004[14].str.contains(termo)].shape[0] / dados2004.shape[0])*100,3))
                cat[2][1] = cat[2][1] + (round((dados2008[dados2008[14].str.contains(termo)].shape[0] / dados2008.shape[0])*100,3))
                cat[3][1] = cat[3][1] + (round((dados2012[dados2012[14].str.contains(termo)].shape[0] / dados2012.shape[0])*100,3))
                cat[4][1] = cat[4][1] + (round((dados2016[dados2016['NM_URNA_CANDIDATO'].str.contains(termo)].shape[0] / dados2016.shape[0])*100,3))
                cat[5][1] = cat[5][1] + (round((dados2020[dados2020['NM_URNA_CANDIDATO'].str.contains(termo)].shape[0] / dados2020.shape[0])*100,3))
                cat[0][2] = cat[0][2] + dados2000[dados2000[14].str.contains(termo, case=False)].shape[0]
                cat[1][2] = cat[1][2] + dados2004[dados2004[14].str.contains(termo, case=False)].shape[0]
                cat[2][2] = cat[2][2] + dados2008[dados2008[14].str.contains(termo, case=False)].shape[0]
                cat[3][2] = cat[3][2] + dados2012[dados2012[14].str.contains(termo, case=False)].shape[0]
                cat[4][2] = cat[4][2] + dados2016[dados2016['NM_URNA_CANDIDATO'].str.contains(termo, case=False)].shape[0]
                cat[5][2] = cat[5][2] + dados2020[dados2020['NM_URNA_CANDIDATO'].str.contains(termo, case=False)].shape[0]
                
                lista[0] = lista[0].append(dados2000[14][dados2000[14].str.contains(termo)])
                lista[1] = lista[1].append(dados2004[14][dados2004[14].str.contains(termo)])
                lista[2] = lista[2].append(dados2008[14][dados2008[14].str.contains(termo)])
                lista[3] = lista[3].append(dados2012[14][dados2012[14].str.contains(termo)])
                lista[4] = lista[4].append(dados2016['NM_URNA_CANDIDATO'][dados2016['NM_URNA_CANDIDATO'].str.contains(termo)])
                lista[5] = lista[5].append(dados2020['NM_URNA_CANDIDATO'][dados2020['NM_URNA_CANDIDATO'].str.contains(termo)])
                
            elif tipo == '2':
                cat[0][1] = cat[0][1] + (round((dados2000[dados2000[14].str.startswith(termo)].shape[0] / dados2000.shape[0])*100,3))
                cat[1][1] = cat[1][1] + (round((dados2004[dados2004[14].str.startswith(termo)].shape[0] / dados2004.shape[0])*100,3))
                cat[2][1] = cat[2][1] + (round((dados2008[dados2008[14].str.startswith(termo)].shape[0] / dados2008.shape[0])*100,3))
                cat[3][1] = cat[3][1] + (round((dados2012[dados2012[14].str.startswith(termo)].shape[0] / dados2012.shape[0])*100,3))
                cat[4][1] = cat[4][1] + (round((dados2016[dados2016['NM_URNA_CANDIDATO'].str.startswith(termo)].shape[0] / dados2016.shape[0])*100,3))
                cat[5][1] = cat[5][1] + (round((dados2020[dados2020['NM_URNA_CANDIDATO'].str.startswith(termo)].shape[0] / dados2020.shape[0])*100,3))
                cat[0][2] = cat[0][2] + dados2000[dados2000[14].str.startswith(termo)].shape[0]
                cat[1][2] = cat[1][2] + dados2004[dados2004[14].str.startswith(termo)].shape[0]
                cat[2][2] = cat[2][2] + dados2008[dados2008[14].str.startswith(termo)].shape[0]
                cat[3][2] = cat[3][2] + dados2012[dados2012[14].str.startswith(termo)].shape[0]
                cat[4][2] = cat[4][2] + dados2016[dados2016['NM_URNA_CANDIDATO'].str.startswith(termo)].shape[0]
                cat[5][2] = cat[5][2] + dados2020[dados2020['NM_URNA_CANDIDATO'].str.startswith(termo)].shape[0]
                lista[0] = lista[0].append(dados2000[14][dados2000[14].str.startswith(termo)])
                lista[1] = lista[1].append(dados2004[14][dados2004[14].str.startswith(termo)])
                lista[2] = lista[2].append(dados2008[14][dados2008[14].str.startswith(termo)])
                lista[3] = lista[3].append(dados2012[14][dados2012[14].str.startswith(termo)])
                lista[4] = lista[4].append(dados2016['NM_URNA_CANDIDATO'][dados2016['NM_URNA_CANDIDATO'].str.startswith(termo)])
                lista[5] = lista[5].append(dados2020['NM_URNA_CANDIDATO'][dados2020['NM_URNA_CANDIDATO'].str.startswith(termo)])
            
            else:
                print('Vacilao')  
        elif opcao == 'n':
            break
        else:
            print('Vacilao')  
            
    x = []
    y = []
    
    for i in range(len(cat)):
        x.append(cat[i][0])
        
    for i in range(len(cat)):
        y.append(cat[i][1])

    fig, ax = plt.subplots()

    bar_plot = plt.bar(x,y, color=cor)
    
    for idx,rect in enumerate(bar_plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
            str(round(cat[idx][1],2)) + '%',
            ha='center', va='bottom', size=6)
    
    plt.tight_layout()        
    plt.xticks(x)
    plt.yticks([0.5, 1, 1.5, 2, 2.5])    
    plt.title('Proporcional de candidaturas com termos da categoria\n"' + categoria + '"\nno nome de urna no estado do RJ', fontweight="bold")
    plt.xlabel('Ano de eleição', fontweight="bold")
    plt.ylabel('% do total de candidaturas', fontweight="bold")
    plt.savefig(fname='./GraficosFINAL/' + categoria + 'proporcional.png', dpi=300)
    
    
    x = []
    y = []
    
    for i in range(len(cat)):
        x.append(cat[i][0])
        
    for i in range(len(cat)):
        y.append(cat[i][2])

    fig, ax = plt.subplots()

    bar_plot = plt.bar(x,y, color=cor)
    
    for idx,rect in enumerate(bar_plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
            cat[idx][2],
            ha='center', va='bottom', size=6)
    
    plt.tight_layout()        
    plt.xticks(x)
    plt.title('Candidatos com termos da categoria\n"' + categoria + '"\nno nome de urna no estado do RJ', fontweight="bold")
    plt.xlabel('Ano de eleição', fontweight="bold")
    plt.ylabel('Candidatos', fontweight="bold")
    plt.savefig('./GraficosFINAL/' + categoria + 'total.png', dpi=300)

    return lista

lista = plottotal()
#DB4437
lista2020 = Counter(" ".join(dados2020['NM_URNA_CANDIDATO']).split()).most_common(300)

