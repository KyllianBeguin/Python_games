"""
PROJET PUISSANCE 4
Auteur : Kyllian BEGUIN
Bibliothèque des fonctions utilisées par p4__main.py
"""

# ZONE D'IMPORT
import random


# ZONE DE GESTION DES ERREURS
class NotAllowedMovement(BaseException):  # Detection de mouvement non autorisés
    pass


# ZONE DES FONCTIONS
# AFFICHAGE --------------------------------------------------
def display_board(board):
    print([str(i) for i in range(7)])
    for nb_line in range(len(board)):
        print(board[nb_line], nb_line)
    return


def play_movement(board, pawn, coordonnees):
    board[coordonnees[1]][coordonnees[0]] = pawn

    return board


# VERIFICATION -----------------------------------------------
def check_line(coordonnees, board, win_case):
    ligne = board[coordonnees[1]]
    win = False
    # print(f"Checking line n°{coordonnees[0]}")
    for k in range(len(ligne) - 4 + 1):  # On a que 4 portions sur la ligne
        portion = ligne[k:k + 4]  # Une portion de 4 emplacements
        if portion == win_case[0] or portion == win_case[1]:
            print(f"Victoire en ligne n°{abs(coordonnees[1] + 1 - len(ligne))}")
            win = not win
    return win


def check_colonne(coordonnees, board, win_case):
    colonne = [ligne[coordonnees[0]] for ligne in board]
    win = False
    # print(f"Checking line n°{coordonnees[0]}")
    for k in range(len(colonne) - 4 + 1):  # On a que 4 portions sur la ligne
        portion = colonne[k:k + 4]  # Une portion de 4 emplacements
        if portion == win_case[0] or portion == win_case[1]:
            print(f"Victoire en colonne n°{coordonnees[0] + 1}")
            win = not win
    return win


def check_diagonales(coordonnees, board, win_case):
    # Rappel : coordonnees = (colonne, ligne)
    win = False

    diag_droite_haut = [(coordonnees[0] + (i + 1), coordonnees[1] - (i + 1)) for i in
                        range(coordonnees[1]) if
                        (coordonnees[0] + (i + 1)) < len(board[0]) and (coordonnees[1] - (i + 1)) >= 0]
    diag_droite_bas = [(coordonnees[0] - (i + 1), coordonnees[1] + (i + 1)) for i in
                       range((len(board) - coordonnees[1]), -1, -1) if
                       (coordonnees[0] - (i + 1) >= 0) and (coordonnees[1] + (i + 1)) < len(board)]
    diagonale_droite = diag_droite_bas + [coordonnees] + diag_droite_haut

    # presque bon pour la gauche, les
    diag_gauche_haut = [(coordonnees[0] - (i + 1), coordonnees[1] - (i + 1)) for i in
                        range(coordonnees[1]) if
                        min(coordonnees[0] - (i + 1), coordonnees[1] - (i + 1)) >= 0]
    diag_gauche_bas = [(coordonnees[0] + (i + 1), coordonnees[1] + (i + 1)) for i in
                       range((len(board) - coordonnees[1]), -1, -1) if
                       (coordonnees[1] + (i + 1)) < len(board) and (coordonnees[0] + (i + 1)) < len(board[0])]
    diagonale_gauche = diag_gauche_bas + [coordonnees] + diag_gauche_haut

    diagonales = ["gauche", "droite"]

    for i in range(2):
        diagonale = [diagonale_gauche, diagonale_droite][i]
        if len(diagonale) >= 4:
            for k in range(len(diagonale) - 4 + 1):
                portion = diagonale[k:k + 4]
                portion_pawns = [board[i[1]][i[0]] for i in portion]
                if portion_pawns == win_case[0] or portion_pawns == win_case[1]:
                    print(f"Victoire en diagonale {diagonales[i]}")
                    win = not win
    return win


def check_move(board_NbCol, num_colonne):
    if num_colonne >= board_NbCol or num_colonne < 0:
        raise NotAllowedMovement

    return num_colonne


def checker(board, str_colonne, player):
    board_NbCol = len(board[0])
    checking_move = True

    # On vérifie la légalité du mouvement
    while checking_move:
        try:
            num_colonne = int(str_colonne)
            print(player, " joue en colonne n°", num_colonne, sep='')
            check_move(board_NbCol, num_colonne)
            checking_move = False
            return num_colonne
        except NotAllowedMovement:
            print("Ce n'est pas une colonne autorisé !")
            if player != "Computer":
                str_colonne = input("Nouvelle colonne: ")
        except ValueError:
            print("Ce n'est pas une valeur valide !")
            str_colonne = input("Nouvelle colonne: ")

    return num_colonne


def check_columnFull(board, num_colonne, player, bot):
    # On vérifie si l'on a besoin de mettre le pion à la ligne au dessus
    num_ligne = len(board) - 1  # La ligne la plus basse est la plus loin dan la liste de lignes
    ligne = board[num_ligne]
    spot = ligne[num_colonne]
    while spot in ["X", "O"]:  # Tant que la case est déjà prise

        try:
            num_ligne -= 1
            ligne = board[num_ligne]  # On va plus haut
            spot = ligne[num_colonne]

        except IndexError:
            if not bot:
                str_colonne = input("Nouvelle colonne: ")  # Colonne pleine = on change de colonne
                num_colonne = checker(board, str_colonne, player)
            elif bot:
                num_colonne = random.randint(0, len(board))

            num_ligne = len(board) - 1
            ligne = board[num_ligne]
            spot = ligne[num_colonne]

    coordonnees = (num_colonne, num_ligne)

    return coordonnees
