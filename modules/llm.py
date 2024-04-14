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
        
    response_data=requests.request(request_type,api_url,headers=headers,json=json_data)
    if response_data.status_code==200:
      response_json = response_data.json()
    return response_json['response']
  
  
if __name__ == "__main__":
    prompt("Hello World")
    pass