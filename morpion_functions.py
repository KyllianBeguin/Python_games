"""
PROJET MORPION
Auteur : Kyllian BEGUIN
Bibliothèque des fonctions utilisées par morpion_main.py
"""


# ZONE D'IMPORT
from random import randint


# ZONE D'INITIALISATION DES VARIABLES
board_size = 3
len_max_nb = len(list(str(board_size*board_size)))
moves_designs = ["X"*len_max_nb, "O"*len_max_nb]
player = False
players = ["Computer", "You"]
victory = False

# ZONE DE CALCUL DES VARIABLES
board_surface = board_size * board_size


# board = [[str(u + i + 1).zfill(len(list(str(board_surface)))) for i in range(board_size)] for u in
#          range(0, board_surface, board_size)]
# board_list = [item for sublist in board for item in sublist]


# ZONE DE GESTION DES ERREURS
class NotAllowedMovement(BaseException):  # Detection de mouvement non autorisés
    pass


# ZONE DES FONCTIONS
def var_init():
    global board_size
    global board_surface

    return board_size, board_surface


def display_board(board):
    for i in board:
        print(i, "\n\n")
    return


def check_move(movement, board):
    global board_surface
    global moves_designs

    # On créer un merge des sous listes de la matrice.
    # On ajoute à la liste l'item de la sous liste du board pour chaque item de sous liste.

    if (movement > board_surface or movement < 0) or board[(movement-1)//len(board)][(movement%len(board))-1] in moves_designs:
        raise NotAllowedMovement

    return movement


def checker(board, movement_str):
    global player
    global board_size

    checking_move = True

    while checking_move:
        try:
            movement = int(movement_str)
            print(players[player], " played: ", movement, "\n\n", sep='')
            check_move(movement, board)
            checking_move = False
            return movement
        except NotAllowedMovement:
            print("Ce n'est pas un mouvement autorisé !")
            if player:
                movement_str = input("Give a movement: ")
            elif not player:
                movement_str = randint(1,board_size*board_size)
        except ValueError:
            print("Ce n'est pas une valeur valide !")
    return


def play_movement(movement, board):
    global player

    if int(board[(movement-1)//len(board)][(movement%len(board))-1]) == movement:
        board[(movement-1)//len(board)][(movement%len(board))-1] = moves_designs[player]

    return board

def victory_check(board):
    global victory
    global player
    global moves_designs

    list_check = [moves_designs[player] for i in range(board_size)]

    for row in range(board_size):
        if board[row] == list_check or [board[j][row] for j in range(board_size)] == list_check:
            print(players[player], "WIN !!", "\n\n")
            victory = True
    if [board[0 + j][0 + j] for j in range(board_size)] == list_check or [board[-1 - j][0 + j] for j in range(board_size)] == list_check:
        print(players[player], "WIN !!", "\n\n")
        victory = True
    player = not player
    return victory