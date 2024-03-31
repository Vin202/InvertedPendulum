from serial.tools import list_ports
import serial
import time

def printPorts():
    ports = list_ports.comports()
    for tempPort in ports:
        if (tempPort.hwid.find('SER=24230313831351418180') != -1 or  tempPort.hwid.find('SER=442313133303513071E1') != -1):
            print(tempPort)

def connectToArduino():
    arduinoConnection = serial.Serial('COM4', baudrate=115200)
    arduinoConnection.setDTR(False)
    time.sleep(1)
    arduinoConnection.reset_input_buffer()
    arduinoConnection.setDTR(True)
    print('Connection Successful')
    return arduinoConnection



def main():
    arduinoConnection = connectToArduino()
    while(True):
        byteLine = arduinoConnection.readline()
        line = byteLine.decode("utf-8").strip('\r\n')
        print(line)


        
//printPorts()
main()