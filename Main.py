import LecteurFichier
import AnalyseDonnées
import Graphiques

def main():
    tableau = LecteurFichier.Lire_Tableau_csv("archive/StudentPerformanceFactors.csv",nom="Éléments de performance", séparateur=",", nom_de_lignes=False)

    for i in range(len(tableau.colonnes)-1):
        résultats = AnalyseDonnées.corrélation_colonne_x_étudiants(i,tableau)
        AnalyseDonnées.nettoyer_données(résultats,AnalyseDonnées.Méthode_Nettoyage.IGNORER)
        if i in [2,3,4,7,8,10,11,12,13,14,15,16,17,18]:
            AnalyseDonnées.transformer_en_histogramme(résultats,AnalyseDonnées.Méthode_Transformation_Histogramme.MOYENNE)
            Graphiques.ajouter_histogramme(résultats)
        else:
            Graphiques.ajouter_nuage_point(résultats)
    print("Affichage des graphiques")
    Graphiques.dessiner_graphiques()

if __name__ == "__main__":
    main()