from tkinter import *

def taille_fenetre_selon_grill(nbr_columns, nbr_lines, size_cell):
    x=nbr_columns*size_cell
    y=nbr_lines*size_cell
    fenetre.geometry(str(x)+"x"+str(y))
fenetre=Tk()
creer_grille(20,15,20)
fenetre.mainloop()

def resized():
    #can you detect when you are resized ? or need an after (x time)
    #check size with cget, check cells max that fit
    #check if what length remaining is greater or inferior to half of size cell, if greater add one more cell
    pass