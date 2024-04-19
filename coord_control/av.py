import tkinter as tk

class AxisVariable:
    axis_value = 0
    max_value = 500
    registered_objects = []
    
    def __init__(self, name, startvalue = 0):
        self.name = name
        self.axis_value = startvalue
        
    def set(self, value:int):
        if value < self.max_value:
            self.axis_value = value
        else:
            self.axis_value = self.max_value
        self.update()
    
    def get(self):
        return self.axis_value
    
    def register(self, obj):
        if obj not in self.registered_objects:
            self.registered_objects.append(obj)
    
    def update(self):
        for obj in self.registered_objects:
            obj.redraw()
        