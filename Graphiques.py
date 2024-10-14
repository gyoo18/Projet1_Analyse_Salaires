import matplotlib.pyplot as plt
from Tableau import Tableau
import seaborn as sns

catégories_quantitatives_set = [
    {"Male","Female"},
    {"Near","Moderate","Far"},
    {"High School", "College", "Postgraduate"},
    {"No", "Yes"},
    {"Negative", "Neutral", "Positive"},
    {"Public", "Private"},
    {"Low", "Medium", "High"},
]
catégories_quantitatives_list = [
    ["Male","Female"],
    ["Near","Moderate","Far"],
    ["High School", "College", "Postgraduate"],
    ["No", "Yes"],
    ["Negative", "Neutral", "Positive"],
    ["Public", "Private"],
    ["Low", "Medium", "High"],
]

def ajouter_nuage_point(Données : Tableau):
    print("Afficher",Données.nom)
    plt.plot(Données.df[Données.df.columns[0]],Données.df[Données.df.columns[1]],'o')
    plt.title(Données.nom)
    plt.xticks(rotation=45)
    plt.grid()
    plt.figure()

def ajouter_diagramme_à_bandes(Données : Tableau):
    print("Afficher",Données.nom)
    plt.bar(Données.df.index,Données.df[Données.df.columns[0]])
    plt.title(Données.nom)
    plt.xticks(rotation=45)
    plt.gca().set_ylim(ymin = 50)
    plt.grid()
    plt.figure()

def ajouter_boîtes_à_moustaches(Données : Tableau):
    print("Afficher",Données.nom)
    df2 = Données.df
    catégories_set = set(df2[df2.columns[0]])
    catégories = []
    for i in range(len(catégories_quantitatives_set)):
        if catégories_set == catégories_quantitatives_set[i]:
            catégories = catégories_quantitatives_list[i]
    else:
        catégories = list(catégories_set)

    plots = []
    positions = []
    for i in range(len(catégories)):
        plots.append(df2[df2[df2.columns[0]] == catégories[i]][df2.columns[1]])

    plt.boxplot(plots, tick_labels=catégories)
    plt.title(Données.nom)
    plt.xticks(rotation=45)
    plt.gca().set_ylim(ymin = 50)
    plt.grid()
    plt.figure()

def ajouter_carte_corrélations(tableau : Tableau):
    print("affichage de la carte de corrélation de",tableau.nom)
    sns.heatmap(tableau.df,annot=True,cmap="viridis")
    plt.xticks(rotation=45)

def dessiner_graphiques() -> None:
    print("affichage de tout les graphiques")
    plt.show()