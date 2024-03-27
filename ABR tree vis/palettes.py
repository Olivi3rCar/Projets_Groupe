from tkinter import *

LAPALETTE = None

class Tibouton:
    def __init__(self, k, pal, fenetre):
        self.fenetre = fenetre
        self.frame = Frame(bg= pal["Fond"]) 
        self.bouton = Button(bg= pal["Clar"], activebackground=pal["Fonc"],
                             fg= pal["Fonc"], activeforeground=pal["Clar"],
                             font= ("Arial", 20), text= pal["Titre"],
                             command= self.getit)
        self.frame.place(x = 25, y = k, width = 250, height = 90)
        self.bouton.place(x = 30, y = k+5, width = 240, height = 80)
        self.palette = pal
    
    def getit(self):
        global LAPALETTE
        LAPALETTE = self.palette
        self.fenetre.destroy()
        
        
     
paletteBase = {
    "Titre": "Basique",
    "Fond" : "gray",
    "Clar" : "light gray",
    "Fonc" : "gray18",
    "txt" : "black"
}   

paletteBleu = {
    "Titre": "Myrtille",
    "Fond" : "Dodger Blue",
    "Clar" : "LightBlue1",
    "Fonc" : "Navy",
    "txt" : "LightBlue1"
}

paletteRouge = {
    "Titre": "Cerise",
    "Fond" : "red",
    "Clar" : "RosyBrown2",
    "Fonc" : "red4",
    "txt" : "white"
}

paletteOlive = {
    "Titre": "Olive",
    "Fond" : "OliveDrab2",
    "Clar" : "DarkOliveGreen1",
    "Fonc" : "dark olive green",
    "txt" : "dark olive green"
}

paletteJaune = {
    "Titre": "Citron",
    "Fond" : "yellow",
    "Clar" : "lemon chiffon",
    "Fonc" : "yellow4",
    "txt" : "yellow4"
}


PALETTES = [paletteBase, paletteBleu, paletteRouge, paletteOlive, paletteJaune]

def choix_couleurs(palettes):
    fenetre = Tk()
    fenetre.geometry("300x600")
    fenetre.title("Choix de l'interface")
    fenetre.resizable(0, 0)
    
    titre = Label(font=("Arial", 15), text="Choisissez Votre Couleur !")
    titre.place(x = 0, y = 10, width=300, height=30)
    
    k = 60
    for i in palettes :
        Tibouton(k, i, fenetre)
        k += 100
    fenetre.mainloop()
    global LAPALETTE, paletteBase
    if LAPALETTE == None :
        return paletteBase
    return LAPALETTE