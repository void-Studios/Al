<<<<<<< HEAD
import platform 
import sys


print(sys.platform)

sysuname  = platform.uname()

for name in sysuname:
    print(name)
    print("|_")
=======
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

>>>>>>> 80e72c200db0a59c30f0eb04c37973a95468bf67
