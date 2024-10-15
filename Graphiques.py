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

    if Données.régression_linéaire != None:
        reglin = Données.régression_linéaire
        plt.plot(Données.df[Données.df.columns[0]], reglin.intercept + reglin.slope*Données.df[Données.df.columns[0]], 'r', label = (("%.3f" % reglin.slope) + "X + " + ("%.3f"%reglin.intercept) + " R^2 = " + ("%.3f"%reglin.rvalue)))

    plt.title(Données.nom)
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()
    plt.figure()

def ajouter_diagramme_à_bandes(Données : Tableau):
    print("Afficher",Données.nom)

    catégories_set = set(Données.df.index)
    catégories = []
    correspondant = False
    for i in range(len(catégories_quantitatives_set)):
        if catégories_set == catégories_quantitatives_set[i]:
            catégories = catégories_quantitatives_list[i]
            correspondant = True
    if not correspondant:
        catégories = list(catégories_set)

    valeurs = []
    for i in range(len(catégories)):
        valeurs.append(Données.df.iat[Données.df.index.tolist().index(catégories[i]),0])

    ax = plt.bar(catégories,valeurs)
    plt.bar_label(ax)
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
    correspondance = False
    for i in range(len(catégories_quantitatives_set)):
        if catégories_set == catégories_quantitatives_set[i]:
            catégories = catégories_quantitatives_list[i]
            correspondance = True
    if not correspondance:
        catégories = list(catégories_set)

    plots = []
    for i in range(len(catégories)):
        plots.append(df2[df2[df2.columns[0]] == catégories[i]][df2.columns[1]])

    ax = plt.boxplot(plots, tick_labels=catégories)
    plt.title(Données.nom)
    plt.xticks(rotation=45)
    plt.gca().set_ylim(ymin = 50)
    plt.grid()
    plt.figure()

def ajouter_diagramme_à_bandes_et_moustaches(Données_bandes : Tableau,Données_moustaches : Tableau):
    Données = Données_bandes
    print("Afficher",Données.nom)

    catégories_set = set(Données.df.index)
    catégories = []
    correspondant = False
    for i in range(len(catégories_quantitatives_set)):
        if catégories_set == catégories_quantitatives_set[i]:
            catégories = catégories_quantitatives_list[i]
            correspondant = True
    if not correspondant:
        catégories = list(catégories_set)

    valeurs = []
    for i in range(len(catégories)):
        valeurs.append(Données.df.iat[Données.df.index.tolist().index(catégories[i]),0])

    ax = plt.bar(catégories,valeurs,)
    plt.bar_label(ax)
    
    Données = Données_moustaches
    df2 = Données.df

    plots = []
    for i in range(len(catégories)):
        plots.append(df2[df2[df2.columns[0]] == catégories[i]][df2.columns[1]])

    ax = plt.boxplot(plots, tick_labels=catégories)

    plt.title(Données.nom)
    plt.xticks(rotation=45)
    plt.gca().set_ylim(ymin = 50)
    plt.grid()
    plt.figure()

def ajouter_carte_corrélations(tableau : Tableau):
    print("affichage de la carte de corrélation de",tableau.nom)
    sns.heatmap(tableau.df,annot=True,cmap="viridis")
    plt.xticks(rotation=45)
    plt.figure()
    #plt.show()

def dessiner_graphiques() -> None:
    print("affichage de tout les graphiques")
    plt.show()