<<<<<<< HEAD
import requests
import typer
import inquirer
from yaspin import yaspin
import pyfiglet
import datetime
from tabulate import tabulate

API_KEY="XXXXXXXXXXXXXXXXXX"

units = dict(
  metric="°C",
  imperial="°F"
)

def weatherDataToTable(data, unit):
  day=datetime.datetime.fromtimestamp(data['dt'])
  return [f"{day:%d.%m.%Y}", minMaxTemp(data, unit)]

def fetchWeeklyWeather(lon, lat, unit):
  params = dict(
    lon=lon,
    lat=lat,
    units= unit,
    exclude="current,hourly,minutely,alerts",
    appid= API_KEY
  )
  API_URL = "http://api.openweathermap.org/data/2.5/onecall"
  response = requests.get(url=API_URL, params=params)
  return response.json()["daily"]

@yaspin(text="Fetching weather data...")
def fetchWeather(city, country, unit):
  params = dict(
    q=f"{city},{country}",
    units= unit,
    appid= API_KEY
  )
  API_URL = "http://api.openweathermap.org/data/2.5/weather"
  response = requests.get(url=API_URL, params=params)
  lon=response.json()["coord"]["lon"]
  lat=response.json()["coord"]["lat"]
  return fetchWeeklyWeather(lon, lat, unit)

def minMaxTemp(data, unit):
  return "{}{} to {}{}".format(round(data["temp"]["min"]), units[unit], round(data["temp"]["max"]), units[unit])

def main(
  city: str = typer.Option(..., prompt=True),
  country: str = typer.Option(..., prompt=True)
):
  unit = inquirer.list_input("Metric or imperial?", choices=['metric', 'imperial'])
  weatherData=fetchWeather(city, country, unit)
  print(pyfiglet.figlet_format(minMaxTemp(weatherData[0], unit)))
  tabledata = map(lambda x: weatherDataToTable(x, unit), weatherData)
  headers = ["Date", "Temperature range"]
  print(tabulate(tabledata, headers, tablefmt="fancy_grid"))

if __name__ == "__main__":
    typer.run(main)
=======
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
    print(f"Hey {ssh_client}")
    # if len(ssh_client) > 0:
    #     client_ip = ssh_client.split()[0]
    #     client_port = ssh_client.split()[-1]
    #     client_string = f"[ {client_ip} : {client_port} ]"
        
        
        
    #     try:
    #         client_username= os.getenv('HOSTNAME')
    #         print(f"Hello {ssh_client}! Did you visit Elsweyr on your way here?")
    #     except socket.herror:
    #         print("Unable to resolve cliente username.")
    #         print(f"Hello {client_string}! Did you visit Elsweyr on your way here?")
        
        
    # else:
    #     print(f"Hello, {user}! My name is Al. Pleased to meet you.")


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
>>>>>>> master
