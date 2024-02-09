class BinarySearchTree:
    def __init__(self):
        """Constructeur de la classe BinarySearchTree 
        """
        self.root=None
        self.left=None
        self.right=None
        
    def insert(self,valeur,depth=1):
        """Méthode qui insère une valeur passee en argument si la hauteur maximale de 6 n'est pas depassee 

        Args:
            valeur (int): valeur à inserer 
            depth (int, optional): hauteur. Defaults to 1.
        """
        if depth>=6: #vérifie que la hauteur max n'est pas depasse 
            if self.root==None:#cas d'un arbre vide
                self.root=valeur
                self.left=BinarySearchTree()
                self.rigth=BinarySearchTree()
            elif valeur<self.root:#cas ce la valeur à inserer plus petite que la racine
                self.left.insert(valeur, depth+1)
            elif valeur>self.root:#cas de la valeur à inserer plus grande que la racine
                self.right.insert(valeur,depth+1)