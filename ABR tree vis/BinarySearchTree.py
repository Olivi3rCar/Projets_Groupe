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
        assert 0<=valeur<100 , "Valeur invalide entrée"
        assert valeur not in self, "Valeur déjà presente"
        assert depth <= 6, "Arbre trop grand pour entrer cette valeur :(" 
        #vérifications nécessaires :
        # la hauteur de l'arbre n'est pas supérieure à 6
        # la valeur n'est pas déjà présente dans l'arbre
        # la valeur est comprise entre 0 et 99 inclus
        if self.root==None:#cas d'un arbre vide
            self.root=valeur
            self.left=BinarySearchTree()
            self.right=BinarySearchTree()
        elif valeur<self.root:#cas ce la valeur à inserer plus petite que la racine
            self.left.insert(valeur, depth+1)
        elif valeur>self.root:#cas de la valeur à inserer plus grande que la racine
            self.right.insert(valeur,depth+1)
    
    def supprimer(self,val):
        #exploration de l'arbre jusqua val
        if self.root==None:
            return None
        if self.root>val:
            if self.left==None:
                self.left=BinarySearchTree()
            self.left =self.left.supprimer(val)
        if self.root<val:
            if self.right==None:
                self.right=BinarySearchTree()
            self.right=self.right.supprimer(val)
        
        if self.root==val:
            if self.left.root==None and self.right.root==None:#cas de la feuille
                return None
            elif self.left.root==None:#cas d'un seul sous arbre
                return self.right
            elif self.right.root==None:#cas d'un seul sous arbre
                return self.left
            else:
                self.root=self.right.min()#cas de deux sous arbre 
                self.right=self.right.supprimer(self.root)
        return self
    
    def min(self):
        if self.left!=None and self.left.root!=None:
                return self.left.min()
        else:
            return self.root
    
    def size(self):
        if self.root==None and self.right==None and self.left==None:
            return 0
        somme = 1
        if type(self.left) is BinarySearchTree :
            somme += self.left.size()
        if type(self.right) is BinarySearchTree :
            somme += self.right.size()
        return somme
    
    
    def depth(self):
        if self.root==None:
            return 0
        dsag, dsad = 0, 0
        if type(self.left) is BinarySearchTree :
            dsag = self.left.depth()
        if type(self.right) is BinarySearchTree :
            dsad = self.right.depth()
        return 1+max(dsag,dsad)
    
    def leaves(self):
        if self.root==None:
            return 0
        lsag, lsad = 0, 0
        if type(self.left) is BinarySearchTree :
            lsag = self.left.leaves()
        if type(self.right) is BinarySearchTree :
            lsad = self.right.leaves()
        if lsad == 0 and lsag == 0 :
            return 1
        return lsag + lsad

    def infixe(self, infi = None):
        if infi==None:
            infi=[]
        if self.root!=None:
            self.left.infixe(infi)
            infi.append(str(self.root))
            self.right.infixe(infi)
        return infi
    
    def prefixe(self, pre = None):
        if pre==None:
            pre=[]
        if self.root!=None:
            pre.append(str(self.root))
            self.left.prefixe(pre)
            self.right.prefixe(pre)
        return pre
    
    def postfixe(self, post = None):
        if post==None:
            post=[]
        if self.root!=None:
            self.left.postfixe(post)
            self.right.postfixe(post)
            post.append(str(self.root))
        return post
    
    def parcours_largeur(self) :
        if self.root==None:#si l'arbre est vide renvoyer liste vide
            return []
        noeuds=[]#créer listes noeud =[]
        niveau_actu=[self]#creer listes niveau actuel=[arbre]
        while niveau_actu!=[]:#tant que niveau actuel non vide:
            niveau_suivant=[]#construire le niveau suivant, creer une liste vide niveau suivant
            for arbre in niveau_actu:#parcours pour chaque noeud de niveau actuel:
                noeuds.append(str(arbre.root))#ajouter sa valeur dans listes noeud 
                if arbre.left!=None and arbre.left.root!=None:
                    niveau_suivant.append(arbre.left)#ajouter ses éventuels fils gauche et fils droit dans niveau suivant
                if arbre.right!=None and arbre.left.root!=None :
                    niveau_suivant.append(arbre.right)
            niveau_actu=niveau_suivant#remplacer niveau actuel par niveau suivant 
        return noeuds 

    def sous_forme_de_tuples_imbriqués(self):
        if self.root == None :
            return ()
        return (self.root, self.left.sous_forme_de_tuples_imbriqués(),
                self.right.sous_forme_de_tuples_imbriqués())
        
    def optimized(self, values = None):
        if values == None :
            values = self.infixe()
            self.root, self.left, self.right = None, None, None
            self.optimized(values)
        elif len(values)<=0:
            return
        else :
            m = int(values.pop(len(values)//2))
            self.insert(m)
            self.optimized(values[:len(values)//2])
            self.optimized(values[len(values)//2:])