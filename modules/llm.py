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
  

def prompt(query):
    api_url=llm_config["url"]
    headers=llm_config["headers"]
    json_data=llm_config["json"]
    json_data["prompt"]=query
    request_type=llm_config["requestType"]
        
    response=requests.request(request_type,api_url,headers=headers,json=json_data)
    return response
