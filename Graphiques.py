import matplotlib.pyplot as plt
from Tableau import Tableau


def ajouter_graphiques_écart_types(Données: list[Tableau]):
    for t in Données:
        x = t.lignes
        y = t.valeurs[0]

        if t.nom == "Canada":
            plt.plot(x, y, label=t.nom)
        else:
            plt.plot(x, y, linestyle = "dotted", label = t.nom)
    
    plt.subplot(2,2,1)
    plt.title("Écart-types en fonction du temps")

def ajouter_graphiques_moyenne(Données: list[Tableau]):
    for t in Données:
        x = t.colonnes
        y = []

        for i in range(len(t.colonnes)):
            y.append(t.valeurs[0][i])

        if t.nom == "Canada":
            plt.plot(x, y, label=t.nom)
        else:
            plt.plot(x, y, linestyle = "dotted", label = t.nom)
    plt.subplot(2,2,2)
    plt.title("Moyennes en fonction du temps")

def ajouter_graphiques_médiane(Données: list[Tableau]):
    for t in Données:
        x = t.colonnes
        y = []

        for i in range(len(t.colonnes)):
            y.append(t.valeurs[1][i])

        if t.nom == "Canada":
            plt.plot(x, y, label=t.nom)
        else:
            plt.plot(x, y, linestyle = "dotted", label = t.nom)
    plt.subplot(2,2,3)
    plt.title("Médianes en fonction du temps")

def dessiner_graphiques() -> None:
    plt.legend()
    plt.xticks(rotation = 45)
    plt.show()