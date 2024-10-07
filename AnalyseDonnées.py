import LecteurFichier
from Tableau import Tableau
import copy
import math

def écart_types_tableaux(tableaux : list[Tableau]):
    tableaux_résultats = []
    lignes_revenus_moyen = [5000,15000,25000,35000,45000,55000,65000,75000,90000,1000000]

    for tab in tableaux:
        t = copy.deepcopy(tab)
        t.retirerLigneInt(16)
        t.retirerLigneInt(15)
        t.retirerLigneInt(14)
        t.retirerLigneInt(4)
        t.retirerLigneInt(2)
        t.retirerLigneInt(1)
        t.retirerLigneInt(0)

        for x in range(len(t.valeurs)-1):
            for y in range(len(t.valeurs[x])):
                if t.valeurs[x+1][y] == "E":
                    t.valeurs[x][y] = 0
                if t.valeurs[x][y] == "":
                    t.valeurs[x][y] = 0

        lenOrigniale = len(t.colonnes)
        for i in range(lenOrigniale):
            if not t.colonnes[lenOrigniale - i - 1].isdigit():
                t.retirerColonneInt(lenOrigniale - i - 1)

        écart_types = Tableau(t.nom)
        écart_types.ajouterColonne("valeurs")
        moyennes = []
        for i in range(len(t.valeurs)):
            moyenne = 0.0
            for j in range(len(t.valeurs[i])):
                moyenne += t.valeurs[i][j]*lignes_revenus_moyen[j]
            moyennes.append(moyenne)

        for i in range(len(t.valeurs)):
            moyenneQuad = 0.0
            for j in range(len(t.valeurs[i])):
                moyenneQuad += (moyennes[i] - lignes_revenus_moyen[j])**2 * t.valeurs[i][j]
            moyenneQuad = math.sqrt(moyenneQuad)
            écart_types.ajouterLigne(t.colonnes[i])
            écart_types.valeurs[0][len(écart_types.lignes)-1] = moyenneQuad
        
        tableaux_résultats.append(écart_types)

    return tableaux_résultats


def analyser_tableaux2(tableaux: list[Tableau]):
    
    tableaux_résultats = []
    for tab in tableaux:
        t = copy.deepcopy(tab)
        lenLignesOriginal = len(t.lignes)
        for i in range(lenLignesOriginal):
            if i not in [16-15, 16-16]:
                t.retirerLigneInt(lenLignesOriginal - i - 1)

        for x in range(len(t.valeurs) - 1):
            for y in range(len(t.valeurs[x])):
                if t.valeurs[x][y] == "":
                    t.valeurs[x][y] = 0

        lenOrigniale = len(t.colonnes)
        for i in range(lenOrigniale):
            if not t.colonnes[lenOrigniale - i - 1].isdigit():
                t.retirerColonneInt(lenOrigniale - i - 1)

        t.ajouterLigne("Différence entre la moyenne et la médiane")
        for i in range(len(t.colonnes)):
            t.valeurs[i][2] = t.valeurs[i][0] - t.valeurs[i][1]
        tableaux_résultats.append(t)

    return tableaux_résultats
