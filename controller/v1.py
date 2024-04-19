import serial
import argparse
import threading

class ArmCtrl:
    active = True
    x = 0
    y = 0
    z = 0
    
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=115200, dsrdtr=None)
        self.ser.setRTS(False)
        self.ser.setDTR(False)
        
        self.serial_recv_thread = threading.Thread(target=self.read_serial)
        self.serial_recv_thread.daemon = True
        self.serial_recv_thread.start()
    
    def set_axs(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.move()
        
    def read_serial(self):
        while True:
            data = self.ser.readline().decode('utf-8')
            if data:
                print(f"Received: {data}", end='')
        
    def write_serial(self, arg):
        self.ser.write(arg.encode() + b'\n')

    def move(self):
        if self.active:
            command = {"T":104,"x":self.x.get(),"y":self.y.get(),"z":self.z.get(),"t":3.14,"spd":0.25}
            self.write_serial(f'{command}')
