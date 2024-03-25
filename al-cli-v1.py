#!/usr/bin/env python3

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
import json

ini = os.path.join(os.path.dirname(__file__),"program_data","api.ini")
jsonconfig = os.path.join(os.path.dirname(__file__),"program_data","api.json")
config = configparser.ConfigParser()
config.read(ini)
config_values= {}

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


def post_to_API(query,API):
  
  pass

def fetchToAPI(query,API):
  api_url = APIS[API]
  api_key = APIKEYS[API]
    
  if api_key is None or api_key == '':
    api_key=None

  headers = {
    'Content-Type':'application/json',
    }
  

  json_data = {
      'prompt': query,
      'stop': [],
      'llm_config': {
          'max_new_tokens': 128,
          'min_length': 0,
          'early_stopping': False,
          'num_beams': 1,
          'num_beam_groups': 1,
          'use_cache': True,
          'temperature': 0.75,
          'top_k': 15,
          'top_p': 0.78,
          'typical_p': 1,
          'epsilon_cutoff': 0,
          'eta_cutoff': 0,
          'diversity_penalty': 0,
          'repetition_penalty': 1,
          'encoder_repetition_penalty': 1,
          'length_penalty': 1,
          'no_repeat_ngram_size': 0,
          'renormalize_logits': False,
          'remove_invalid_values': False,
          'num_return_sequences': 1,
          'output_attentions': False,
          'output_hidden_states': False,
          'output_scores': False,
          'encoder_no_repeat_ngram_size': 0,
          'n': 1,
          'presence_penalty': 0,
          'frequency_penalty': 0,
          'use_beam_search': False,
          'ignore_eos': False,
          'skip_special_tokens': True,
      },
      'adapter_name': None,
  }

  response=requests.post(apiurl,headers=headers,json=json_data)
  return response
  

def main():
  while True:
    API = inquirer.list_input("What api do you choose?",choices=APISV2)

    print(API)
    
    
    query = input("How may I help you today?\n>>>")
    if query.lower()=='exit':
      break
    
    
    responseData=fetchToAPI(query,API)
    
    if responseData.status_code == 200:
        print('POST request was successful!')
        print('Response:', responseData.json())
    else:
        print('POST request failed with status code:', responseData.status_code)
    
    print("Restarting...")


if __name__ == "__main__":
    typer.run(main)
    pass