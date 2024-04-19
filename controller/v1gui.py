import tkinter as tk

class V1CtrlGui:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.label_is_active = tk.Label(self.root, text=f"Status: {self.controller.status}")

        self.button_activate = tk.Button(self.root, text="activate", command=self.on_button_activate)

        self.label_is_active.grid(row=0, column=1)
        self.button_activate.grid(row=0, column=0)


    def on_button_activate(self):
        if self.controller.status != 2:
            self.controller.activate()
        
    
    def render(self):
        self.root.delete(self.label_is_active)
        self.label_is_active = tk.Label(self.root, text=f"active: {self.controller.active}")
        self.label_is_active.pack(row=0, column=1)