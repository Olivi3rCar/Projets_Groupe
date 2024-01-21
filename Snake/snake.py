from tkinter import *
from random import *

class Snake:
    def __init__(self,matriceCellules):
        #calculer les cellules centrales qui feront le corps du snake en début de partie 
        cell_centrale=matriceCellules[(len(matriceCellules))//2].pos#coord de la cell centrale, calculee en fonction de la matrice cellule, devient i_tete, j_tete
                            #si la cell centrale est la tête, alors pour les deux autres cases ont a juste à incrémenter le x des coord x,y
        self.body=[cell_centrale,(cell_centrale[0]+1,cell_centrale[1]),(cell_centrale[0]+2,cell_centrale[1])]#liste de couples représentant le corps du snake 
        self.direction=(0,-1)#gauche au départ, change plus tard selon les inputs du joueur
        pass
    
    def changer_direction(self, event):
        """méthode qui met à jour la direction que va prendre le snake
        """
        if event.keysym=="Left" and self.direction!=(0,1):#si le joueur input Left et que le snake ne va pas à droite
            self.direction=(0,-1)#met à jour direction, vers la gauche
            
        if event.keysym=="Right" and self.direction!=(0,-1):#si le joueur input Right et que le snake ne va pas à gauche
            self.direction=(0,1)#met à jour direction, vers la droite
            
        if event.keysym=="Up" and self.direction!=(1,0):#si le joueur input Up et que le snake ne va pas en bas
            self.direction=(-1,0)#met à jour direction, vers le haut
            
        if event.keysym=="Down" and self.direction!=(-1,0):#si le joueur input Down et que le snake ne va pas en haut
            self.direction=(1,0)#met à jour direction, vers le bas
        pass
        
    def acquerir_cible(self, nb_lignes, nb_colonnes):
        """Méthode qui renvoie les nouvelles coordonnées de la tête du serpent en fonction de self.direction
        """
        (xActu, yActu) = (self.body[0][0],self.body[0][1]) # Définit les coordonnées actuelles de la tête du serpent sous les int xActu et yActu
        
        xNouv = xActu + self.direction[0] # Définit la nouvelle abscisse de tête du serpent en additionnant xActu et la valeur d'abscisse de direction
        if xNouv > nb_colonnes-1: # Cas où la nouvelle abscisse dépasse la dernière colonne par la droite: on "téléporte" la tête de l'autre côté
            xNouv = 0
        elif xNouv < 0 : # cas opposé où la nouvelle abscisse dépasse la première colonne par la gauche
            xNouv = nb_colonnes-1
        
        yNouv = yActu + self.direction[1] # Définit la nouvelle ordonnée de tête du serpent en additionnant yActu et la valeur d'ordonnée de direction
        if yNouv > nb_lignes-1: # Cas où la nouvelle ordonnée dépasse la dernière ligne par le bas: on "téléporte" la tête de l'autre côté
            yNouv = 0
        elif yNouv < 0 : # cas opposé où la nouvelle ordonnée dépasse la première ligne par le haut
            yNouv = nb_lignes-1
        
        return (xNouv, yNouv)
    
    def deplacer(self, grille, i_tete, j_tete):
        """Méthode qui déplace l'ensemble des cellules constituant le snake vers leurs prochaines coordonnées
        """
        global matriceCellules #récupère la matrice des cellules afin de la modifier
        
        coordsPrec = self.body[0] # définit les coordonnées de la cellule précédente avant le déplacement, 
        # afin d'y déplacer ensuite la cellule actuelle (premier cas avec la cellule de tête)
        self.body[0] = (i_tete, j_tete) # Donne à la tête du snake ses nouvelles coordonnées
        matriceCellules[i_tete][j_tete].valeur = 1 # Donne une valeur de 1 (snake) à la cellule au nouvel emplacement de la tête
        
        for cell in range(1, len(self.body)): # Donne leurs nouvelles coordonnées à chaque cellule de body, sauf la tête
            coordsPrec, self.body[cell] = self.body[cell], coordsPrec
            # intervertit les coordonnées de la variable coordsPrec avec les coordonnées de la cellule actuelle du serpent, afin de :
            # - donner à la cellule actuelle les coordonnées où se trouvait la cellule précédente avant son déplacement
            # - donner à la variable coordsPrec les coordonnées de la cellule actuelle, afin de les donner à la cellule suivante
            matriceCellules[self.body[cell][0]][self.body[cell][1]].valeur = 1 # Donne une valeur de 1 (snake) à la cellule au nouvel emplacement    
        
        matriceCellules[coordsPrec[0]][coordsPrec[1]].valeur = 0 # Donne une valeur de 0 (vide) à la cellule étant anciennement la queue du serpent
        matriceCellules[i_tete][j_tete].valeur = 1 # Donne une valeur de 1 (snake) à la cellule au nouvel emplacement de la tête, 
        # l'action est effectuée après le changement de la queue pour ne pas créer d'erreur dans le cas où le nouvel emplacement de la tête
        # est le même que l'ancien emplacement de la queue
        
    def manger(self, grille, i_tete, j_tete):
        #si la cellule cible de la tête à une valeur de 2 (pomme présente):
        #deplacer le snake
        #lui ajouter un nouveau segment à sa queue (soit à l'ancien emplacement de la queue après déplacement)
        pass
        
class Cellule :
    def __init__(self, x, y):
        self.valeur = 0 # Cellule vide au départ
        self.pos = (x, y) # Position de la cellule en fonction de x et y


def taille_fenetre_selon_grill(nbr_columns, nbr_lines, size_cell, fenetre):
    """Méthode qui règle la taille de la fenêtre selon les paramêtres de la grille"""
    x = nbr_columns*size_cell
    y=  nbr_lines*size_cell
    fenetre.geometry(str(x)+"x"+str(y))


def generer_pomme(matriceCellules):
    coord=matriceCellules[randint(0,len(matriceCellules))]#générer coord aléatoire de pomme
    if coord.valeur==0:
        #afficher une pomme
        coord.valeur=2
    "la fonction manger() appelle la fonction generer pomme après le premier appel de celle ci"
    #generer une nouvelle pomme dès que manger est appelé, ou des que aucune cellule a la valeur 2 (pomme présente)
    pass

"""Programme Principal"""
fenetre=Tk() #instance de Tk comme fenetre
fenetre.title("Snake !")

nb_colonnes=30 #paramètres de la taille de la fenetre selon les paramêtres de la matrice cellule
nb_lignes=20
taille_cellule=40

matriceCellules = [Cellule(x, y) for x in range(nb_colonnes) for y in range(nb_lignes)] # Matrice des cellules définissant l'espace de jeu


taille_fenetre_selon_grill(nb_colonnes, nb_lignes, taille_cellule, fenetre) #réglage de la taille de la fenetre 
fenetre.resizable(0,0)

fenetre.bind("<Left>", lambda event: Snake.changer_direction(event)) #binding des touches directionnelles pour faire changer de direction
fenetre.bind("<Right>", lambda event: Snake.changer_direction(event)) #le snake
fenetre.bind("<Up>", lambda event: Snake.changer_direction(event))
fenetre.bind("<Down>", lambda event: Snake.changer_direction(event))

fenetre.mainloop()
print("C'est bon !")