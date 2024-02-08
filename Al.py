#!/usr/bin/env python3
import socket
import os
import sys
import subprocess
from datetime import datetime

#IMPORTING MODULES
from modules import netscan



# Global variables
user = os.getenv('USER')
ssh_client = os.getenv('SSH_CLIENT')
system_info = os.uname()
date_current = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
modules_directory = os.path.join(os.path.dirname(__file__),"modules")

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
<<<<<<< HEAD
    if ssh_client is None:
      print(f"Hello, {user}! My name is Al. Pleased to meet you.")
    
    else:  
      if len(ssh_client) > 0:
          client_ip = ssh_client.split()[0]
          client_port = ssh_client.split()[-1]
          client_string = f"[ {client_ip} : {client_port} ]"
              
=======
    
    if ssh_client is None:
        print(f"Hello, {user}! My name is Al. Pleased to meet you.")
    else:
        client_ip = ssh_client.split()[0]
        client_port = ssh_client.split()[-1]
        client_string = f"[ {client_ip} : {client_port} ]"
        
        print(f"Hey {client_string}! My name is Al. Pleased to meet you.")
    
    
>>>>>>> bfff0e0aec2a68478d41f83966891a61a3eb5085
    #     try:
    #         client_username= os.getenv('HOSTNAME')
    #         print(f"Hello {ssh_client}! Did you visit Elsweyr on your way here?")
    #     except socket.herror:
    #         print("Unable to resolve cliente username.")
    #         print(f"Hello {client_string}! Did you visit Elsweyr on your way here?")

def hello():
    os.system('clear')
    subprocess.run(["neofetch"])
    getSSHUser()
    print(f"Your current session details:")
    for info in system_info:
        print(info)

    print(f"Time: {date_current}")
def clear_screen():
    os.system('clear')

def idle():
    while True:
        user_input=input("Can I help you with anything?\n>>")
        if user_input.lower()=='n' or user_input.lower()=='no' or user_input.lower()=='exit':
            print("It was a pleasure assisting you today. Have a wonderful day.")
            break
        modules(user_input.lower())

   
def modules(module):
    if module == "netscan":
        netscan()
        return True
    elif module == "clear":
        clear_screen()
    elif module == "hello":
        hello()
    else:
        print("Module not yet set. Please address Kaichou-sama with this.")
        return False

if __name__ == "__main__":
    hello()
    idle()