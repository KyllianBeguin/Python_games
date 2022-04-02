"""
PROJET PUISSANCE 4
Auteur : Kyllian BEGUIN
Script principal
"""

# ZONE D'IMPORT DES MODULES
import p4___functions as p4f
import random

# ZONE D'INITIALISATION DES VARIABLES
pawns = ["X", "O"]
players = [input("Votre pseudo: "), "Computer"]

win_case = [[pawns[0] for i in range(4)], [pawns[1] for i in range(4)]]
win_ligne = False
win_colonne = False
win_diagonale = False

# UNE PARTIE, VOUS VS L'ORDINATEUR, 20 COUPS AUTORISÉS
if __name__ == "__main__":

    for i in range(1):  # Modifier la valeur du range si vous souhaitez faire plusieurs parties

        print(f"BOARD N°{i + 1}")
        board = [[" " for i in range(7)] for k in range(6)]  # Initialisation du board
        p4f.display_board(board)

        for coup in range(20):
            # Mise en place du tour du joueur
            pawn = pawns[coup % len(pawns)]
            player = players[coup % len(pawns)]

            # Jouer le coup
            if player != "Computer":
                str_colonne = input("Choisissez votre colonne : ")
                num_colonne = p4f.checker(board, str_colonne, player)
                coordonnees = p4f.check_columnFull(board, num_colonne, player, bot=False)
                board = p4f.play_movement(board, pawn, coordonnees)

            # Partie "ordinateur"
            elif player == "Computer":
                num_colonne = random.randint(0, len(board))
                coordonnees = p4f.check_columnFull(board, num_colonne, player, bot=True)
                print(f"L'ordinateur joue en colonne n°{coordonnees[1]}")
                board = p4f.play_movement(board, pawn, coordonnees)
                p4f.display_board(board)

            # Variables de victoire
            win_ligne = p4f.check_line(coordonnees, board, win_case)
            win_colonne = p4f.check_colonne(coordonnees, board, win_case)
            win_diagonale = p4f.check_diagonales(coordonnees, board, win_case)

            # Recherche d'une victoire dans les variables de vitoire
            if True in [win_ligne, win_colonne, win_diagonale]:
                print(f"Coup n°{coup + 1}")
                p4f.display_board(board)
                break

        # Égalité
        if True not in [win_ligne, win_colonne, win_diagonale]:
            print("Égalité !")
            p4f.display_board(board)