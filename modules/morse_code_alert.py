#!/usr/bin/env python3

import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0',baudrate=115200, timeout=1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    while True:
        data = arduino.readline().decode().strip()
        if '/420' in data:
            break
        print(data)

while True:
    message = input("Enter a message: ")
    value = write_read(message)
    print("Message sent successfully. Restarting...")

    