from tkinter import *
from random import *

class Snake:
    def __init__(self,matriceCellules):
        self.mat = matriceCellules # Référence à la matrice matriceCellules
        cell_centrale=(nb_colonnes//2,nb_lignes//2)#définition de la cellule de tête comme la cellule centrale
        self.body=[cell_centrale,(cell_centrale[0],cell_centrale[1]-1),
                   (cell_centrale[0],cell_centrale[1]-2)]#liste de couples représentant le corps du snake 
        for cell in self.body :
            self.mat[cell[0]][cell[1]].valeur = 1
        dessiner_grille(self.mat)
        self.direction=(0,1)#droite au départ, change plus tard selon les inputs du joueur
        self.direction_cible = self.direction # attribut permettant d'empêcher d'éventuels problèmes au niveau du mouvement
    
    def changer_direction(self, event):
        """méthode qui met à jour la direction que va prendre le snake
        """
        if event.keysym=="Left" and self.direction!=(0,1):#si le joueur input Left et que le snake ne va pas à droite
            self.direction_cible=(0,-1)#met à jour direction_cible, vers la gauche
            
        if event.keysym=="Right" and self.direction!=(0,-1):#si le joueur input Right et que le snake ne va pas à gauche
            self.direction_cible=(0,1)#met à jour direction_cible, vers la droite
            
        if event.keysym=="Up" and self.direction!=(1,0):#si le joueur input Up et que le snake ne va pas en bas
            self.direction_cible=(-1,0)#met à jour direction_cible, vers le haut
            
        if event.keysym=="Down" and self.direction!=(-1,0):#si le joueur input Down et que le snake ne va pas en haut
            self.direction_cible=(1,0)#met à jour direction_cible, vers le bas
        pass
        
    def acquerir_cible(self):
        """Méthode qui renvoie les nouvelles coordonnées de la tête du serpent en fonction de self.direction_cible
        """
        self.direction = self.direction_cible # affecte à direction la valeur de direction_cible pour éviter les problèmes de direction
        (yActu, xActu) = (self.body[0][0],self.body[0][1]) # Définit les coordonnées actuelles de la tête du serpent sous les int xActu et yActu
        
        xNouv = xActu + self.direction[1] # Définit la nouvelle abscisse de tête du serpent en additionnant xActu et la valeur d'abscisse de direction
        if xNouv > nb_colonnes-1: # Cas où la nouvelle abscisse dépasse la dernière colonne par la droite: on "téléporte" la tête de l'autre côté
            xNouv = 0
        elif xNouv < 0 : # cas opposé où la nouvelle abscisse dépasse la première colonne par la gauche
            xNouv = nb_colonnes-1
        
        yNouv = yActu + self.direction[0] # Définit la nouvelle ordonnée de tête du serpent en additionnant yActu et la valeur d'ordonnée de direction
        if yNouv > nb_lignes-1: # Cas où la nouvelle ordonnée dépasse la dernière ligne par le bas: on "téléporte" la tête de l'autre côté
            yNouv = 0
        elif yNouv < 0 : # cas opposé où la nouvelle ordonnée dépasse la première ligne par le haut
            yNouv = nb_lignes-1
        
        return (yNouv, xNouv)
    
    def deplacer(self):
        """Méthode qui déplace l'ensemble des cellules constituant le snake vers leurs prochaines coordonnées
        """
        coordsPrec = self.body[0] #enregistre les coordonnées de la tête du serpent avant le déplacement
        (i_tete, j_tete) = self.acquerir_cible() #Donne à i et j les prochaines coordonnées de la tête du serpent
        
        self.body[0] = (i_tete, j_tete) # Donne à la tête du snake ses nouvelles coordonnées
        self.mat[i_tete][j_tete].valeur = 1 # Donne une valeur de 1 (snake) à la cellule au nouvel emplacement de la tête
        
        for cell in range(1, len(self.body)): # Donne leurs nouvelles coordonnées à chaque cellule de body, sauf la tête
            coordsPrec, self.body[cell] = self.body[cell], coordsPrec
            # intervertit les coordonnées de la variable coordsPrec avec les coordonnées de la cellule actuelle du serpent, afin de :
            # - donner à la cellule actuelle les coordonnées où se trouvait la cellule précédente avant son déplacement
            # - donner à la variable coordsPrec les coordonnées de la cellule actuelle, afin de les donner à la cellule suivante
            self.mat[self.body[cell][0]][self.body[cell][1]].valeur = 1 # Donne une valeur de 1 (snake) à la cellule au nouvel emplacement    
        
        self.mat[coordsPrec[0]][coordsPrec[1]].valeur = 0 # Donne une valeur de 0 (vide) à la cellule étant anciennement la queue du serpent
        self.mat[i_tete][j_tete].valeur = 1 # Donne une valeur de 1 (snake) à la cellule au nouvel emplacement de la tête, 
        # l'action est effectuée après le changement de la queue pour ne pas créer d'erreur dans le cas où le nouvel emplacement de la tête
        # est le même que l'ancien emplacement de la queue
        
        
    def manger(self):
        """Méthode qui déplace l'ensemble des cellules constituant le snake vers leurs prochaines coordonnées,
        et qui rallonge le snake en ajoutant un élément à la fin de la liste
        """
        # fonction appelée si la cellule cible de la tête à une valeur de 2 (pomme présente), analyse donnée par def tour_de_jeu
        ancien_dernier = self.body[-1] # on enregistre les coordonnées du dernier élément du snake
        self.deplacer()# deplacer le snake grâce à la première fonction
        self.body.append(ancien_dernier)# on lui ajoute un nouveau segment à sa queue (soit à l'ancien emplacement de la queue après déplacement)
        self.mat[self.body[0][0]][self.body[0][1]].valeur = 1 # redonne une valeur de 1 à la cellule à l'emplacement de la nouvelle queue
        generer_pomme(self.mat) # on génère une nouvelle pomme

        
class Cellule :
    def __init__(self, x, y):
        self.valeur = 0 # Cellule vide au départ
        self.pos = (x, y) # Position de la cellule en fonction de x et y
        self.rect = canevas.create_rectangle(x*taille_cellule,y*taille_cellule,(x*taille_cellule)+taille_cellule,(y*taille_cellule)+taille_cellule)
    
    def changer_couleur(self):
        """Méthode qui permet de changer la couleur de la cellule en l'élément qu'elle représente"""
        canevas.itemconfig(self.rect, fill = COULEURS[self.valeur])

def taille_fenetre_selon_grill(nbr_columns, nbr_lines, size_cell, fenetre):
    """Fonction qui règle la taille de la fenêtre selon les paramêtres de la grille"""
    x = nbr_columns*size_cell
    y=  nbr_lines*size_cell
    fenetre.geometry(str(x)+"x"+str(y))


def generer_pomme(matriceCellules):
    """Fonction qui génère une pomme à des coordonnées aléatoires de la grille, tant que ces coords pointent une case vide
    """
    coord=matriceCellules[randint(0, nb_lignes-1)][randint(0, nb_colonnes-1)]#générer coord aléatoire de pomme
    while coord.valeur!=0:
        coord=matriceCellules[randint(0, nb_lignes-1)][randint(0, nb_colonnes-1)]#modifie les coordonnées si elles sont sur une case non vide
    #afficher une pomme
    coord.valeur=2
    #la fonction manger() appelle la fonction generer pomme après le premier appel de celle ci
    #generer une nouvelle pomme dès que manger est appelé, ou des que aucune cellule a la valeur 2 (pomme présente)
    pass

def game_over(snake):
    score = len(snake.body)-3
    canevas.create_text(nb_colonnes*20,nb_lignes*20-50, text="GAME OVER", fill="black", font=('Comic Sans MS', 40))
    canevas.create_text(nb_colonnes*20,nb_lignes*20, text=f"Score : {score}", fill="black", font=('Century Gothic', 20))

def tour_de_jeu(snake):
    """Fonction qui analyse la case cible du snake après son acquisition par la fonction acquerir_cible, et déplace le snake selon les cas possibles
    """
    x_suite, y_suite = snake.acquerir_cible()
    #analyse la case cible trois cas possible
    val = matriceCellules[x_suite][y_suite].valeur
    if val == 0 :#la case est vide
        snake.deplacer() #le snake se déplace simplement
        dessiner_grille(matriceCellules)
        fenetre.after(500, tour_de_jeu, snake)
    elif val == 2 : #la case contient une pomme:
        snake.manger() #le snake se deplace avec la fonction manger qui ajoute un segment à son corps
        dessiner_grille(matriceCellules)
        fenetre.after(500, tour_de_jeu, snake)
    elif val == 1 :#la case contient un segment du corps du snake:
        game_over(snake)

def dessiner_grille(matriceCellules):
    """Fonction qui s'occupe de mettre à jour la grille et les elements qu'elle contient
    """
    for ligne in matriceCellules :
        for cell in ligne :
            cell.changer_couleur() # appel de la méthode changer_couleur, qui s'occupe de changer la couleur de la cellule en fonction de a valeur

"""Programme Principal"""
fenetre=Tk() #instance de Tk comme fenetre
fenetre.title("Snake !")


nb_colonnes=30 #paramètres de la taille de la fenetre selon les paramêtres de la matrice cellule
nb_lignes=20
taille_cellule=40
taille_fenetre_selon_grill(nb_colonnes, nb_lignes, taille_cellule, fenetre) #réglage de la taille de la fenetre 
fenetre.resizable(0,0)

COULEURS = ["white","green","red"]
canevas = Canvas()
canevas.pack(expand = True, fill = "both")

matriceCellules = [[Cellule(x, y) for x in range(nb_colonnes)] for y in range(nb_lignes)] # Matrice des cellules définissant l'espace de jeu
python=Snake(matriceCellules)#instance de la classe snake dans la matrice de cellules
generer_pomme(matriceCellules)#premier appel de la fonction generer_pomme

fenetre.bind("<Left>", lambda event: python.changer_direction(event)) #binding des touches directionnelles pour faire changer de direction
fenetre.bind("<Right>", lambda event: python.changer_direction(event)) #le snake
fenetre.bind("<Up>", lambda event: python.changer_direction(event))
fenetre.bind("<Down>", lambda event: python.changer_direction(event))

tour_de_jeu(python)

fenetre.mainloop()