import LecteurFichier
from Tableau import Tableau
import copy
import math

#Calculer l'écart-type des revenus par année
def écart_types_tableaux(tableaux : list[Tableau]):
    tableaux_résultats = []
    lignes_revenus_moyen = [5000,15000,25000,35000,45000,55000,65000,75000,90000,110000] # Revenu moyen pour chaque catégorie de revenus

    for tab in tableaux:
        t = copy.deepcopy(tab) # Faire une copie profonde pour faciliter la manipulation sans affecter les autres instances.
        # Retirer toutes les lignes qui ne contiennent pas les pourcentage de la population dans chaque catégorie de revenus ou le revenus moyen.
        t.retirerLigneInt(16)
        #t.retirerLigneInt(15)
        t.retirerLigneInt(14)
        t.retirerLigneInt(4)
        t.retirerLigneInt(2)
        t.retirerLigneInt(1)
        t.retirerLigneInt(0)
        
        for x in range(len(t.valeurs)-1):
            for y in range(len(t.valeurs[x])):
                if t.valeurs[x+1][y] == "E":
                    # Retirer toutes les valeurs jugées "À manipuler avec précaution"
                    t.valeurs[x][y] = 0
                if t.valeurs[x][y] == "":
                    # Transformer les cases vides en 0
                    t.valeurs[x][y] = 0

        # Retirer les colonnes contenant les annotations des données pour ne conserver que les données
        lenOrigniale = len(t.colonnes)
        for i in range(lenOrigniale):
            if not t.colonnes[lenOrigniale - i - 1].isdigit():
                t.retirerColonneInt(lenOrigniale - i - 1)

        # Calculer l'écart-type
        écart_types = Tableau(t.nom)    # Tableau contenant les résultats
        écart_types.ajouterColonne("valeurs")
        # Calculer l'écart-type
        for i in range(len(t.valeurs)):
            moyenneQuad = 0.0
            for j in range(len(t.valeurs[i])-1):
                moyenneQuad += (t.valeurs[i][10] - lignes_revenus_moyen[j])**2 * t.valeurs[i][j]
            moyenneQuad = math.sqrt(moyenneQuad)
            écart_types.ajouterLigne(t.colonnes[i])
            écart_types.valeurs[0][len(écart_types.lignes)-1] = moyenneQuad
        
        del t
        tableaux_résultats.append(écart_types)

    return tableaux_résultats


def moyenne_médiane_tableaux(tableaux: list[Tableau]):
    
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

def moyenne_médiane_dérivée(tableaux: list[Tableau]):
    
    tableaux_résultats = copy.deepcopy(tableaux)
    for t in range(len(tableaux_résultats)):
        for i in range(len(tableaux_résultats[t].colonnes)):
            for j in range(len(tableaux_résultats[t].lignes)):
                tableaux_résultats[t].valeurs[i][j] = tableaux[t].valeurs[i][j]-tableaux[t].valeurs[max(i-1,0)][j]

    return tableaux_résultats

def indice_GINI_tableaux(tableaux : list[Tableau]):

    tableaux_résultats = []
    lignes_revenus_moyen = [5000,15000,25000,35000,45000,55000,65000,75000,90000,110000]
    for tab in tableaux:
        t = copy.deepcopy(tab)

        for x in range(len(t.valeurs)-1):
            for y in range(len(t.valeurs[x])):
                if t.valeurs[x+1][y] == "E":
                    # Retirer toutes les valeurs jugées "À manipuler avec précaution"
                    t.valeurs[x][y] = 0
                if t.valeurs[x][y] == "":
                    # Transformer les cases vides en 0
                    t.valeurs[x][y] = 0
        
         # Retirer les colonnes contenant les annotations des données pour ne conserver que les données
        lenOrigniale = len(t.colonnes)
        for i in range(lenOrigniale):
            if not t.colonnes[lenOrigniale - i - 1].isdigit():
                t.retirerColonneInt(lenOrigniale - i - 1)

        lenLignesOriginal = len(t.lignes)
        for i in range(lenLignesOriginal):
            if i in [16-0, 16-1, 16-2, 16-4, 16-14, 16-16]:
                t.retirerLigneInt(lenLignesOriginal - i - 1)
        
        tableau_gini = Tableau(t.nom)
        tableau_gini.ajouterColonne("coefficients")
        for i in range(len(t.colonnes)):
            E = 0
            for j in range(len(t.lignes)-1):
                for l in range(len(t.lignes)-1):
                    E += ( t.valeurs[i][j]/100 )*( t.valeurs[i][l]/100 )*abs(lignes_revenus_moyen[j] - lignes_revenus_moyen[l])
            tableau_gini.valeurs[0].append( E/(2*t.valeurs[i][10]) )
            tableau_gini.lignes.append(t.colonnes[i])
        
        tableaux_résultats.append(tableau_gini)
    return tableaux_résultats

def indice_GINI_dérivé(tableaux : list[Tableau]):
    tableaux_résultats = copy.deepcopy(tableaux)

    for t in range(len(tableaux_résultats)):
        for i in range(len(tableaux_résultats[t].colonnes)):
            for j in range(len(tableaux_résultats[t].lignes)):
                tableaux_résultats[t].valeurs[i][j] = tableaux[t].valeurs[i][j] - tableaux[t].valeurs[i][max(j-1,0)]
    return tableaux_résultats

def corrélation_gouvernement_moyenne(données_canada : Tableau, gouvernement : Tableau, vertical : bool):
    tableau_résultat = Tableau("Corrélation " + données_canada.nom + " et le type de gouvernement")
    tableau_résultat.ajouterColonne("Libéraux")
    tableau_résultat.ajouterColonne("Conservateurs")
    types_données = len(données_canada.colonnes) if vertical else len(données_canada.lignes)
    for i in range(types_données):
        tableau_résultat.ajouterLigne(données_canada.colonnes[i] if vertical else données_canada.lignes[i])
        moyenne_libérale = 0
        n_L = 0
        moyenne_conservatrice = 0
        n_C = 0
        for j in range(len(gouvernement.lignes)):
            if gouvernement.valeurs[0][j] == "L":
                moyenne_libérale += données_canada.valeurs[i][j] if vertical else données_canada.valeurs[j][i]
                n_L += 1
            elif gouvernement.valeurs[0][j] == "C":
                moyenne_conservatrice += données_canada.valeurs[i][j] if vertical else données_canada.valeurs[j][i]
                n_C += 1
        tableau_résultat.valeurs[0][i] = moyenne_libérale/n_L
        tableau_résultat.valeurs[1][i] = moyenne_conservatrice/n_C

    return tableau_résultat

def corrélation_colonne_x_étudiants(i_colonne : int, tableau : Tableau):
    print("Extraction de la colonne", i_colonne, tableau.colonnes[i_colonne])
    tableau_résultat = copy.deepcopy(tableau)
    tableau_résultat.nom = "notes en fonction de " + tableau_résultat.colonnes[i_colonne]
    n_colonnes = len(tableau_résultat.colonnes)-1
    for i in range(len(tableau_résultat.colonnes)-1):
        if n_colonnes - i - 1 != i_colonne:
            tableau_résultat.retirerColonneInt(n_colonnes - i - 1)
    
    tableau_résultat.lignes = tableau_résultat.valeurs[0]
    tableau_résultat.valeurs[0] = tableau_résultat.valeurs[1]
    tableau_résultat.retirerColonneInt(1)
    
    return tableau_résultat