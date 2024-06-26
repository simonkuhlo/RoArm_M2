import tkinter as tk
from tkinter import ttk
from tkinter import font
from coord_control_1 import ccm
from controller import v2

root = tk.Tk()
default_font = font.nametofont("TkFixedFont")
default_font.configure(size=10)
root.option_add("*Font", default_font)
root.minsize(width=950, height=500)
test = tk.Label(root, text="Hallo!")
test.pack()
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
coordControlFrame = tk.Frame(tab1, padx=20, pady=20)
coordControlFrame.pack()


controller = v2.CtrlSerial("COM3")
CoordControlMaster = ccm.CoordControlMaster(coordControlFrame, controller=controller)
tabControl.add(tab1, text ='1')


tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text ='2')



tabControl.pack(expand=1, fill="both")
root.mainloop()