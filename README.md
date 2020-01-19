# ROBOT-B-VZXR
Compilation (et compréhension du programme)
Objectifs
L'objectif de ce TP est de s’exercer avec le langage Python tout en manipulant les fichiers, les tableaux de variables, des séquences d’instructions conditionnelles et répétitives.... 
Le programme écrit est un système simplifié de lecture d'instructions par un petit robot téléguidé, nommé B-VZXR.
Le but de l'exercice est de construire un programme qui lit une suite d'instruction et donne la position finale de B-VZXR
Pour compiler notre code à la main, nous allons suivre quelques étapes.
Mise en place
Les prérequis pour exécuter le programme sont :
-	Avoir installé Python sur sa machine
-	Avoir installé un éditeur et compilateur de code Python (Spyder est un environnement de développement pour Python. Libre et multiplateforme qui intègre de nombreuses bibliothèques d'usage scientifique. C’est l’IDE que nous avons utilisé pour le développement de ce programme)
L'univers du robot
B-VZXR vit dans un espace rectangulaire plat, comme un échiquier de taille n * p.
Chacune des n * p positions, ou cases, est définie par son abscisse et son ordonnée.
Le robot naît toujours sur la case en bas à gauche (ie. d'abscisse et d'ordonnée nulle), la tête vers le haut
C’est ainsi que pour créer l’univers dans lequel le robot se déplacera on créé un fichier texte qui contient les paramètres width et height, ie la largeur et la hauteur consécutivement, suivi de leur valeur.
Le fichier universe.txt pour l’exemple contient :
width: 120
height: 100
On a donc un espace de 120 cases en largeur X 100 cases en hauteur.

Le langage du robot
Le petit robot ne comprend qu'un seul type d'instruction, qu'il lit de manière séquentielle.
Une instruction est composée de deux éléments :
Une chaîne de caractère : "right" ou "left"
Un nombre positif ou nul : 0, 1, 2…
Lorsque B-VZXR lit une instruction :
il va se tourner d'un quart de tour :
vers sa droite si la chaîne de caractère vaut "right"
vers sa gauche si la chaîne de caractère vaut "left"

Il va ensuite avancer de k cases selon la valeur du nombre
si il devait rencontrer un mur, il s'arrêtera d'avancer et lirait l'instruction suivante.
Il faudra disposer de ce fichier qui contiendra toutes les instructions a suivre par le robot dans un format precis. 
Voici les 10 premières lignes des 500 instructions au total qui existent dans le fichier instrucion_list.txt
right, 6
left, 10
left, 8
left, 1
right, 7
left, 7
right, 5
right, 5
right, 1
left, 1


1.	Commencez par créer un dossier dans un espace personnel
2.	Créez un fichier appelé get_final_position.py dans le répertoire créé. 
3.	Recopiez-y le code que contient le fichier get_final_position.py à l'intérieur du fichier créé.
4.	Pour comprendre le programme, nous avons les commentaires précédents chaque groupe de code

Apres avoir enregistré le ficher, pour poursuivre l’exécution, Il voudra vous positionner dans le répertoire courant du programme .py et de préférence, copier les fichiers textes dans ce même répertoire. 
 Le code peut être exécuté dans l’éditeur utilisé et pour pouvoir voir les résultats , il faudra exécuter la commande suivante dans la console de l’éditeur de code .
$ python get_final_position.py instrucion_list.txt universe.txt


Compilation (Dans la console de l’ordinateur)
Tapez cette commande sur votre terminal :
 python repertoire_du_fichier_get_final_position.py repertoire_du_fichier_instruction_list.txt repertoire_du_fichier_universe.txt
//
//
Exemple :
------------------------------------------------------------
 $ python .\get_final_position.py .\instrucion_list.txt .\universe.txt
------------------------------------------------------------
//
//

Si tous les fichiers sont dans le même répertoire, tapez les commandes
 1ere commande:
$  cd repertoire_des_fichiers
 2eme commande:
$  python get_final_position.py nom_du_fichier_contenant_instruction_list.txt nom_du_fichier_contenant_universe.txt
------------------------------------------------------------
exemple:

$  cd E:\cours\entretien\new
------------------------------------------------------------
 $  python get_final_position.py instrucion_list.txt universe.txt
------------------------------------------------------------


Voici le rendu du programme avec les positions du robot B-VZXR X et de Y

###################################################################
# RENDU DE LA POSITION DU ROBOT B-VZXR DANS UN SYSTEME DE REPERE(X,Y)  ##
###################################################################

ouff j'ai effectuer : 500  deplacements!!! en  0.01730179786682129  milliemes de seconde du coup je suis tous épuisé!!!

-------------------------------------------------------------------------------------
je suis actuellement a la case de coordonnée :  *X= 113 * et *Y= 87 * au cas ou vous avez besoin de moi

;-)
