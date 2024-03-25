#!/usr/bin/env python3

#AL MODULES IMPORT
from modules import morse_code_alert



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

APIKEYS={}
for key in config_values['api_keys']:
  APIKEYS[key]=config_values['api_keys'][key]

def fetchToAPI(query,API):


  headers = {
    'Content-Type':'application/json',
    }
  
  json_data= {
    "model": "mistral",
    "prompt": query,
    "stream": False
  }
  
  api_url=APISV2[API]["url"]
  
# 
# response = requests.post('http://localhost:3000/v1/generate', headers=headers, json=json_data)
  
  
  response=requests.request("POST",api_url,headers=headers,json=json_data)
  return response
  

def main():
  while True:
    API = inquirer.list_input("What api do you choose?",choices=APISV2)

    session=True
    while session:
      query = input(">>>")
      if query.lower()=='exit':
        session=False
        break
      
      
      responseData=fetchToAPI(query,API)
      
      if responseData.status_code == 200:
          responseJson = responseData.json()
          responseMessage  = responseJson['response']
          # responseMessage  = responseJson.get('response','')
          
          morse_code_alert.arduino_communications(responseMessage)
        
        
        
        
        
        
    else:
        print('POST request failed with status code:', responseData.status_code)

if __name__ == "__main__":
    typer.run(main)
    pass