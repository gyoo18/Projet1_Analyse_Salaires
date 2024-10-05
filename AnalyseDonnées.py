import LecteurFichier
from Tableau import Tableau
import math

def analyser_tableaux(tableaux : list[Tableau]):
    tableauCanada = tableaux[0]

    for t in tableaux:
        t.retirerLigneInt(16)
        t.retirerLigneInt(15)
        t.retirerLigneInt(14)
        t.retirerLigneInt(4)
        t.retirerLigneInt(2)
        t.retirerLigneInt(1)
        t.retirerLigneInt(0)

    for x in range(len(tableauCanada.valeurs)-1):
        for y in range(len(tableauCanada.valeurs[x])):
            if tableauCanada.valeurs[x+1][y] == "E":
                tableauCanada.valeurs[x][y] = 0
            if tableauCanada.valeurs[x][y] == "":
                tableauCanada.valeurs[x][y] = 0

    lenOrigniale = len(tableauCanada.colonnes)
    for i in range(lenOrigniale):
        if not tableauCanada.colonnes[lenOrigniale - i - 1].isdigit():
            tableauCanada.retirerColonneInt(lenOrigniale - i - 1)

    écart_types = []
    années = []
    for i in range(len(tableauCanada.valeurs)):
        moyenneQuad = 0.0
        for j in range(len(tableauCanada.valeurs[i])):
            moyenneQuad += tableauCanada.valeurs[i][j]**2

        moyenneQuad /= len(tableauCanada.valeurs[i])
        moyenneQuad = math.sqrt(moyenneQuad)
        écart_types.append(moyenneQuad)
        années.append(tableauCanada.colonnes[i])

