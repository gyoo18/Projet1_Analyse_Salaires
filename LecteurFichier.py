#                            _..-===-.._
#                          .o   O   O   o.
#                         (( ( (  O  ) ) ))                                               .
#                          ^-.(_\( )/_).-^                                          .    /
#                               \^V^/                                              /    /   .    .
#                            \   |||    /                                         |^-._/   /    /
#                      ^-._   \  |||   /   _.-^                                    \  /-._/    /
#       		           ^-._\/ | \ /_.-^   					                    \/    ^-._/    .
#                          __.-^.-^-.^-.__                                          /  .-.  //^-._/
#               .=============================================================== - /  |\O/|//____/
#               |  ____            ____  ___   _______   ___   __  __  ___   __   /___^-|-^/  _  *
#               |  \\\\\    __    ///// //=\\ ||||==\\\ |   \ |  ||  ||   \ |  | /  __\_///  | | |
#               |   \\\\\  //\\  ///// ///_\\\||||__))))|    \|  ||  ||    \|  ||  /    \__| | | |
#               |    \\\\\///\\\///// ///(_)\\\|||V//// |        ||  ||        ||  |   ____  |_| |
#            _  |     \\\\///\\\//// /////=\\\\\||\\\\  |  |\    ||  ||  |\    ||  \__|_   |  _  |
#        O   \\ |      \\\//  \\/// /////   \\\\\| \\\\ |__| \___||__||__| \___| \________/  (_) |
#     ___|____))______                                                                           |
#    / _ ||_(______)_|| - =====================_=================================================*
#   | (_|||_(_____\\_||_______________________( \ ) 
#    \___||_(______)_||========================| )>-  --[[>                       -[[>
#           //\\    _                         (_/)            .---------------------------------.
#          //  \\  //                                         | You are entering a danger zone. |
#         //    \\                                            *---------------------------------*

from Tableau import Tableau

def isfloat(a):
    try: 
        float(a)
        return True
    except ValueError:
        return False

def Lire_Tableau_csv( répertoire : str, nom_de_lignes : bool, séparateur = ";", nom = ""):

    #Vérifier la validité des paramètres
    if(type(répertoire) != str):
        raise TypeError("Répertoire doit être un string.")
    
    # Extraire le fichier
    print("Ouverture du fichier " + répertoire)
    fichier = open(répertoire,"r")
    lignes = []
    lire = True
    while lire:
        motsLigne = fichier.readline()
        if motsLigne == "":
            break
        lignes.append(motsLigne)
    fichier.close()

    # Transformer en liste 2D
    print("Extraction des données")
    cases = [[] for i in range(len(lignes))] # cases[y][x] x = > et y = v
    for i in range(len(lignes)):
        motsLigne = []
        mot = ""
        for j in range(len(lignes[i])):
            if lignes[i][j] == séparateur or lignes[i][j] == '\n':
                mot = mot.replace('"','')
                motsLigne.append(mot)
                mot = ""
            else:
                mot += lignes[i][j]
        
        for j in range(len(motsLigne)):
            cases[i].append(motsLigne[j])
        
    # Analyser pour ne conserver que le tableau de données
    # Dans notre cas, le tableau sera le plus long rectangle de cases dont la première ligne est entièrement pleine (c'est l'en-tête du tableau)

    # Trouver la ligne contigue la plus longue
    print("Extraction du tableau")
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
    print("Préparation pour l'utilisation")
    tableau = Tableau(nom if nom != "" else répertoire)
    
    tmpi = 1 if nom_de_lignes else 0
    
    for i in range(len(cases_ordonnées)-tmpi):
        tableau.ajouterColonne(cases_ordonnées[i+tmpi][0])
    if nom_de_lignes:
        for i in range(len(cases_ordonnées[0])-1):
            tableau.ajouterLigne(cases_ordonnées[0][i+1])
    else:
        for i in range(len(cases_ordonnées[0])-1):
            tableau.ajouterLigne(str(i))
        
    for i in range(len(tableau.colonnes)-tmpi):
        for j in range(len(tableau.lignes) - 1):
            if isfloat( cases_ordonnées[i+tmpi][j+1].replace(' ','').replace(',','.') ):
                tableau.valeurs[i][j] = float(cases_ordonnées[i+tmpi][j+1].replace(' ','').replace(',','.'))
            else:
                tableau.valeurs[i][j] = cases_ordonnées[i+tmpi][j+1]

    return tableau