from tkinter import *
from BinarySearchTreeVisualizer import *

class VisualizerEditTab:
    def __init__(self,visualizer,x=20,y=5):#20,5
        self.vizualiser=visualizer
        
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
        self.vizualiser=visualizer
        
        frame=Frame()
        frame.configure(borderwidth=1,highlightcolor="black")
        frame.place(x=x,y=y,width=200,height=100)
        self.frame=frame
        
        size=Label()
        size.place(anchor=self.Frame,x=10,y=5,width=190,height=15)
        depth=Label()
        depth.place(anchor=self.Frame,x=10,y=35,width=190,height=15)
        leaf=Label()
        leaf.place(anchor=self.Frame,x=10,y=65,width=190,height=15)
        
        self.size_label=size
        self.depth_label=depth
        self.leaf_label=leaf
        
class VisualizerCommandTab:
    def __init__(self,x=18,y=510):#18,510
        pass