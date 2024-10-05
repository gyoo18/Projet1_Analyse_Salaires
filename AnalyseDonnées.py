import LecteurFichier
from Tableau import Tableau
import math

def analyser_tableaux(tableaux : list[Tableau]):
    tableaux_résultats = []

    for t in tableaux:
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


        écart_types = Tableau("écart-types")
        écart_types.ajouterColonne("valeurs")
        moyennes = []
        for i in range(len(t.valeurs)):
            moyenne = 0.0
            for j in range(len(t.valeurs[i])):
                moyenne += t.valeurs[i][j]
            moyenne /= len(t.valeurs[i])
            moyennes.append(moyenne)

        for i in range(len(t.valeurs)):
            moyenneQuad = 0.0
            for j in range(len(t.valeurs[i])):
                moyenneQuad += (moyennes[i] - t.valeurs[i][j]) ** 2
            moyenneQuad /= len(t.valeurs[i])
            moyenneQuad = math.sqrt(moyenneQuad)
            écart_types.ajouterLigne(t.colonnes[i])
            écart_types.valeurs[0][len(écart_types.lignes)-1] = moyenneQuad
        
        tableaux_résultats.append(écart_types)

    return tableaux_résultats