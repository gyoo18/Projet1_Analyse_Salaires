import LecteurFichier
import AnalyseDonnées
import Graphiques
import pandas as pd

tableau_qualitatif_en_quantitatif= [
    ("Male",0),
    ("Female",1),

    ("Near",0),
    ("Moderate",1),
    ("Far",2),

    ("High School",0),
    ("College",1),
    ("Postgraduate",2),

    ("No",0),
    ("Yes",1),

    ("Negative",0),
    ("Neutral",1),
    ("Positive",2),

    ("Public",0),
    ("Private",1),

    ("Low",0),
    ("Medium",1),
    ("High",2)     ]

def main():
    tableau = LecteurFichier.Lire_Tableau_csv("archive/StudentPerformanceFactors.csv",nom="Éléments de performance")

    print("Calcul de la carte de corrélation")
    Graphiques.ajouter_carte_corrélations(
        AnalyseDonnées.générer_carte_corrélation(
            AnalyseDonnées.transformer_qualitatif_en_quantitatif(tableau,tableau_qualitatif_en_quantitatif)
        )
    )

    print("Calcul des autres graphiques")
    for i in range(len(tableau.df.columns)-1):
        résultats = AnalyseDonnées.extraire_colonne_étudiants(i,tableau)
        AnalyseDonnées.nettoyer_données(résultats,AnalyseDonnées.Méthode_Nettoyage.IGNORER)
        if i in [2,3,4,7,8,10,11,12,13,15,16,17,18]:
            Graphiques.ajouter_boîtes_à_moustaches(résultats)
            résultats2 = AnalyseDonnées.transformer_en_histogramme(résultats,AnalyseDonnées.Méthode_Transformation_Histogramme.MOYENNE)
            #Graphiques.ajouter_diagramme_à_bandes(résultats2)
            #Graphiques.ajouter_diagramme_à_bandes_et_moustaches(résultats2,résultats)
        else:
            AnalyseDonnées.régression_linéaire(résultats)
            Graphiques.ajouter_nuage_point(résultats)
    print("Affichage des graphiques")
    Graphiques.dessiner_graphiques()

if __name__ == "__main__":
    main()