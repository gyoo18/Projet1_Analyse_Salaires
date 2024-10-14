#import LecteurFichier
from Tableau import Tableau
import copy
import math
import pandas as pd
from pandas import DataFrame

def extraire_colonne_étudiants(i_colonne : int, tableau : Tableau):
    print("Extraction de la colonne", i_colonne, tableau.df.columns[i_colonne])

    return Tableau(tableau.df.columns[i_colonne],tableau.df.iloc[:,[i_colonne,-1]])

    '''
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
    '''

class Méthode_Nettoyage:
    IGNORER = 0
    INTERPOLATION = 1
    MOYENNE = 2
    MÉDIANE = 3
    MODE = 4

    def __nom_méthode__(méthode : int):
        match méthode:
            case Méthode_Nettoyage.IGNORER:
                return "INGORER"
            case Méthode_Nettoyage.INTERPOLATION:
                return "INTERPOLATION"
            case Méthode_Nettoyage.MOYENNE:
                return "MOYENNE"
            case Méthode_Nettoyage.MÉDIANE:
                return "MÉDIANE"
            case Méthode_Nettoyage.MODE:
                return "MODE"

def nettoyer_données(Données : Tableau, méthode : int):
    print("Nettoyage de",Données.nom,"par la méthode",Méthode_Nettoyage.__nom_méthode__(méthode))

    match méthode:
        case Méthode_Nettoyage.IGNORER:
            Données.df.dropna(axis = 0, inplace= True)
        case Méthode_Nettoyage.INTERPOLATION:
            Données.df.interpolate(method="linear")
        case Méthode_Nettoyage.MOYENNE:
            Données.df.fillna(Données.df.mean(), inplace=True)
        case Méthode_Nettoyage.MÉDIANE:
            Données.df.fillna(Données.df.median(), inplace=True)
        case Méthode_Nettoyage.MODE:
            Données.df.fillna(Données.df.mode(), inplace=True)

    return Données
    
    '''
    moyenne = 0
    mode = 0
    médiane = 0

    if méthode == 2:
        print("calcul de la moyenne")
        for i in range(len(Données.lignes)):
            moyenne += Données.valeurs[0][i]
        moyenne /= len(Données.lignes)

    if méthode == 3:
        print("calcul de la médiane")
        if len(Données.lignes)%2 == 0:
            médiane = ( Données.valeurs[0][ int(len(Données.lignes) / 2) ] + Données.valeurs[0][ int(len(Données.lignes) / 2) + 1 ] ) / 2
        else:
            médiane = Données.valeurs[0][ int(len(Données.lignes) / 2) ]
    
    if méthode == 4:
        print("calcul du mode")
        instance = []
        nombre_apparition = []
        for i in range(len(Données.lignes)):
            if Données.valeurs[0][i] in instance:
                nombre_apparition[ instance.index( Données.valeurs[0][i] ) ] += 1
            else:
                instance.append(Données.valeurs[0][1])
                nombre_apparition.append(1)
        
        objet = 0
        max_aparitions = 0
        for i in range(len(instance)):
            if nombre_apparition[i] > max_aparitions:
                max_aparitions = nombre_apparition[i]
                objet = instance[i]
        
        mode = objet

    print("nettoyage")
    n = len(Données.lignes)-1
    for i in range(len(Données.lignes)):
        à_nettoyer = ( Données.valeurs[0][n-i] == "" or Données.valeurs[0][n-i] == 0 or Données.valeurs[0][n-i] == " "  # Possède un valeur invalide
                      or Données.valeurs[0][n-i] > 100 or Données.valeurs[0][n-i] < 0   # Possède une valeur aberrante
                      or Données.lignes[n-i] == "" or Données.lignes[n-i] == 0 or Données.lignes[n-i] == " ")   # Possède une valeur invalide
        match méthode:
            case Méthode_Nettoyage.IGNORER:
                if à_nettoyer:
                    Données.retirerLigneInt(n-i)
            case Méthode_Nettoyage.INTERPOLER_LINÉAIRE:
                if à_nettoyer:
                    m = ( Données.valeurs[0][n-i-1] - Données.valeurs[0][n-i+1] ) / ( float(Données.lignes[n-i-1]) - float(Données.lignes[n-i+1]) )
                    b = Données.valeurs[0][n-i-1] - ( m*float(Données.lignes[n-i-1]) )
                    Données.valeurs[0][n-i] = float(Données.lignes[n-i])*m + b
            case Méthode_Nettoyage.MOYENNE:
                if à_nettoyer:
                    Données.valeurs[0][n-i] = moyenne
            case Méthode_Nettoyage.MÉDIANE:
                if à_nettoyer:
                    Données.valeurs[0][n-i] = médiane
            case Méthode_Nettoyage.MODE:
                if à_nettoyer:
                    Données.valeurs[0][n-i] = mode

    return Données
    '''

class Méthode_Transformation_Histogramme:
    MOYENNE = 0
    MÉDIANE = 0
    MODE = 0

    def __nom_méthode__(méthode : int):
        match méthode:
            case Méthode_Transformation_Histogramme.MOYENNE:
                return "MOYENNE"
            case Méthode_Transformation_Histogramme.MÉDIANE:
                return "MÉDIANE"

def transformer_en_histogramme(Données : Tableau, méthode : int):
    print("Transformation de",Données.nom,"en histogramme, avec la méthode", Méthode_Transformation_Histogramme.__nom_méthode__(méthode))

    match méthode:
        case Méthode_Transformation_Histogramme.MOYENNE:
            return Tableau(Données.nom,Données.df.groupby([Données.df.columns[0]]).mean())
        case Méthode_Transformation_Histogramme.MÉDIANE:
            return Tableau(Données.nom,Données.df.groupby([Données.df.columns[0]]).median())

    '''
    match méthode:
        case Méthode_Transformation_Histogramme.MOYENNE:
            catégories = list(set(Données.lignes))
            cumul = [0 for i in range(len(catégories))]
            n_catégories = [0 for i in range(len(catégories))]
            min_catégorie = [1000 for i in range(len(catégories))]
            max_catégorie = [0 for i in range(len(catégories))]
            for i in range(len(Données.lignes)):
                cumul[catégories.index(Données.lignes[i])] += Données.valeurs[0][i]
                n_catégories[catégories.index(Données.lignes[i])] += 1
                if Données.valeurs[0][i] < min_catégorie[catégories.index(Données.lignes[i])]:
                    min_catégorie[catégories.index(Données.lignes[i])] = Données.valeurs[0][i]
                if Données.valeurs[0][i] > max_catégorie[catégories.index(Données.lignes[i])]:
                    max_catégorie[catégories.index(Données.lignes[i])] = Données.valeurs[0][i]
            for i in range(len(cumul)):
                cumul[i] /= n_catégories[i]
            Données.lignes = catégories
            Données.valeurs[0] = cumul
            Données.ajouterColonne("min")
            Données.ajouterColonne("max")
            for i in range(len(Données.lignes)):
                Données.valeurs[1][i] = min_catégorie[i]
                Données.valeurs[2][i] = max_catégorie[i]
    '''