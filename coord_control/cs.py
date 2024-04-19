import coord_control.settings_cs as settings_cs
import math
import tkinter as tk

class CoordSystem():
    canvas:tk.Canvas = None
    zoom = settings_cs.zoom
    coord_margin = settings_cs.coord_margin * zoom
    max_size = settings_cs.max_size * zoom + coord_margin
    coord_size = settings_cs.max_size * zoom
    coord_originX = coord_size / 2 + coord_margin
    coord_originY = coord_size / 2 + coord_margin
    
    
    def __init__(self, input_canvas, axs1, axs2):
        self.axs1 = axs1
        self.axs1.register(self)
        self.axs2 = axs2
        self.axs2.register(self)
        self.canvas = input_canvas
        self.setup()
    
    def setup(self):
        self.canvas.config(width=self.max_size, height=self.max_size)
    #create_coord_system
        #x-axis
        self.x_axs = self.canvas.create_line(
            self.coord_margin, 
            self.coord_originY, 
            self.coord_size + self.coord_margin, 
            self.coord_originY,
            fill="lightgrey",
            dash=(2,2))
        #y-axis
        self.y_axs = self.canvas.create_line(
            self.coord_originX, 
            self.coord_margin, 
            self.coord_originX, 
            self.coord_size + self.coord_margin, 
            fill="lightgrey",
            dash=(2,2))
        #create_outline
        self.redraw()
        
    def create_outline(self):
        x1 = self.coord_originX - self.outline_radius
        x2 = self.coord_originX + self.outline_radius
        y1 = self.coord_originY - self.outline_radius
        y2 = self.coord_originY + self.outline_radius
        self.outline = self.canvas.create_oval(x1, y1, x2, y2, outline="grey", dash=(2,2))
        
    def update_outline(self, dif):
        old_axs1 = self.axs1.get() * self.zoom
        old_axs2 = self.axs2.get() * self.zoom
        self.outline_radius = math.sqrt(old_axs1**2 + old_axs2**2) + dif
        if self.outline_radius > self.coord_size / 2:
            self.outline_radius = self.coord_size / 2
        self.canvas.delete(self.outline)
        self.create_outline()
        self.update_direction(0)
        
    def update_direction(self, degdif):
        raddif = math.radians(degdif)
        old_axs1 = self.axs1.get() * self.zoom
        old_axs2 = self.axs2.get() * self.zoom
        direction = math.atan2(old_axs1, old_axs2) + raddif
        axs1nxt = self.outline_radius * math.sin(direction) + self.coord_originX
        axs2nxt = self.outline_radius * math.cos(direction) + self.coord_originY
        self.axs1.set((axs1nxt - self.coord_originX) / self.zoom) 
        self.axs2.set((axs2nxt - self.coord_originY) / self.zoom) 
        self.canvas.delete(self.direction_line)
        self.direction_line = self.canvas.create_line(self.coord_originX, self.coord_originY, axs1nxt, axs2nxt, fill="blue")
    
    def redraw(self):
        axs1cur = self.axs1.get() * self.zoom
        axs2cur = self.axs2.get() * self.zoom
        direction = math.atan2(axs1cur, axs2cur)
        self.outline_radius = math.sqrt(axs1cur**2 + axs2cur**2)
        dlX = self.outline_radius * math.sin(direction) + self.coord_originX
        dlY = self.outline_radius * math.cos(direction) + self.coord_originY
        if self.outline_radius > self.coord_size / 2:
            self.outline_radius = self.coord_size / 2
        if hasattr(self, "outline"):
            self.canvas.delete(self.outline)
        self.create_outline()
        if hasattr(self, "direction_line"):
            self.canvas.delete(self.direction_line)
        self.direction_line = self.canvas.create_line(self.coord_originX, self.coord_originY, dlX, dlY, fill="blue")
        print(f"{self.axs1.name}: {axs1cur}")
