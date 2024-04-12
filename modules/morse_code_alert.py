#!/usr/bin/env python3

#
# Current script will only be requested to run by Al main hive
# modules are tools not hives
#

import serial
import time
import re

arduino = serial.Serial(port='/dev/ttyACM0',baudrate=115200)

def arduino_communications(message):
        message = re.sub(r'\n{3,}','\n\n',message)
        print(message)
        
        arduino.flush()
        arduino.write(bytes(message, 'utf-8'))
        time.sleep(0.1)
        while True:
            data = arduino.readline().decode().strip()
            if '/420' in data:
                break
            data = data.replace("::","")
            print(data,end='',flush=True)
        print("")
