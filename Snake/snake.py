from tkinter import *

class Snake:
    def __init__(self,grille, cell_centrale):
        self.body=[(),(),()]#liste de couples représentant le corps du snake 
        self.direction=(0,-1)#gauche au départ, change plus tard selon les inputs du joueur
        pass
    
    def changer_direction(self,event):
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
        
    def acquerir_cible(self,nb_lignes,nb_colonnes):
        pass
    
    def deplacer(self,grille,i_tete,j_tete):
        pass
    
    def manger(self,grille,i_tete,j_tete):
        pass
        
class Cellule :
    def __init__(self, x, y):
        self.valeur = 0 # Cellule vide au départ
        self.pos = (x, y) # Position de la cellule en fonction de x et y


def taille_fenetre_selon_grill(nbr_columns, nbr_lines, size_cell):
    """Méthode qui règle la taille de la fenêtre selon les paramêtres de la grille"""
    x=nbr_columns*size_cell
    y=nbr_lines*size_cell
    fenetre.geometry(str(x)+"x"+str(y))

"""Programme Principal"""
fenetre=Tk()#instance de Tk comme fenetre
fenetre.title("Snake !")

nb_colonnes=30#paramêtres de la taille de la fenetre selon les paramêtres de la grille 
nb_lignes=20
taille_cellule=40

taille_fenetre_selon_grill(nb_colonnes,nb_lignes,taille_cellule)#réglage de la taille de la fenetre 
fenetre.resizable(0,0)

fenetre.bind("<Left>", lambda event: Snake.changer_direction(event))#binding des touches directionnelles pour faire changer de direction
fenetre.bind("<Right>",lambda event: Snake.changer_direction(event))#le snake
fenetre.bind("<Up>",lambda event: Snake.changer_direction(event))
fenetre.bind("<Down>",lambda event: Snake.changer_direction(event))

fenetre.mainloop()