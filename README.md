# MORPION

*My comments are written in french, sorry about that...*  
*This part will also be written in french, also sorry about that...*  
  
Ce fichier contient des **explications** indiquées dans le fichier [morpion_functions.py](https://github.com/KyllianBeguin/Python_games/blob/01_Morpion/morpion_functions.py)
  
## 1. Calcul de la position du mouvement sur le plateau de jeu
  
Voici comment je calcul la position du mouvement sur le plateau de jeu :  
  
board[(movement - 1) // len(board)][(movement % len(board)) - 1]  
  
### 1.1. Calcul du numéro de ligne
Dans un premier temps, je calcule à quelle **ligne** je dois accéder :  
ligne = [(movement - 1) // len(board)]  
. Je fais alors la [division entière](https://fr.wikipedia.org/wiki/Partie_enti%C3%A8re_et_partie_fractionnaire) du **mouvement** (l'input du joueur) par la **longueur du plateau** de jeu. En faisant seulement cela, je "décale" le numéro de la ligne que je dois accéder, **je soustrais donc 1** à la valeur du mouvement.
