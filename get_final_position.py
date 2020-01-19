# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:35:30 2020

@author: Vang Toan
"""
#un programme en python qui lit deux fichiers texte précédents contenant des instructions
#et qui renvoie la position finale du robot B-VZXR apres suivi d'instructions...

import time
import sys

start_time = time.time()
#Cette fonction lit le fichier d’instruction du robot et renvoie deux valeurs
#un tableau contenant toutes les directions de déplacement du robot 
# et un deuxième qui contient le nombre de cases sur lesquels le robot doit se déplacer


def read_files_instruction(path_file_instruction):    
    mat = []  
    deplacement=[]   
    val_deplacement=[]                       
    with open (path_file_instruction, "r") as f: 
        i=0
        for li in f :                 
            s = li.strip ("\n\r")  
            l = s.split (",") 
            mat.append (l)
        for i in range(len(mat)):
            deplacement.append(mat[i][0])
            val_num =int(mat[i][1])
            val_deplacement.append(val_num)
    return deplacement, val_deplacement
        
#Cette fonction lit le fichier universe et renvoie deux valeurs
# x contenant la taille de la largeur de l’univers du robot
# et y qui contient la taille de la hauteur de l’univers du robot


def read_files_universe(path_file_universe): 
    mat = []                        
    with open (path_file_universe, "r") as f: 
        for li in f :                 
            s = li.strip ("\n\r")  
            l = s.split (":") 
            mat.append (l)
        x=int(mat[0][1])
        y=int(mat[1][1])
    return y, x

path_file_instruction = ( sys.argv[1] )
path_file_universe = ( sys.argv[2] )

#passage en paramètres des répertoires des fichiers textes 
#aux deux fonctions précédentes et récupération des valeurs retour

deplacement,val_deplacement = read_files_instruction(path_file_instruction)
pos_y, pos_x = read_files_universe(path_file_universe) 

#definition des deplacement du robots
up='up'
down='down'
left='left'
right='right'

dernier_deplacement = up
new_deplacement=deplacement[0]
position_X=0
position_Y=0


#Toutes les instructions pour définir tous les cas que peut rencontrer le robot pendant son trajet 
#et comment il devra se comporter a chaque instruction différente. Selon par exemple s’il regarde vers la gauche 
#et que la prochaine instruction lui dit d’aller a gauche, il devra se tourner vers le bas avant d’effectuer le déplacement.



for i in range (len(deplacement)):
    val_dep=val_deplacement[i]
    new_deplacement=deplacement[i]
#gestion du "up"
    if ((dernier_deplacement==up and new_deplacement==left) or (dernier_deplacement==down and new_deplacement==left)):
        if(position_X >= val_dep):
            #deplace toi vers vers left a gauche 
            position_X=position_X-val_dep
        elif(position_X <= val_dep):
            #deplace toi vers vers left a gauche 
            position_X=0
        dernier_deplacement=left
    elif((dernier_deplacement==up and new_deplacement==right) or (dernier_deplacement==down and new_deplacement==right)):
        #deplace toi vers vers right a droite        
        if((position_X+val_dep)<=pos_x):
            #deplace toi vers vers left a gauche 
            position_X=position_X+val_dep
        elif((position_X+val_dep) >= pos_x):
            #deplace toi vers vers left a gauche 
            position_X=pos_x
        dernier_deplacement=right
    elif((dernier_deplacement==left and new_deplacement==left) or (dernier_deplacement==right and new_deplacement==right)):
        #deplace toi vers vers down en bas 
        if(position_Y >= val_dep):
            #deplace toi vers vers left a gauche 
            position_Y=position_Y-val_dep
        elif(position_Y <= val_dep):
            #deplace toi vers vers left a gauche 
            position_Y=0
        dernier_deplacement=down
    elif((dernier_deplacement==left and new_deplacement==right) or (dernier_deplacement==right and new_deplacement==left)):
        #deplace toi vers vers up en haut         
        if((position_Y+val_dep)<=pos_y):
            #deplace toi vers vers left a gauche 
            position_Y=position_Y+val_dep
        elif((position_Y+val_dep) >= pos_y):
            #deplace toi vers vers left a gauche 
            position_Y=pos_y
        dernier_deplacement=up      
time_end=time.time() - start_time
    #print('position de x a l iteration ',i,' est :',position_X)
    #print('position de y a l iteration ',i,' est :',position_Y)
    #print('postion dernier depalcement------------', dernier_deplacement)
    #print('------------------------------------------------------------------')

print('#########################################################################')
print('#                                                                      ##')                             
print('# RENDU DE LA POSITION DU ROBOT B-VZXR DANS UN SYSTEME DE REPERE(X,Y)  ##')
print('#                                                                      ##')
print('#########################################################################')
    
print('')
print('ouff j\'ai effectuer :',len(deplacement), ' deplacements!!! en ',time_end,' milliemes de seconde du coup je suis tous épuisé!!!\n')
print('-------------------------------------------------------------------------------------')
print('je suis actuellement a la case de coordonnée :  *X=',position_X,'* et *Y=',position_Y,'* au cas ou vous avez besoin de moi\n')
print(';-)\n\n\n')
    