import tkinter as tk
from . import cs

class CoordControlPanel:
    def __init__(self, root, name:str, axs, controller=None):
        
        self.frame = tk.Frame(root, borderwidth=1, relief='groove', padx=3, pady=3)
        
        self.label = tk.Label(self.frame, text=name)
        
        self.canvas = tk.Canvas(self.frame, borderwidth=5, relief='sunken')
        self.CSystem:cs.CoordSystem = cs.CoordSystem(self.canvas, axs[0], axs[1])
    
        self.button_right = tk.Button(self.frame, text="->", command=self.on_button_right)
        self.button_left = tk.Button(self.frame, text="<-", command=self.on_button_left)
        self.button_up = tk.Button(self.frame, text="+", command=self.on_button_up)
        self.button_down = tk.Button(self.frame, text="-", command=self.on_button_down)
        
        self.controller = controller
        
    def on_button_right(self):
        self.CSystem.update_direction(5)
        if self.controller:
            self.controller.move()
    def on_button_left(self):
        self.CSystem.update_direction(-5)
        if self.controller:
            self.controller.move()
    def on_button_up(self):
        self.CSystem.update_outline(5)
        if self.controller:
            self.controller.move()
    def on_button_down(self):
        self.CSystem.update_outline(-5)
        if self.controller:
            self.controller.move()
        
    def add(self):
        self.label.grid(row = 0, columnspan=4)
        self.canvas.grid(row=1, columnspan=4)
        self.button_left.grid(row=2, column=0)
        self.button_up.grid(row=2, column=1)
        self.button_down.grid(row=2, column=2)
        self.button_right.grid(row=2, column=3)