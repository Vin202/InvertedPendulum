from serial.tools import list_ports
import serial
import time

arduinoConnection = None

def printPorts():
    ports = list_ports.comports()
    for tempPort in ports:
        if (tempPort.hwid.find('SER=24230313831351418180') != -1):
            print(tempPort)

def connectToArduino():
    global arduinoConnection
    arduinoConnection = serial.Serial('/dev/cu.usbmodem1442401', 115200)
    arduinoConnection.setDTR(False)
    time.sleep(1)
    arduinoConnection.reset_input_buffer()
    arduinoConnection.setDTR(True)



def main():
    connectToArduino()
    while(True):
        print(1)
        byteLine = arduinoConnection.readline()
        print(2)
        line = byteLine.decode("utf-8").strip('\r\n')
        print(3)
        print(line)
        print('attempted')


        

main()