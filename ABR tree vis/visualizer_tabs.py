from tkinter import *
from BinarySearchTreeVisualizer import *

class VisualizerEditTab:
    def __init__(self,):
        self.vizualiser=BinarySearchTreeVisualizer()
        
        frame=Frame()
        frame.configure(borderwidth=1,highlightcolor="black")
        self.frame=Frame()
        
        self.add_label=Label()
        self.del_label=Label()
        self.add_entry=Entry()
        self.del_entry=Entry()
        self.add_button=Button()
        self.del_button=Button()

class VisualizerInfoTab:
    def __init__(self):
        self.vizualiser=BinarySearchTreeVisualizer()
        self.frame=Frame()
        self.size_label=Label(self.frame)
        self.depth_label=Label(self.frame)
        self.leaf_label=Label(self.frame)
        
class VisualizerCommandTab:
    def __init__(self):
        pass