import tkinter as tk
from tkinter import ttk
from tkinter import font
from coord_control import ccm

root = tk.Tk()
default_font = font.nametofont("TkFixedFont")
default_font.configure(size=10)
root.option_add("*Font", default_font)

test = tk.Label(root, text="Hallo!")
test.pack()

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
coordControlFrame = tk.Frame(tab1, padx=20, pady=20)
coordControlFrame.pack()
CoordControlMaster = ccm.CoordControlMaster(coordControlFrame)
tabControl.add(tab1, text ='1')


tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text ='2')



tabControl.pack(expand=1, fill="both")
root.mainloop()