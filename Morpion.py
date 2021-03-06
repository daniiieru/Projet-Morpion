# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GptgzSvfkvqpIDmBQ3qsf2ZFFxPxnjw8
"""

####################################################################
## PREMIER PROJET NSI - moteur de jeu de morpion                  ##
####################################################################

# définition des "constantes"
VIDE    = '.'          # symbôle d'une case vide
JOUEURS = ('O', 'X')   # tuple qui contient les symbôles des 2 joueurs
NOMBRE_DE_LIGNES   = 3 # sans commentaire...
NOMBRE_DE_COLONNES = 3 # ...
 
# ne vous embêtez pas avec ça, c'est un dictionnaire, vous n'avez pas encore eu le cours dessus.
# Il me sert dans la gestion de l'affichage
COULEURS = {VIDE : '\033[1;30m', JOUEURS[0] : '\033[0;31m', JOUEURS[1] : '\033[0;32m'}
 
 
# création du tableau de jeu
# c'est un tableau de NOMBRE_DE_LIGNES lignes sur NOMBRE_DE_COLONNES colonnes
tableau_de_jeu = [ [VIDE for j in range(NOMBRE_DE_COLONNES)] for i in range(NOMBRE_DE_LIGNES)]
 
 
def case_jouable(i,j):
  if i in [0,1,2] and j in [0,1,2] and tableau_de_jeu[i][j] == ".":
    return('Cette case est libre, tu peux y aller ;)')
  else:
    print("Les coordonnées de la case doivent etre comprise entre 0 et 2 et la case doit etre vide")
   
 
def encore_au_moins_une_case_jouable():
  var = 0
  for i in range(NOMBRE_DE_LIGNES):
    for j in range(NOMBRE_DE_COLONNES):
      if tableau_de_jeu[i][j] == VIDE:
        var = var+1
  if (var >= 1) :
    return(True)
  else:
     return(False)
 
def joueur_gagnant():
  if il_y_a_un_gagnant() == True:
    return JOUEURSG
  else:
    print("")
 
 
def il_y_a_un_gagnant():
  global JOUEURSG
 
              #POUR LE JOUEUR QUI JOUE 'X'
  #XXX
  #OOO
  #OOO
  if tableau_de_jeu[0][0] and tableau_de_jeu[0][1] == 'X' and tableau_de_jeu[0][2] == 'X':
    JOUEURSG = 'X'
    return(True)
 
  #OOO
  #XXX
  #OOO

  if tableau_de_jeu[1][0] == 'X' and tableau_de_jeu[1][1] == 'X' and tableau_de_jeu[1][2] == 'X':
    JOUEURSG = 'X'
    return(True)
 
  #OOO
  #OOO
  #XXX

  if tableau_de_jeu[2][0] == 'X' and tableau_de_jeu[2][1] == 'X' and tableau_de_jeu[2][2] == 'X':
    JOUEURSG = 'X'
    return(True)

  #OOX
  #OXO
  #XOO
  if tableau_de_jeu[0][2] == 'X' and tableau_de_jeu[1][1] == 'X' and tableau_de_jeu[2][0] == 'X':
    JOUEURSG = 'X'
    return(True)
 
  #XOO
  #OXO
  #OOX
  if tableau_de_jeu[0][0] == 'X' and tableau_de_jeu[1][1] == 'X' and tableau_de_jeu[2][2] == 'X':
    JOUEURSG = 'X'
    return(True)
 
  #XOO
  #XOO
  #XOO
  if tableau_de_jeu[2][0] == 'X' and tableau_de_jeu[1][0] == 'X' and tableau_de_jeu[0][0] == 'X':
    JOUEURSG = 'X'
    return(True)
 
  #OXO
  #OXO
  #OXO
  if tableau_de_jeu[0][1] == 'X' and tableau_de_jeu[1][1] == 'X' and tableau_de_jeu[2][1] == 'X':
    JOUEURSG = 'X'
    return(True)
 
  #OOX
  #OOX
  #OOX
  if tableau_de_jeu[0][2] == 'X' and tableau_de_jeu[1][2] == 'X' and tableau_de_jeu[2][2] == 'X':
    JOUEURSG = 'X'
    return(True)
 
              #POUR LE JOUEUR QUI JOUE 'O'
 
  #OOO
  #XXX
  #XXX
  if tableau_de_jeu[0][0] == 'O' and tableau_de_jeu[0][1] == 'O' and tableau_de_jeu[0][2] == 'O':
    JOUEURSG = 'O'
    return(True)
 
  #XXX
  #OOO
  #XXX
  if tableau_de_jeu[1][0] == 'O' and tableau_de_jeu[1][1] == 'O' and tableau_de_jeu[1][2] == 'O':
    JOUEURSG = 'O'
    return(True)
 
  #XXX
  #XXX
  #OOO
  if tableau_de_jeu[2][0] == 'O' and tableau_de_jeu[2][1] == 'O' and tableau_de_jeu[2][2] == 'O':
    JOUEURSG = 'O'
    return(True)
 
  #XXO
  #XOX
  #OXX
  if tableau_de_jeu[0][2] == 'O' and tableau_de_jeu[1][1] == 'O' and tableau_de_jeu[2][0] == 'O':
    JOUEURSG = 'O'
    return(True)
 
  #OXX
  #XOX
  #XXO
  if tableau_de_jeu[0][0] == 'O' and tableau_de_jeu[1][1] == 'O' and tableau_de_jeu[2][2] == 'O':
    JOUEURSG = 'O'
    return(True)
 
  #OXX
  #OXX
  #OXX
  if tableau_de_jeu[2][0] == 'O' and tableau_de_jeu[1][0] == 'O' and tableau_de_jeu[0][0] == 'O':
    JOUEURSG = 'O'
    return(True)
 
  #XOX
  #XOX
  #XOX
  if tableau_de_jeu[0][1] == 'O' and tableau_de_jeu[1][1] == 'O' and tableau_de_jeu[2][1] == 'O':
    JOUEURSG = 'O'
    return(True)
 
  #XXO
  #XXO
  #XXO
  if tableau_de_jeu[0][2] == 'O' and tableau_de_jeu[1][2] == 'O' and tableau_de_jeu[2][2] == 'O':
    JOUEURSG = 'O'
    return(True)
 
 
def partie_terminee():
  if encore_au_moins_une_case_jouable() == False or il_y_a_un_gagnant() == True:
    return(True)
  else:
    return(False)
 
 
############# fonctions gracieusement fournies par le prof ---------
# Ne pas modifier --------------------------------------------------
def rep(condition):
  '''Transforme True et False en 'oui' et 'non'
  Entrée : un booléen
  Sortie : une chaîne de caractères'''
  if condition:
    return "oui"
  return "non"
 
def affiche_tableau_de_jeu():
  '''Affiche le tableau de jeu dans la console
     Entrée : rien
     Sortie : le tableau de jeu et des informations '''
  print("  ", end=' ')
  for j in range(NOMBRE_DE_COLONNES):
    print('\033[1;37m'+str(j), end='  ')
  print()
  for i in range(NOMBRE_DE_LIGNES):
    print ('\033[1;37m'+str(i), end='  ')
    for j in range(NOMBRE_DE_COLONNES):
      print(COULEURS[tableau_de_jeu[i][j]]+tableau_de_jeu[i][j],' ', end='')
    print(COULEURS[VIDE])
  print(f"Partie terminée : {rep(partie_terminee())}")
  print(f'Il y a  encore au moins une case jouable : {rep(encore_au_moins_une_case_jouable())}')
  print(f"il y a un gagnant : {rep(il_y_a_un_gagnant())} - ({joueur_gagnant()})")
############# fonctions gracieusement fournies par le prof ---------
 
 
def pose_pion(numero_du_joueur, i, j):
  k = numero_du_joueur
  if (k == 0) :
    tableau_de_jeu[i][j] = 'O'
  else:
    tableau_de_jeu[i][j] = 'X'
  affiche_tableau_de_jeu() # à la fin de pose_pion(), on affiche le tableau de jeu, donc
                           # ne pas changer cette dernière instructio