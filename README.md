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
  
Je calcul la [partie entière](https://fr.wikipedia.org/wiki/Partie_enti%C3%A8re_et_partie_fractionnaire) de la division entre le **mouvement** (l'input du joueur) par la **longueur du plateau** de jeu. En faisant seulement cela, je "décale" de +1 le numéro de la ligne pour la dernière valeur de la ligne (entrainant un IndexError pour la valeur la plus grande du plateau), **je soustrais donc 1** à la valeur du mouvement.
  
  
### 1.2. Calcul du numéro de colonne  
Je calcul ensuite à quelle **colonne** je dois accéder :  
  
colonne = [(movement % len(board)) - 1]  
  
Je fais calcul la [partie fractionnaire](https://fr.wikipedia.org/wiki/Partie_enti%C3%A8re_et_partie_fractionnaire) de la division entre le mouvement et la longueur du plateau. En faisant seulement cela, je "décale" de +1 le numéro de la colonne, allant jusqu'à me donner le début de la ligne pour la dernière valeur de la ligne. je soustrais donc 1 au résultat.

### 1.3. Exemple  
Voici un exemple des calculs réalisés sur un plateau avec 3 lignes (9 cases)   
Ces lignes de codes vont vous permettre d'apprécier les différents calculs ainsi que l'utilité des soustractions  
for i in range(1, 10):  
print("i =", i, "\t// only =", i//3, "\t// and sub =", (i-1)//3, "\t% only = ", i%3, "\t% and sub =", (i%3)-1)  
  
## 2. Vérification des colonnes  
Ce point fait mention à la compréhension de liste utilisée dans ma fonction victory_check().  
Dans cette fonction, j'utilise une boucle dans laquelle je check à la fois les lignes et les colonnes...  
Pour les colonnes, je passe par une liste qui m'envois le contenu de chaque colonne pour la valeur de la ligne en cour.  
  
Voici le code en question :  
  
for row in range(board_size):  
if board[row] == list_check or [board[j][row] for j in range(board_size)] == list_check:  
print(players[player], "WIN !!", "\n\n")  
victory = True  
  
### 2.1. Le check des colonnes avec [board[j][row] for j in range(board_size)]
Ici, je récupère dans un premier temps la valeur row en cours.  
Ensuite, je fais une liste dans laquelle je demande, pour chaque valeur de 1 à board_size, de me donner les valeurs des cases à la ligne row et à la colonne de la valeur (ici j) . 
  
Cela semble très simple à première vu, mais je tenais à le mettre en lumière pour montrer la puissance de la compréhension de liste qui ici m'a évité de devoir faire une deuxième boucle et calculer les positions.  
  
## 3. Construction du board aka "la quitescence de la compréhension de liste"
