#LLM API
import requests
import json
import configparser
import os

#LLM Setup
api_name = ""
jsonconfig = os.path.join(os.path.dirname(os.path.dirname(__file__)), "program_data", "api.json")

with open(jsonconfig) as f: 
  data= json.load(f)

def check_url(url):
    global api_name
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            api_name= "localhost"
        else:
            api_name= "gemini"
    except requests.exceptions.RequestException as e:
        api_name="gemini"

check_url("http://192.168.196.42:11434")


def prompt(query):
    
    llm_config=data[api_name]
    
    
    api_url=llm_config["url"]
    headers=llm_config["headers"]
    json_data=llm_config["json"]
    
    if api_name == "localhost":
      json_data["prompt"]=query
    else:
      api_key = os.environ.get("GEMINI_API_KEY")
      if not api_key:
        raise ValueError("GEMINI_API_KEY not set")
      api_url.replace("<key>",api_key)
      json_data["contents"][0]["parts"][0]["text"] = query
    
    request_type=llm_config["requestType"]    
    response=requests.request(request_type,api_url,headers=headers,json=json_data)
    return response

