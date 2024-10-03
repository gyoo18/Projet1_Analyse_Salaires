
class Tableau:
    valeurs = [[]] # valeurs[x][y], x = > et y = v
    colonnes = []
    lignes = []

    def __init__(self):
        self.valeurs = [[]]
    
    def ajouterColonne(self,nom : str):
        if type(nom) != str:
            raise TypeError("Nom doit être de type str.")
        self.valeurs.append( [] * len(self.valeurs[0]) )
        self.colonnes.append(nom)
    
    def ajouterLigne(self,nom : str):
        if type(nom) != str:
            raise TypeError("Nom doit être de type str.")
        for i in range(len(self.valeurs)):
            self.valeurs[i].append(0)
        self.lignes.append(nom)

    def retirerColonne(self, indexe):
        if type(indexe) != int:
            raise TypeError("Indexe doit être de type int.")
        del self.valeurs[indexe]
        del self.lignes[indexe]
    
    def retirerLigne(self, indexe):
        if type(indexe) != int:
            raise TypeError("Indexe doit être de type int.")
        for i in range(len(self.valeurs[0])):
            del self.valeurs[i][indexe]
        del self.lignes[indexe]

    def retirerColonne(self, nom):
        if type(nom) != str:
            raise TypeError("Nom doit être de type str.")
        indexe = self.colonnes.index(nom)
        self.retirerLigne(indexe)
    
    def retirerLigne(self, nom):
        if type(nom) != str:
            raise TypeError("Nom doit être de type str.")
        indexe = self.lignes.index(nom)
        self.retirerLigne(indexe)

