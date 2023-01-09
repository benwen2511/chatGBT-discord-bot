import json

def get_token(token_name):
  with open('config.json', 'r') as f:
    data = json.load(f)
  return data[token_name]
