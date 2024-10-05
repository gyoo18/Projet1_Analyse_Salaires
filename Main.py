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

    résultats = AnalyseDonnées.écart_types_tableaux(tableaux)
    Graphiques.ajouter_graphiques_écart_types(résultats)
    résultats = AnalyseDonnées.analyser_tableaux2(tableaux)
    Graphiques.ajouter_graphiques_moyenne(résultats)
    Graphiques.ajouter_graphiques_médiane(résultats)
    Graphiques.dessiner_graphiques()


if __name__ == "__main__":
    main()