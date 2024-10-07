import matplotlib.pyplot as plt
from Tableau import Tableau


def ajouter_graphiques_écart_types(Données: list[Tableau]):
    plt.subplot(2,2,1)
    for t in Données:
        x = t.lignes
        y = t.valeurs[0]

        if t.nom == "Canada":
            plt.plot(x, y, label=t.nom)
        else:
            plt.plot(x, y, linestyle = "dotted", label = t.nom)
    plt.legend()
    plt.xticks(rotation = 45)
    plt.title("Écart-types en fonction du temps")

def ajouter_graphiques_moyenne(Données: list[Tableau]):
    plt.subplot(2,2,2)
    for t in Données:
        x = t.colonnes
        y = []

        for i in range(len(t.colonnes)):
            y.append(t.valeurs[i][0])

        if t.nom == "Canada":
            plt.plot(x, y, label=t.nom)
        else:
            plt.plot(x, y, linestyle = "dotted", label = t.nom)
    plt.legend()
    plt.xticks(rotation = 45)
    plt.title("Moyennes en fonction du temps")

def ajouter_graphiques_médiane(Données: list[Tableau]):
    plt.subplot(2,2,3)
    for t in Données:
        x = t.colonnes
        y = []

        for i in range(len(t.colonnes)):
            y.append(t.valeurs[i][1])

        if t.nom == "Canada":
            plt.plot(x, y, label=t.nom)
        else:
            plt.plot(x, y, linestyle = "dotted", label = t.nom)
    plt.legend()
    plt.xticks(rotation = 45)
    plt.title("Médianes en fonction du temps")

def ajouter_graphiques_différence_moyenne_médiane(Données: list[Tableau]):
    plt.subplot(2,2,4)
    for t in Données:
        x = t.colonnes
        y = []

        for i in range(len(t.colonnes)):
            y.append(t.valeurs[i][2])

        if t.nom == "Canada":
            plt.plot(x, y, label=t.nom)
        else:
            plt.plot(x, y, linestyle = "dotted", label = t.nom)
    plt.legend()
    plt.xticks(rotation = 45)
    plt.title("Différence entre la moyenne et la médiane en fonction du temps")


def dessiner_graphiques() -> None:
    plt.show()