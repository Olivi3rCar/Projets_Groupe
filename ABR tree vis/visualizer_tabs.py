from tkinter import *
from BinarySearchTree import *
from palettes import *

""" Choix des couleurs via ColorPalettes.py """
cols = choix_couleurs(PALETTES)
LIGHT = cols["Clar"]
MID = cols["Fond"]
DARK = cols["Fonc"]
TXT = cols["txt"]

class VisualizerEditTab:
    def __init__(self,visualizer,x=20,y=5):#20,5
        self.visualizer=visualizer
        
        frame=Frame()
        frame.configure(borderwidth=1,highlightcolor="black", background=MID)
        frame.place(x=x,y=y,width=200,height=100)
        self.frame=frame
        
        add_label=Label(frame,text="Ajouter valeur :",
                        background=MID, foreground=TXT)
        add_label.place(x=10,y=15,width=90,height=15)
        add_entry=Entry(frame)
        add_entry.place(x=110,y=15,width=30,height=15)
        add_button=Button(frame,text="OK",command=self.on_add, 
                       relief= "flat", bg= DARK, activebackground= LIGHT,
                        fg= LIGHT, activeforeground= DARK)
        add_button.place(x=160,y=15,width=20,height=15)

        del_label=Label(frame,text="Enlever valeur :",
                        background=MID, foreground=TXT)
        del_label.place(x=10,y=60,width=90,height=15)
        del_entry=Entry(frame)
        del_entry.place(x=110,y=60,width=30,height=15)
        del_button=Button(frame,text="OK", command=self.on_del, 
                       relief= "flat", bg= DARK, activebackground= LIGHT,
                        fg= LIGHT, activeforeground= DARK)
        del_button.place(x=160,y=60,width=20,height=15)



        self.add_label=add_label
        self.del_label=del_label
        self.add_entry=add_entry
        self.del_entry=del_entry
        self.add_button=add_button
        self.del_button=del_button

    def on_add(self):
        value=self.add_entry.get()#on récupère valeur entrée dans Entry
        assert value != '', "Valeur vide entrée"
        value = int(value)
        self.visualizer.tree.insert(value)#on insert dans l'arbre
        self.visualizer.update()#on met tout à jour
        self.add_entry.delete(0,END)#on efface la valeur dans Entry
        print ("Hello World")

    def on_del(self):
        value=self.del_entry.get()#on récupère valeur entrée dans 
        assert value != '', "Valeur vide entrée"
        value = int(value)
        self.visualizer.tree.supprimer(value)#on retirer de l'arbre
        self.visualizer.update()#on met tout à jour
        self.del_entry.delete(0,END)#on efface la valeur dans Entry
        print("Goodbye World")

class VisualizerInfoTab:
    def __init__(self,visualizer,x=580,y=5):#580,5
        self.visualizer=visualizer
        
        frame=Frame()
        frame.configure(borderwidth=1,border=True,background=MID)
        frame.place(x=x,y=y,width=200,height=100)
        self.frame=frame
        
        size=Label(frame,text="Taille de l'arbre : 0",anchor="w",
                        background=MID, foreground=TXT)
        size.place(x=10,y=10,width=190,height=15)
        depth=Label(frame,text="Hauteur de l'arbre : 0",anchor="w",
                        background=MID, foreground=TXT)
        depth.place(x=10,y=40,width=190,height=15)
        leaf=Label(frame,text="Nombre de feuilles : 0",anchor="w",
                        background=MID, foreground=TXT)
        leaf.place(x=10,y=70,width=190,height=15)
        
        self.size_label=size
        self.depth_label=depth
        self.leaf_label=leaf
        
    def update(self,arbre):
        self.size_label.configure(text="Taille de l'arbre : "+str(arbre.size()))
        self.depth_label.configure(text="Hauteur de l'arbre : "+str(arbre.depth()))
        self.leaf_label.configure(text="Nombres de feuilles : "+str(arbre.leaves()))


        
class VisualizerCommandTab:
    def __init__(self,visualizer,x=18,y=510):
        self.visu = visualizer
        
        frame=Frame()
        frame.configure(borderwidth=1,highlightcolor="black", background=MID)
        frame.place(x=x,y=y,width=764,height=80)
        self.frame=frame
        
        output=Entry(frame)
        output.place(x=10,y=55,width=744,height=15)
        self.output_entry = output


        nouveau=Button(frame,text="Nouveau",command = self.visu.resetTree, 
                       relief= "flat", bg= DARK, activebackground= LIGHT,
                        fg= LIGHT, activeforeground= DARK)
        nouveau.place(x=10,y=10,width=82,height=25)
        
        infixe=Button(frame,text="Infixe",command = self.visu.infixe, 
                       relief= "flat", bg= DARK, activebackground= LIGHT,
                        fg= LIGHT, activeforeground= DARK)
        infixe.place(x=120,y=10,width=82,height=25)
        
        prefixe=Button(frame,text="Préfixe",command = self.visu.prefixe, 
                       relief= "flat", bg= DARK, activebackground= LIGHT,
                        fg= LIGHT, activeforeground= DARK)
        prefixe.place(x=230,y=10,width=82,height=25)
        
        postfixe=Button(frame,text="Postfixe",command = self.visu.postfixe, 
                       relief= "flat", bg= DARK, activebackground= LIGHT,
                        fg= LIGHT, activeforeground= DARK)
        postfixe.place(x=340,y=10,width=82,height=25)
        
        largeur=Button(frame,text="Largeur",command = self.visu.largeur, 
                       relief= "flat", bg= DARK, activebackground= LIGHT,
                        fg= LIGHT, activeforeground= DARK)
        largeur.place(x=450,y=10,width=82,height=25)
        
        export=Button(frame,text="Exporter",command = self.visu.export, 
                       relief= "flat", bg= DARK, activebackground= LIGHT,
                        fg= LIGHT, activeforeground= DARK)
        export.place(x=560,y=10,width=82,height=25)
        
        reduire=Button(frame,text="Réduire",command=self.visu.opti, 
                       relief= "flat", bg= DARK, activebackground= LIGHT,
                        fg= LIGHT, activeforeground= DARK)
        reduire.place(x=670,y=10,width=82,height=25)

        self.nouveau_button = nouveau 
        self.infixe_button = infixe
        self.prefixe_button = prefixe
        self.postfixe_button = postfixe
        self.largeur_button = largeur
        self.export_button = export
        self.reduire_button = reduire
