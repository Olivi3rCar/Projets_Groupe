from tkinter import *

class Cellule :
    def __init__(self, x, y):
        self.valeur = 0 # Cellule vide au départ
        self.pos = (x, y) # Position de la 

fenetre=Tk()
fenetre.geometry("1200x800")
fenetre.resizable(0,0)

fenetre.mainloop()