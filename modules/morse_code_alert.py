import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0',baudrate=115200, timeout=1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    
    data = arduino.readline()
    
    return data

while True:
    num = input("Enter a message: ")
    value = write_read(num)
    print(value)