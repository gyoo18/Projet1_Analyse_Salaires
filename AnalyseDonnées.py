import LecteurFichier
import math

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

for t in tableaux:

    t.retirerLigneInt(16)
    t.retirerLigneInt(15)
    t.retirerLigneInt(14)
    t.retirerLigneInt(4)
    t.retirerLigneInt(2)
    t.retirerLigneInt(1)
    t.retirerLigneInt(0)

    for x in range(len(t.valeurs)-1):
        for y in range(len(t.valeurs[x])):
            if t.valeurs[x+1][y] == "E":
                t.valeurs[x][y] = 0
            if t.valeurs[x][y] == "":
                t.valeurs[x][y] = 0

    lenOrigniale = len(t.colonnes)
    for i in range(lenOrigniale):
        if not t.colonnes[lenOrigniale - i - 1].isdigit():
            t.retirerColonneInt(lenOrigniale - i - 1)

# écart_types = []
# années = []
# for i in range(len(tableau.valeurs)):
#     moyenneQuad = 0.0
#     for j in range(len(tableau.valeurs[i])):
#         moyenneQuad += tableau.valeurs[i][j]**2
#
#     moyenneQuad /= len(tableau.valeurs[i])
#     moyenneQuad = math.sqrt(moyenneQuad)
#     écart_types.append(moyenneQuad)
#     années.append(tableau.colonnes[i])

