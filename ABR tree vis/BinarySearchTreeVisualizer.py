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
        self.window=window#initalisation de la fenetre
        
        canevas=Canvas()
        canevas.place(x=0,y=120,width=800,height=400)
        canevas.configure(bg="white",bd=0, highlightthickness=0)
        self.canevas=canevas#initialisation du canvas
        self.tree=BinarySearchTree()#instancialisation de l'arbre (d'abord vide)
        
        
        self.window.mainloop()
        
    def draw(self,x=400,y=15,depth=1):
        """Methode qui dessine recursivement l'arbre binaire de recherche

        Args:
            tree (BinarySearchTree): arbre binaire de recherche a representer
            x (int): coord x du centre. Defaults to 400.
            y (int): coord y du centre. Defaults to 15.
            depth (int, optional): hauteur actuelle. Defaults to 1.
        """
        if depth==1: #on dessine d'abord pour la racine originelle, sert a ne pas dessiner de branche qui relie la racine originelle a rien
            if self.tree.root==None:#cas de racine originelle vide
                return
            else:#cas de la racine orirginelle non vide, affichage du premier noeud
                racine=self.canevas.create_oval(x-11,y-11,x+11,y+11,fill="grey")
                self.canevas.create_text(x,y,text=str(self.tree.root))#creer un text qui a la valeur du noeud à afficher
                self.tree.left.draw(x=0,y=0,depth=depth+1)#rappel sur sous arbre gauche (possiblement vide)
                self.tree.right.draw(x=0,y=0,depth=depth+1)#rappel sur sous arbre droit (possiblement vide)
                
        if depth>1 and depth<=6:#on dessine pour le reste des noeuds (diff hauteur) si hauteur inferieure a 6
            if self.tree.root==None:#cas du noeud vide
                return
            else:#cas de noeud non vide (peut etre feuille)
                #check si on est dans un sous arbre droit ou dans un sous arbre gauche (vérifie dans quel sens on décale un noeud donné par rapport à son parent): 
                self.canevas.create_line(x,y,x+0,y-70)#dessine la branche qui relie le noeud à son parent (modif troisieme arg selon décalage par rapport au parent)
                noeud=self.canevas.create_oval(x-11,y-11,x+11,y+11,fill="grey")#creer un noeud
                self.canevas.create_text(x,y,text=str(self.tree.root))#creer un text qui a la valeur du noeud à afficher
                self.tree.left.draw(x=0,y=0,depth=depth+1)#rappel sur sous arbre gauche
                self.tree.right.draw(x=0,y=0,depth=depth+1)#rappel sur sous arbre droit
            
        """
        coordonnee_centre = x, y
        centre_x=x 
        centre_y=y
        """
        """self.branche= self.canevas.create_line(self.centre_x, self.centre_y, self.fils_gauche_x, self.fils_droite_y)
        self.noeuds =self.canevas.create_oval((self.centre_x - self.noeuds,
                                          self.centre_y - self.noeuds, 
                                          self.centre_x + self.noeuds,
                                          self.centre_y + self.noeuds), fill ="gray")
        self.value = self.canevas.create_text(self.centre_x, self.centre_y, tex(tree.value))
        if tree.left != None:
            pass
        if tree.right != None:
            pass"""
    
    def update(self):
        """Methode qui met a jour le canvas et l'onglet info_tab
        """
        self.canevas.delete()
        self.draw()
        self.info_tab.update()
        
        
arbre_test=BinarySearchTree()
arbre_test.insert(valeur)
eh=BinarySearchTreeVisualizer()