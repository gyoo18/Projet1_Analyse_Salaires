import LecteurFichier
import AnalyseDonnées
import Graphiques

def main():
    tableauCanada = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Canada.csv","Canada")
    tableauAlberta = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Provinces/Alberta.csv","Alberta")
    tableauColombieBritannique = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Provinces/Colombie-Britannique.csv","Colombie-Britannique")
    tableauIDPE = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Provinces/IDPE.csv","Île-du-Prince-Édouard")
    tableauManitoba = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Provinces/Manitoba.csv","Manitoba")
    tableauNouveauBrunswick = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Provinces/Nouveau_Brunswick.csv","Nouveau-Brunswick")
    tableauNouvelleEcosse = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Provinces/Nouvelle_Ecosse.csv","Nouvelle-Écosse")
    tableauOntario = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Provinces/Ontario.csv","Ontario")
    tableauQuebec = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Provinces/Québec.csv","Québec")
    tableauSaskatchewan = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Provinces/Saskatchewan.csv","Saskatchewan")
    tableauTNetLabrador = LecteurFichier.Lire_Tableau_csv("Données_Stat_Can/Provinces/TN_et_Labrador.csv","Terre-Neuve-et-Labrador")

    tableaux = [tableauCanada, tableauAlberta, tableauColombieBritannique, tableauIDPE, tableauManitoba, tableauNouveauBrunswick, tableauNouvelleEcosse, tableauOntario, tableauQuebec, tableauSaskatchewan, tableauTNetLabrador]

    tableauGouvernement = LecteurFichier.Lire_Tableau_csv("Données_Autre/Gouvernement_Type.csv","Gouvernements")

    résultats = AnalyseDonnées.écart_types_tableaux(tableaux)
    Graphiques.ajouter_graphiques_écart_types(résultats)
    résultats = AnalyseDonnées.moyenne_médiane_tableaux(tableaux)
    Graphiques.ajouter_graphiques_moyenne(résultats)
    Graphiques.ajouter_graphiques_médiane(résultats)
    Graphiques.ajouter_graphiques_différence_moyenne_médiane(résultats)
    résultats = AnalyseDonnées.moyenne_médiane_dérivée(résultats)
    Graphiques.ajouter_dérivée_moyenne(résultats)
    Graphiques.ajouter_dérivée_médiane(résultats)
    Graphiques.ajouter_dérivée_différence_moyenne_médiane(résultats)

    résultats = AnalyseDonnées.corrélation_gouvernement_moyenne(résultats[0],tableauGouvernement,False)
    Graphiques.ajouter_corrélation_gouvernement(résultats)

    résultats = AnalyseDonnées.indice_GINI_tableaux(tableaux)
    Graphiques.ajouter_graphique_GINI(résultats)
    résultats = AnalyseDonnées.indice_GINI_dérivé(résultats)
    Graphiques.ajouter_dérivée_GINI(résultats)

    résultats = AnalyseDonnées.corrélation_gouvernement_moyenne(résultats[0],tableauGouvernement,True)
    Graphiques.ajouter_corrélation_gouvernement(résultats)

    Graphiques.dessiner_graphiques()


if __name__ == "__main__":
    main()