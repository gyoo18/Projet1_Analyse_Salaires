import AnalyseDonnées
import matplotlib.pyplot as plt
from Tableau import Tableau

def afficher_graphiques(Données : list[Tableau]):

    for t in Données:

        x = t.lignes
        y = t.valeurs[0]

        plt.plot(x, y, label=t.nom)

    plt.show()