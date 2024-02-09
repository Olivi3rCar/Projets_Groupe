class BinarySearchTree:
    def __init__(self):
        """Constructeur de la classe BinarySearchTree 
        """
        self.root=None
        self.left=None
        self.right=None
        
    def __contains__(self, val):
        if self.root == None:
            return False
        if self.root == val :
            return True
        elif self.root > val :
            return val in self.right
        else :
            return val in self.left
    
    def insert(self,valeur,depth=1):
        """Méthode qui insère une valeur passee en argument si la hauteur maximale de 6 n'est pas depassee 

        Args:
            valeur (int): valeur à inserer 
            depth (int, optional): hauteur. Defaults to 1.
        """
        if depth<=6 and valeur not in self and valeur in range(0,100): #vérifications nécessaires :
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