#!/Al/.venv/bin/python3

#AL MODULES IMPORT
from modules import *

import requests
import json
import typer
import inquirer
from yaspin import yaspin
import pyfiglet
import datetime
from tabulate import tabulate
import configparser
import os
import re

ini = os.path.join(os.path.dirname(__file__),"program_data","api.ini")
jsonconfig = os.path.join(os.path.dirname(__file__),"program_data","api.json")
config = configparser.ConfigParser()
config.read(ini)
config_values= {}
session=False

with open(jsonconfig) as f: 
  data= json.load(f)
  
for section in config.sections():
  config_values[section]={}
  for option in config.options(section):
    config_values[section][option]= config.get(section,option)  

APISV2={}
for key in data:
  APISV2[key] = data[key]


APIS={}
for api in config_values['api_url']:
  APIS[api]=config_values['api_url'][api]


def fetchToAPI(query,API):
  

  # headers = {
  #   'Content-Type':'application/json',
  #   }
  
  # json_data= {
  #   "model": "mistral",
  #   "prompt": query,
  #   "stream": False
  # }
  
  api_url=API["url"]
  headers=API["headers"]
  json_data=API["json"]
  json_data["prompt"]=query
  request_type=API["requestType"]
  
  response=requests.request(request_type,api_url,headers=headers,json=json_data)
  return response
  

def main():
  responseMessage= ""
  while True:
    API = inquirer.list_input("What api do you choose?",choices=APISV2)
    
    if API=="exit":
      break
    session=True
    while session:
      query = input(">>>")
      if query.lower()=='exit':
        session=False
        break
      elif query.lower()=='test':
        responseMessage='Hello World'
      else:
        responseData=fetchToAPI(query,APISV2[API])
        if responseData.status_code == 200:
            responseJson = responseData.json()
            responseMessage  = responseJson['response']

      morse_code_alert.arduino_communications(responseMessage) # type: ignore
        
       
        
    else:
        print('POST request failed with status code:', responseData.status_code)

if __name__ == "__main__":
    typer.run(main)
    pass
