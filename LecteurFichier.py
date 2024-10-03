import Tableau
from multipledispatch import dispatch

def Lire_Tableau_csv(répertoire : str):

    #Vérifier la validité des paramètres
    if(type(répertoire) != str):
        raise TypeError("Répertoire doit être un string.")
    
    # Extraire le fichier
    fichier = open(répertoire,"r")
    lignes = []
    lire = True
    while lire:
        motsLigne = fichier.readline()
        if motsLigne == "":
            break
        lignes.append(motsLigne)

    # Transformer en liste 2D
    cases = [[] for i in range(len(lignes))] # cases[y][x] x = > et y = v
    for i in range(len(lignes)):
        motsLigne = []
        mot = ""
        for j in range(len(lignes[i])):
            if lignes[i][j] == ';' or lignes[i][j] == '\n':
                motsLigne.append(mot)
                mot = ""
            else:
                mot += lignes[i][j]
        
        for j in range(len(motsLigne)):
            cases[i].append(motsLigne[j])
        
    # Analyser pour ne conserver que le tableau de données
    # Dans notre cas, le tableau sera le plus long rectangle de cases dont la première ligne est entièrement pleine (c'est l'en-tête du tableau)

    # Trouver la ligne contigue la plus longue
    longeur_max = 0
    indexe_max = 0
    for i in range(len(cases)):
        est_contigue = True
        for j in range(len(cases[i])):
            if cases[i][j] == "":
                est_contigue = False
                break
        
        if est_contigue and len(cases[i]) > longeur_max:
            longeur_max = len(cases[i])
            indexe_max = i
    
    indexe_en_tête = indexe_max

    # Retirer toutes les lignes qui ne font pas parties du tableau
    # Retirer toutes les lignes au-dessus de l'en-tête
    # Dès qu'une ligne ne fait pas la longueur de l'en-tête, retirer toutes les lignes en-dessous, incluant celle-là
    cases_nettoyées = []
    en_dessous = False
    for i in range(len(cases)):
        if len(cases[i]) == longeur_max and i >= indexe_en_tête:
            cases_nettoyées.append(cases[i])
        elif i >= indexe_en_tête and len(cases[i]) < longeur_max:
            break
    
    # Réarranger les cases pour qu'elles soient dans le même ordre que le tableau
    cases_ordonnées = [[0 for i in range(len(cases_nettoyées))] for i in range(len(cases_nettoyées[0]))] # cases_nettoyées[x][y] x = > et y = v
    for i in range(len(cases_nettoyées)):
        for j in range(len(cases_nettoyées[i])):
            cases_ordonnées[j][i] = cases_nettoyées[i][j]

    if not isinstance(cases_ordonnées[0],list):
            raise TypeError("Cases doit être une liste à 2 dimensions.")

    # Transformer en tableau
    tableau = Tableau.Tableau()
    for i in range(len(cases_ordonnées)-1):
        tableau.ajouterColonne(cases_ordonnées[i+1][0])
    for i in range(len(cases_ordonnées[0])-1):
        tableau.ajouterLigne(cases_ordonnées[0][i+1])

    for i in range(len(cases_ordonnées)-1):
        for j in range(len(cases_ordonnées[i])-1):
            if cases_ordonnées[i+1][j+1].isdigit():
                tableau.valeurs[i][j] = float(cases_ordonnées[i+1][j+1])
            else:
                tableau.valeurs[i][j] = cases_ordonnées[i+1][j+1]

    return tableau