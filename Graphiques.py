import AnalyseDonnées
import matplotlib.pyplot as plt
from Tableau import Tableau

def afficher_graphiques(Données : Tableau):

    x = Données.lignes
    y = Données.valeurs[0]

    plt.plot(x, y)
    plt.show()