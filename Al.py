#!/usr/bin/env python3
import socket
import os
import sys
import subprocess
from datetime import datetime

#IMPORTING MODULES
from modules import netscan
os.system('clear')
# Global variables
user = os.getenv('USER')
ssh_client = os.getenv('SSH_CLIENT')
system_info = os.uname()
date_current = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
modules_directory = os.path.join(os.path.dirname(__file__),"modules")
isStandby=True

def script_setup(language,script_name):
    script_path = os.path.join(modules_directory,script_name)
    if os.path.isfile(script_path):
        subprocess.run([language,script_path])
    else:
        print(f"Error: {script_path} not found.")

def netscan():
    print("Performing network scan...")
    script_setup("python3","lan_scan/scan.py")
    
def getSSHUser():
    if ssh_client is None:
        print(f"Hello, {user}! My name is Al. Pleased to meet you.")
    else:
        client_ip = ssh_client.split()[0]
        client_port = ssh_client.split()[-1]
        client_string = f"[ {client_ip} : {client_port} ]"
        
        print(f"Hey {client_string}! My name is Al. Pleased to meet you.")
    
    #         print(f"Hello {ssh_client}! Did you visit Elsweyr on your way here?")
    #         print(f"Hello {client_string}! Did you visit Elsweyr on your way here?")

def hello():
    global isStandby
    subprocess.run(["neofetch"])
    getSSHUser()
    print(f'You have successfully authenticated into the {system_info.nodename} network. Congratulations!')
    print(f"The current time where you are located is time: {date_current}")
    isStandby=modules(input("I'm still learning, but let me know if there is anything I can do to assist you.\n>>"))
    

def help():
    global isStandby
    print("|_")
    print("The available modules as of right now are static. They are the following:")
    print("netscan\nclear\nhello")
    print("Help to get to this message.")
    print("|_")
    isStandby = modules(input("Which option do you choose?"))

def clear_screen():
    os.system('clear')

def idle():
    global isStandby
    while True:
        if isStandby:
            isStandby =modules(input("Can I help you with anything?\n>>"))
        else:
            isStandby =modules(input(">>"))

   
def modules(module) -> bool:
    print("|_")
    module= module.lower()
    if module=='n' or module=='no' or module=='exit':
            print("I appreciated our interaction today. I'll be here if you need me.")
            return False  
    
    if module == "netscan":
        netscan()
        return True
    elif module == "clear":
        clear_screen()
    elif module == "hello":
        hello()
    elif module == "help":
        help()
    else:
        print("Module not yet set. Please address Kaichou-sama with this or try 'help' for available modules.")
        return False
    return True

if __name__ == "__main__":
    hello()
    idle()