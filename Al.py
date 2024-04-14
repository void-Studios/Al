#!/home/al/.Al/.venv/bin/python3
import socket
import platform
import sys
import subprocess
from datetime import datetime
import os

from modules import *

def test():
    #folder_path = os.getcwd()
    folder_path = "/home/al/.Al"
    folder_size.visualize_folders(folder_path) # type: ignore
    return

os.system('clear')


# Global variables
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
    
def hello():
    global isStandby
    subprocess.run(["neofetch"])
    ssh_info.getUser()
    print(f'You have successfully authenticated into the {system_info.nodename} network. Congratulations!')
    print(f"The current time where you are located is time: {date_current}")
    isStandby=modules(input("I'm still learning, but let me know if there is anything I can do to assist you.\n>>"))
    

def help():
    global isStandby
    
    print("The available modules as of right now are static. They are the following:")
    print("netscan\nclear\nhello")
    print("Help to get to this message.")
    print("|_")
    isStandby = modules(input("Which option do you choose?"))

def ping():
    llmResponse = llm.prompt("Help me here")
    print(llmResponse)

def clear_screen():
    os.system('clear')


def ping(prompt):
    parsed_prompt = prompt.replace('\n','\\n') 
    llm_response = llm.prompt(parsed_prompt)
    print(llm_response)

def modules(module) -> bool:
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
    elif module =="test":
        test()
    elif module == "logout":
        sys.exit()
    else:
        ping(module)
        print("\nIf there is anything else, please address Kaichou-sama with this or try 'help' for available modules.")
        return False
    return True

def netscan():
    ping("""
    Provide a response taking into account the following:
    You are executing the netscan command
    Some time to wait
    """)
    
def hello():
    global isStandby
    subprocess.run(["neofetch"])
    user_info = ssh_info.getUser()
    ping(f"""
    Your name is Al, and you are residing within the Kurai Tachi server called KuraiOrg,
    Provide a server welcome message, and make sure to use information below as it has been curated for the greeting:
    system information: {system_info.nodename}
    current time: {date_current}
    current user details: {user_info}
    """)
    
    isStandby=modules(input("I'm still learning, but let me know if there is anything I can do to assist you.\n>>"))
    

def help():
    global isStandby
    print("The available modules as of right now are static. They are the following:")
    # Print list of modules
    print("netscan\nclear\nhello")
    
    print("Help to get to this message.")
    
    isStandby = modules(input("Which option do you choose?\n>>"))

def idle():
    global isStandby
    while True:
        if isStandby:
            isStandby =modules(input("Can I help you with anything?\n>>"))
        else:
            isStandby =modules(input(">>"))

   




if __name__ == "__main__":
    hello()
    idle()