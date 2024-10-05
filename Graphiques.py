import AnalyseDonnées
import matplotlib.pyplot as plt

def main():

    x = AnalyseDonnées.années
    y = AnalyseDonnées.écart_types

    plt.plot(x, y)
    plt.show()