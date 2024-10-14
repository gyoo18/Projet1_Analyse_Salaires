import matplotlib.pyplot as plt
from Tableau import Tableau

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
    plt.boxplot(Données.df.index,Données.df[Données.df.columns[0]])
    plt.title(Données.nom)
    plt.xticks(rotation=45)
    plt.gca().set_ylim(ymin = 50)
    plt.grid()
    plt.figure()



def dessiner_graphiques() -> None:
    plt.show()