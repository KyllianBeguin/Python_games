"""
PROJET MORPION
Auteur : Kyllian BEGUIN
Script principal
"""
# ZONE D'IMPORT
from morpion_functions import var_init, display_board, checker, play_movement, victory_check
from random import randint

# ZONE D'INITIALISATION DES VARIABLES
board_size, board_surface = var_init()
victory = False
player = False

# ZONE DE CALCUL DES VARIABLES
board = [[str(u + i + 1).zfill(len(list(str(board_surface)))) for i in range(board_size)] for u in
         range(0, board_surface, board_size)]
board_list = [item for sublist in board for item in sublist]






# SCRIPT PRINCIPAL
if __name__ == '__main__':
    while not victory:
        display_board(board)
        print("\n\n", "#" * 50, "\n\n", sep='')

        if not player:
            movement = randint(1,9)
            movement = checker(board, movement)
        elif player:
            movement_str = input("Give a movement: ")
            movement = checker(board, movement_str)

        board = play_movement(movement, board)
        victory = victory_check(board)

        player = not player



    display_board(board)