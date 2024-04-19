import tkinter as tk
from tkinter import ttk
from . import ccp
from controller import v2, v1gui

class CoordControlMaster:
    
    
    def __init__(self, root, controller=None):
        if not controller:
            self.controller:v2.CtrlSerial = v2.CtrlSerial("COM3")
        else:
            self.controller = controller
        self.axisX = self.controller.get_axs(0)
        self.axisY = self.controller.get_axs(1)
        self.axisZ = self.controller.get_axs(2)
        self.axisDummy = None
        
        self.tabControl = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tabControl)
        
        CCP_1 = ccp.CoordControlPanel(self.tab1, name="XY", axs=[self.axisX, self.axisY], controller=self.controller)
        CCP_1.frame.grid(row=1, column=0, padx=5)
        CCP_1.add()
        CCP_2 = ccp.CoordControlPanel(self.tab1, name="YZ", axs=[self.axisZ, self.axisX], controller=self.controller)
        CCP_2.frame.grid(row=1, column=1, padx=5)
        CCP_2.add()
        CCP_3 = ccp.CoordControlPanel(self.tab1, name="ZX", axs=[self.axisY, self.axisZ], controller=self.controller)
        CCP_3.frame.grid(row=1, column=2, padx=5)
        CCP_3.add()
        
        self.tab2 = ttk.Frame(self.tabControl)
        self.ctrlgui = v1gui.V1CtrlGui(self.tab2, self.controller)
        self.tabControl.add(self.tab1, text ='CCtrl')
        self.tabControl.add(self.tab2, text ='Controller')
        self.tabControl.pack()