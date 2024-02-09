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
        
    def draw(self):
        pass
    
    def update(self):
        pass
        
eh=BinarySearchTreeVisualizer()