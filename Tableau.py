class Tableau:
    valeurs = []  # valeurs[x][y], la représentation est comme suit : x est croissant vers la gauche (->) et y est croissant vers le bas (v)
                        #  |̅                                           ̅ |   0
                        #  | |̅  ̅ | |̅  ̅ | |̅  ̅ | |̅  ̅ | |̅  ̅ | |̅  ̅ | |̅  ̅ |  |   
                        #  | | o,| | o,| | o,| | o,| | o,| | o,| | o,|  |   |
                        #  | | o,| | o,| | o,| | o,| | o,| | o,| | o,|  |   |
                        #  | | o,| | o,| | o,| | o,| | o,| | o,| | o,|  |   V
                        #  | |_ _|,|_ _|,|_ _|,|_ _|,|_ _|,|_ _|,|_ _|  |   
                        #  |_                                          _|   Y+
                        #      0     ==========> X+

    colonnes = []   # nom des colonnes
    lignes = []     # nom des lignes
    nom = ""         # nom du tableau

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

    def retirerColonneInt(self, indexe : int):
        if type(indexe) != int:
            raise TypeError("Indexe doit être de type int.")
        del self.valeurs[indexe]
        del self.colonnes[indexe]
    
    def retirerLigneInt(self, indexe : int):
        if type(indexe) != int:
            raise TypeError("Indexe doit être de type int.")
        for i in range(len(self.valeurs[0])):
            del self.valeurs[i][indexe]
        del self.lignes[indexe]

    def retirerColonneNom(self, nom : str):
        if type(nom) != str:
            raise TypeError("Nom doit être de type str.")
        indexe = self.colonnes.index(nom)
        self.retirerLigne(indexe)
    
    def retirerLigneNom(self, nom : str):
        if type(nom) != str:
            raise TypeError("Nom doit être de type str.")
        indexe = self.lignes.index(nom)
        self.retirerLigne(indexe)

