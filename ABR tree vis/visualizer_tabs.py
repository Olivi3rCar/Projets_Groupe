from tkinter import *

class VisualizerEditTab:
    def __init__(self,visualizer,x=20,y=5):#20,5
        self.visualizer=visualizer
        
        frame=Frame()
        frame.configure(borderwidth=1,highlightcolor="black")
        frame.place(x=x,y=y,width=200,height=100)
        self.frame=frame
        
        self.add_label=Label()
        self.del_label=Label()
        self.add_entry=Entry()
        self.del_entry=Entry()
        self.add_button=Button()
        self.del_button=Button()

class VisualizerInfoTab:
    def __init__(self,visualizer,x=580,y=5):#580,5
        self.visualizer=visualizer
        
        frame=Frame()
        frame.configure(borderwidth=1,border=True)
        frame.place(x=x,y=y,width=200,height=100)
        self.frame=frame
        
        size=Label()
        size.place(x=x,y=5,width=190,height=15)
        depth=Label()
        depth.place(x=x,y=35,width=190,height=15)
        leaf=Label()
        leaf.place(x=x,y=65,width=190,height=15)
        
        self.size_label=size
        self.depth_label=depth
        self.leaf_label=leaf
        
class VisualizerCommandTab:
    def __init__(self,visualizer,x=18,y=510):
        self.visu = visualizer
        
        frame=Frame()
        frame.configure(borderwidth=1,highlightcolor="black")
        frame.place(x=x,y=y,width=764,height=80)
        self.frame=frame
        
        self.output_entry = Entry()
        
        self.nouveau = Button(self.visu.window, "Nouveau",
                            command = self.visu.resetTree)
        self.infixe = Button(self.visu.window, "Infixe",
                            command = self.visu.infixe)
        self.prefixe = Button(self.visu.window, "Prefixe",
                            command = self.visu.prefixe)
        self.postfixe = Button(self.visu.window, "Postfixe",
                            command = self.visu.postfixe)
        self.largeur = Button(self.visu.window, "Largeur",
                            command = self.visu.largeur)
        self.export = Button(self.visu.window, "Exporter",
                            command = self.visu.export)
        self.reduire = Button(self.visu.window, "Réduire",
                            self.visu.opti)