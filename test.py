import requests

API = ""

def check_url(url):
    global API
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            API= "LOCALHOST"
        else:
            API= "GEMINI"
    except requests.exceptions.RequestException as e:
        API="GEMINI"

def get_API():
    global API
    return API

