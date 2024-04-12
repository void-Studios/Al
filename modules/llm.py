#LLM API
import requests
import json
import configparser
import os


#LLM Setup
jsonconfig = os.path.join(os.path.dirname(os.path.dirname(__file__)), "program_data", "api.json")

with open(jsonconfig) as f: 
  data= json.load(f)

llm_config=data["localhost"]
  

def promtp(query):
    
    response ="Pong"
    return response
