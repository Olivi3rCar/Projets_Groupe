from tkinter import *
from BinarySearchTree import *
from visualizer_tabs import *


class BinarySearchTreeVisualizer :
    def __init__(self):
        """Constructeur de la classe BinarySearchTreeVisualizer
        """
        window=Tk()
        window.geometry("800x600")
        window.configure(bg=LIGHT)
        window.resizable(0,0)
        self.window=window#initalisation de la fenetre
        
        canevas=Canvas()
        canevas.place(x=0,y=120,width=800,height=400)
        canevas.configure(bg=LIGHT,bd=0, highlightthickness=0)
        self.canevas=canevas#initialisation du canvas
        
        arbre_test=BinarySearchTree()
        
        self.tree=arbre_test#instancialisation de l'arbre (d'abord vide)(ici code en dur)
        self.draw()
        self.info = VisualizerInfoTab(self)
        self.command = VisualizerCommandTab(self)
        self.edit = VisualizerEditTab(self)
        self.update()
        
        self.window.mainloop()
        
    def draw(self,tree=None,x=400,y=15,depth=1):
        """Methode qui dessine recursivement l'arbre binaire de recherche

        Args:
            tree (BinarySearchTree): arbre binaire de recherche a representer
            x (int): coord x du centre. Defaults to 400.
            y (int): coord y du centre. Defaults to 15.
            depth (int, optional): hauteur actuelle. Defaults to 1.
        """
        if tree == None: # cas où la racine actuelle est la plus haute, on def tree comme l'ABR self.tree
            tree = self.tree
        if tree.root==None:#cas de racine vide
            return
        else:#cas de la racine  non vide, affichage du noeud actuel
            if tree.left != None and tree.left.root != None: # cas où le SAG existe : on trace une ligne et on appelle la fonction pour le SAG
                xG,yG=x-(6*(2**(6-depth))),y+70 #calcul des coords du noeud su SAG
                brancheG = self.canevas.create_line(x, y, xG, yG)#dessin de la branche qui relie la racine et le SAG
                self.draw(tree.left,xG,yG,depth+1)#rappel sur sous arbre gauche
            if tree.right != None and tree.right.root != None : # cas où le SAD existe : on trace une ligne et on appelle la fonction pour le SAD
                xD,yD=x+(6*(2**(6-depth))),y+70 #calcul des coords du noeud su SAD
                brancheD = self.canevas.create_line(x, y, xD, yD)#dessin de la branche qui relie la racine et le SAG
                self.draw(tree.right,xD,yD,depth+1)#rappel sur sous arbre droit (possiblement vide)
            racine=self.canevas.create_oval(x-11,y-11,x+11,y+11,fill=DARK)# dessine le cercle correspondant au noeud
            self.canevas.create_text(x,y,text=str(tree.root), fill="white")#creer un text qui a la valeur du noeud à afficher
            # le noeud est dessiné en dernier afin d'éviter des problèmes au niveau de quel élément se retrouve au premier plan,
            # le noeud est forcément dessiné par dessus les branches si elles existent
            
    
    def resetTree(self) :
        self.command.output_entry.delete(0,END)#on efface la valeur dans Entry
        self.tree = BinarySearchTree()
        self.update()
    
    def infixe(self):
        self.command.output_entry.delete(0,END)#on efface la valeur dans Entry
        liste = self.tree.infixe()
        self.command.output_entry.insert(0, ",".join(liste))
    
    def prefixe(self):
        self.command.output_entry.delete(0,END)#on efface la valeur dans Entry
        liste = self.tree.prefixe()
        self.command.output_entry.insert(0, ",".join(liste))
        
    def postfixe(self):
        self.command.output_entry.delete(0,END)#on efface la valeur dans Entry
        liste = self.tree.postfixe()
        self.command.output_entry.insert(0, ",".join(liste))
    
    def largeur(self):
        self.command.output_entry.delete(0,END)#on efface la valeur dans Entry
        liste = self.tree.parcours_largeur()
        self.command.output_entry.insert(0, ",".join(liste))
    
    def export(self):
        self.command.output_entry.delete(0,END)#on efface la valeur dans Entry
        tup = self.tree.sous_forme_de_tuples_imbriqués()
        self.command.output_entry.insert(0, str(tup))
    
    def opti(self):
        self.command.output_entry.delete(0,END)#on efface la valeur dans Entry
        self.tree.optimized()
        self.update()
    
    def update(self):
        """Methode qui met a jour le canvas et l'onglet info_tab
        """
        self.canevas.delete('all')
        self.draw()
        self.info.update(self.tree)
    

arbre = BinarySearchTreeVisualizer()