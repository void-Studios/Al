#!/home/al/.Al/.venv/bin/python3
from modules import llm
import json

response = llm.prompt("Hello world")
response_data  = response.json()
response_text = response_data['candidates'][0]['content']['parts'][0]['text']

print(response_text)
