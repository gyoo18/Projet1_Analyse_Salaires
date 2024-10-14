import LecteurFichier
import AnalyseDonnées
import Graphiques
import pandas as pd

def main():
    tableau = LecteurFichier.Lire_Tableau_csv("archive/StudentPerformanceFactors.csv",nom="Éléments de performance")
    #tableau = pd.read_csv('archive/StudentPerformanceFactors.csv')

    for i in range(len(tableau.df.columns)-1):
        résultats = AnalyseDonnées.extraire_colonne_étudiants(i,tableau)
        AnalyseDonnées.nettoyer_données(résultats,AnalyseDonnées.Méthode_Nettoyage.IGNORER)
        if i in [2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18]:
            résultats = AnalyseDonnées.transformer_en_histogramme(résultats,AnalyseDonnées.Méthode_Transformation_Histogramme.MOYENNE)
            Graphiques.ajouter_diagramme_à_bandes(résultats)
        else:
            Graphiques.ajouter_nuage_point(résultats)
    print("Affichage des graphiques")
    Graphiques.dessiner_graphiques()

if __name__ == "__main__":
    main()