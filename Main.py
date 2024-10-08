import LecteurFichier
import AnalyseDonnées
import Graphiques

def main():
    tableau = LecteurFichier.Lire_Tableau_csv("archive/StudentPerformanceFactors.csv",nom="Éléments de performance", séparateur=",", nom_de_lignes=False)

    for i in range(len(tableau.colonnes)-1):
        Graphiques.ajouter_nuage_point(AnalyseDonnées.corrélation_colonne_x_étudiants(i,tableau))
    print("Affichage des graphiques")
    Graphiques.dessiner_graphiques()

if __name__ == "__main__":
    main()