# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 20:23:06 2023

@author: Utilisateur
"""

import matplotlib.pyplot as plt
import numpy as np
from df_loading import datasets as dts

def Répartition_flms_sans_notes(table):
    # les données à afficher dans le camembert
    labels = ['Sans notes', 'Notés'] 
    data = table['cpt']
    
    # configuration des couleurs de chaque tranche
    colors = ['#beaed4','#7fc97f']
    
    # création du camembert avec les données
    plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    
    # Ajout d'un titre
    plt.title("Répartition des flms sans notes")
    
    # Affichage du camembert
    plt.show()
    
def Répartition_notes_2_films(table):

    # Les données à afficher dans le graphique en barres
    occurance = table['occurance']
    averageRating = table['averageRating'].astype(int)
    prc = table['prc']
    
    # Création de la figure et des axes
    fig, ax = plt.subplots()
    
    # Configuration de l'espacement entre les barres et leur largeur
    bar_width = 0.9
    bar_spacing = 0.1
    
    # Génération des positions de départ de chaque groupe de barres
    bar_positions = np.arange(len(occurance))
    
    # Affichage des barres
    ax.bar(bar_positions, prc, width=bar_width, color='blue', alpha=0.7)
    
    # Ajout des étiquettes d'axe et de titre
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(averageRating, rotation=90)
    ax.set_ylabel('%')
    ax.set_title('Répartition des notes')
    
    # Affichage du graphique
    plt.show()
    
def Répartition_items_par_types(table, red_color=False):

    # Les données à afficher dans le graphique en barres
    occurance = table['occurance']
    titleType = table['titleType']
    prc = table['prc']
    
    #construction du vecteur couleur
    if red_color :
        colors = np.where(np.array(table['titleType']) == 'movie', 'red', 'blue')
    else:
        colors = np.full(dts['analyses']['types'].shape[0],'blue')
    
    # Création de la figure et des axes
    fig, ax = plt.subplots()
    
    # Configuration de l'espacement entre les barres et leur largeur
    bar_width = 0.5
    bar_spacing = 0.1
    
    # Génération des positions de départ de chaque groupe de barres
    bar_positions = np.arange(len(occurance))
    
    # Affichage des barres
    ax.bar(bar_positions, prc, width=bar_width, color=colors, alpha=0.7)
    
    # Ajout des étiquettes d'axe et de titre
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(titleType, rotation=90)
    ax.set_ylabel('Millions')
    ax.set_title("épartition des types d'items")
    
    # Affichage du graphique
    plt.show()
  
def Correspondance_Notes_Nombre_Votes_Decennies(table):
    
    annee = table['annee']
    avg_rating = table['avg_rating']
    avg_num_votes = table['avg_num_votes']
    
    # Création du plot
    fig, ax = plt.subplots()
    sc = ax.scatter(avg_rating, avg_num_votes, c=annee, cmap='viridis')
    ax.set_xlabel('Note moyenne sur tous les films')
    ax.set_ylabel('Nombre de votes moyens sur tous les films')
    fig.colorbar(sc, label='annee')
    
    # Ajout des labels
    for i, txt in enumerate(annee):
        ax.annotate(txt, (avg_rating[i], avg_num_votes[i]), textcoords='offset points', xytext=(0, 8), ha='center')
    
    plt.show()
    
def Nombre_films_difusés_par_regions(table):    
    # Création des données
    occurence = table['occurence'][:20]
    region = table['region'][:20]
    
    # Création du graphique
    fig, ax = plt.subplots()
    
    #construction du vecteur couleur 
    colors = np.where(np.array(table['occurence']) > 2000000, 'Green', 'blue')
    colors[7:9] ='Red'
    
    y_pos = np.arange(len(region))
    ax.barh(y_pos, occurence, align='center', color=colors)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(region)
    ax.invert_yaxis()  # Inverse l'ordre des éléments sur l'axe Y
    ax.set_xlabel('Nombre de films')
    ax.set_title('Nombre de films difusés par regions')
    
    plt.show()    
    
def Nombre_films_produits_par_regions(table):  
    # Création des données
    occurence = table['occurence'][:20]
    region = table['region'][:20]
    
    # Création du graphique
    fig, ax = plt.subplots()
    
    colors = np.full(occurence.shape[0],'blue')
    colors[:2] ='Red'
    
    y_pos = np.arange(len(region))
    ax.barh(y_pos, occurence, align='center', color=colors)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(region)
    ax.invert_yaxis()  # Inverse l'ordre des éléments sur l'axe Y
    ax.set_xlabel('Nombre de films')
    ax.set_title('Nombre de films produits par regions')
    
    plt.show()    
    
def Part_films_produits_par_regions(table):  
    
    labels = ['US-GB', 'Reste du monde'] 
    data = [np.sum( table['occurence'][:2]),np.sum( table['occurence'][2:-1])] 
    
    # configuration des couleurs de chaque tranche
    colors = ['Red','royalblue']
    
    # création du camembert avec les données
    plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    
    # Ajout d'un titre
    plt.title("Part de la production de films")
    
    # Affichage du camembert
    plt.show()
    
def Part_films_difusion_par_regions(table):  
    
    labels = ['DE-JP-FR-IN-ES-IT-PT', 'US-GB', 'Reste du monde'] 
    data = [np.sum( table['occurence'][:7]),np.sum( table['occurence'][7:9]),np.sum( table['occurence'][9:-1])] 
    
    # configuration des couleurs de chaque tranche
    colors = ['Green', 'red','royalblue']
    
    # création du camembert avec les données
    plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    
    # Ajout d'un titre
    plt.title("Part de la diffusion de films")
    
    # Affichage du camembert
    plt.show()
    
    # region1 = table['region'][:2]
    


Nombre_films_produits_par_regions(dts['analyses']['classement_regions_production_films'])    
Nombre_films_difusés_par_regions(dts['analyses']['region_diffusion_films'])  
Correspondance_Notes_Nombre_Votes_Decennies(dts['analyses']['decenie_votes_rating'])
Répartition_notes_2_films(dts['analyses']['notes'])  
Répartition_items_par_types(dts['analyses']['types'])  
Répartition_items_par_types(dts['analyses']['types'][1:-1], True)  
Répartition_flms_sans_notes(dts['analyses']['prop_notes_null'])
Part_films_produits_par_regions(dts['analyses']['classement_regions_production_films'])
Part_films_difusion_par_regions(dts['analyses']['region_diffusion_films'])