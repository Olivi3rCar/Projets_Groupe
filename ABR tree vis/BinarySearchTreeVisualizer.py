from tkinter import *
from BinarySearchTree import *

class BinarySearchTreeVisualizer :
    def __init__(self):
        """Constructeur de la classe BinarySearchTreeVisualizer
        """
        window=Tk()
        window.geometry("800x600")
        window.configure(bg="white")
        window.resizable(0,0)
        self.window=window
        
        canevas=Canvas()
        canevas.place(x=0,y=120,width=800,height=400)
        canevas.configure(bg="white",bd=0, highlightthickness=0)
        self.canevas=canevas
        self.tree=BinarySearchTree()
        
        
        self.window.mainloop()
        
    def draw(self, tree, x, y, depth=1):
        self.tree = tree
        self.coordonnee_centre = x, Y
        self.centre_x =x 
        self.centre_y = y
        self.branche= canevas.create_line(self.centre_x, self.centre_y, self.fils_gauche_x, self.fils_droite_y)
        self.noeuds =canevas.create_oval((self.centre_x - self.noeuds,
                                          self.centre_y - self.noeuds, 
                                          self.centre_x + self.noeuds,
                                          self.centre_y + self.noeuds), fill ="gray")
        self.value = canevas.create_text(self.centre_x, self.centre_y, tex(tree.value))
        if fils_gauche != None:
        pass
        if fils_droite != None:
            pass
    
    def update(self):
        self.canevas.delete()
        self.draw()
        self.info_tab.update()
        
eh=BinarySearchTreeVisualizer()