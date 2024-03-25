#!/usr/bin/env python3

#Required updates:
# Arugment to enable modularity
# Current script will only be requested to run by Al main hive
# modules are tools not hives
#

import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0',baudrate=115200, timeout=1)

def arduino_communications(message):
        arduino.write(bytes(message, 'utf-8'))
        while True:
            data = arduino.readline().decode().strip()
            if '/420' in data:
                break
            print(data)

    