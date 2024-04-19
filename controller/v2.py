import controller.axisVariable as axisVariable
import serial
import threading

class CtrlSerial:
    movement_style = 0 #0=on axis update 1=manual trigger
    status = 0 #0=off 1=paused 2=running

    axsX = axisVariable.AxisVariable("AxisX", 100)
    axsY = axisVariable.AxisVariable("AxisY", 100)
    axsZ = axisVariable.AxisVariable("AxisZ", 100)
    axsA = [axsX, axsY, axsZ]

    def __init__(self, port):
        self.port = port
        self.setup()

    def setup(self):
        if self.status != 0:
            self.ser = serial.Serial(self.port, baudrate=115200, dsrdtr=None)
            self.ser.setRTS(False)
            self.ser.setDTR(False)
            
            self.serial_recv_thread = threading.Thread(target=self.read_serial)
            self.serial_recv_thread.daemon = True
            self.serial_recv_thread.start()
    
    def write_serial(self, arg):
        self.ser.write(arg.encode() + b'\n')
    
    def read_serial(self):
        while True:
            data = self.ser.readline().decode('utf-8')
            if data:
                print(f"Received: {data}", end='')

    def activate(self):
        if self.status == 0:
            self.setup()
        self.status = 2


    def update(self, axs:int, value:int):
        self.axsA[axs].set(value)
        if self.movement_style == 0:
            self.move()
    
    def move(self):
        if self.status == 2:
            command = {"T":104,"x":self.axsX.get(),"y":self.axsY.get(),"z":self.axsZ.get(),"t":3.14,"spd":0.25}
            self.write_serial(f'{command}')
    


    def get_axs(self, axs):
        if len(self.axsA) > axs:
            return self.axsA[axs]