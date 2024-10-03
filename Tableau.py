class Tableau:
    valeurs = [] # valeurs[x][y], x = > et y = v
    colonnes = []
    lignes = []
    nom = ""

    def __init__(self, nom : str):
        self.nom = str(nom)
    
    def ajouterColonne(self,nom : str):
        if type(nom) != str:
            raise TypeError("Nom doit être de type str.")
        
        if len(self.valeurs) > 0:
            self.valeurs.append( [] * len(self.valeurs[0]) )
        else:
            self.valeurs.append([])
        
        self.colonnes.append(nom)
    
    def ajouterLigne(self,nom : str):
        if type(nom) != str:
            raise TypeError("Nom doit être de type str.")
        for i in range(len(self.valeurs)):
            self.valeurs[i].append(0)
        self.lignes.append(nom)

    def retirerColonneI(self, indexe : int):
        if type(indexe) != int:
            raise TypeError("Indexe doit être de type int.")
        del self.valeurs[indexe]
        del self.colonnes[indexe]
    
    def retirerLigneI(self, indexe : int):
        if type(indexe) != int:
            raise TypeError("Indexe doit être de type int.")
        for i in range(len(self.valeurs[0])):
            del self.valeurs[i][indexe]
        del self.lignes[indexe]

    def retirerColonneN(self, nom : str):
        if type(nom) != str:
            raise TypeError("Nom doit être de type str.")
        indexe = self.colonnes.index(nom)
        self.retirerLigne(indexe)
    
    def retirerLigneN(self, nom : str):
        if type(nom) != str:
            raise TypeError("Nom doit être de type str.")
        indexe = self.lignes.index(nom)
        self.retirerLigne(indexe)

