import LecteurFichier
import math

tableau = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Canada.csv","Canada")

tableau.retirerLigneInt(16)
tableau.retirerLigneInt(15)
tableau.retirerLigneInt(14)
tableau.retirerLigneInt(4)
tableau.retirerLigneInt(2)
tableau.retirerLigneInt(1)
tableau.retirerLigneInt(0)

for x in range(len(tableau.valeurs)-1):
    for y in range(len(tableau.valeurs[x])):
        if tableau.valeurs[x+1][y] == "E":
            tableau.valeurs[x][y] = 0
        if tableau.valeurs[x][y] == "":
            tableau.valeurs[x][y] = 0

lenOrigniale = len(tableau.colonnes)
for i in range(lenOrigniale):
    if not tableau.colonnes[lenOrigniale - i - 1].isdigit():
        tableau.retirerColonneInt(lenOrigniale - i - 1)

écart_types = []
années = []
for i in range(len(tableau.valeurs)):
    moyenneQuad = 0.0
    for j in range(len(tableau.valeurs[i])):
        moyenneQuad += tableau.valeurs[i][j]**2

    moyenneQuad /= len(tableau.valeurs[i])
    moyenneQuad = math.sqrt(moyenneQuad)
    écart_types.append(moyenneQuad)
    années.append(tableau.colonnes[i])

