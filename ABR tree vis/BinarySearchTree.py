class BinarySearchTree:
    def __init__(self):
        """Constructeur de la classe BinarySearchTree 
        """
        self.root=None
        self.left=None
        self.right=None
        
    def __repr__(self,lst=None):
        if lst==None:
            lst=[]
        if self.root==None:
            return str(lst)
        if self.left!=None:
            self.left.__repr__(lst)
        lst.append(self.root)
        if self.right!=None:
            self.right.__repr__(lst)
        return str(lst)    
    
    def __contains__(self, val):
        """Methode surchargeant "in" pour verifier si une valeur passee en argument est presente dans self

        Args:
            val (int): valeur cible dont on vérifie la presence
        Returns:
            bool: -
        """
        if self.root == None:
            return False
        if self.root > val :
            if self.right==None:
                self.right=BinarySearchTree()
            self.right.__contains__(val)
        elif self.root<val :
            if self.left==None:
                self.left=BinarySearchTree()
            self.left.__contains__(val)
        else:
            return True
    
    def insert(self,valeur,depth=1):
        """Méthode qui insère une valeur passee en argument si la hauteur maximale de 6 n'est pas depassee 

        Args:
            valeur (int): valeur à inserer 
            depth (int, optional): hauteur. Defaults to 1.
        """
        assert 0<=valeur<100 , "valeur invalide entree"
        assert valeur not in self, "valeur deja presente"
        if depth<=6 : #vérifications nécessaires :
            # la hauteur de l'arbre n'est pas supérieure à 6
            # la valeur n'est pas déjà présente dans l'arbre
            # la valeur est comprise entre 0 et 99 inclus
            if self.root==None:#cas d'un arbre vide
                self.root=valeur
                self.left=BinarySearchTree()
                self.rigth=BinarySearchTree()
            elif valeur<self.root:#cas ce la valeur à inserer plus petite que la racine
                self.left.insert(valeur, depth+1)
            elif valeur>self.root:#cas de la valeur à inserer plus grande que la racine
                self.right.insert(valeur,depth+1)
                
    def size(self):
        if self.root==None:
            return 0
        return 1+self.left.size()+self.right.size()
    
    
    def depth(self):
        if self.root==None:
            return 0
        return 1+max(self.left.size(),self.right.size())
    
    def leaves(self):
        if self.root==None:
            return 0
        else:
            if self.left==BinarySearchTree() and self.right==BinarySearchTree():
                return 1
            else:
                return self.left.leaves()+self.right.leaves()
    
  