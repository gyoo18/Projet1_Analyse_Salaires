import AnalyseDonnées
import matplotlib.pyplot as plt


def main():

    for t in AnalyseDonnées.tableaux:

        x = t.get_annees()
        y = t.get_ecarts_types()

        plt.plot(x, y, label=t.nom)

    plt.show()


if __name__ == "__main__":
    main()