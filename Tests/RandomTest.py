'''Used for quick tests of random stuff'''

from serial.tools import list_ports
import serial
import time

arduinoConnection = None

def printPorts():
    ports = list_ports.comports()
    print('here')
    print(ports)
    for tempPort in ports:
        print('here')
        print(tempPort.hwid)

printPorts()