import tkinter as tk
from tkinter import ttk
from . import ccp
from.import av
from controller import v1

class CoordControlMaster:
    
    
    def __init__(self, root, controller=None):
        self.axisX = av.AxisVariable("X", 100)
        self.axisY = av.AxisVariable("Y", 100)
        self.axisZ = av.AxisVariable("Z", 100)
        self.axisDummy = av.AxisVariable("Dummy", 100)
        if not controller:
            self.controller = v1.ArmCtrl("COM3")
        else:
            self.controller = controller
        self.controller.set_axs(self.axisX, self.axisY, self.axisZ)
        
        self.tabControl = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tabControl)
        
        CCP_1 = ccp.CoordControlPanel(self.tab1, name="XY", axs1=self.axisX, axs2=self.axisY, controller=self.controller)
        CCP_1.frame.grid(row=1, column=0, padx=5)
        CCP_1.add()
        CCP_2 = ccp.CoordControlPanel(self.tab1, name="YZ", axs1=self.axisY, axs2=self.axisZ, controller=self.controller)
        CCP_2.frame.grid(row=1, column=1, padx=5)
        CCP_2.add()
        CCP_3 = ccp.CoordControlPanel(self.tab1, name="ZX", axs1=self.axisZ, axs2=self.axisX, controller=self.controller)
        CCP_3.frame.grid(row=1, column=2, padx=5)
        CCP_3.add()
        
        self.tab2 = ttk.Frame(self.tabControl)
        
        self.tabControl.add(self.tab1, text ='CCtrl')
        self.tabControl.add(self.tab2, text ='Controller')
        self.tabControl.pack()