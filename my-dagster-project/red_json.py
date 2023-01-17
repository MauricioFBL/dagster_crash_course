import json

def read_json() -> str:
    f = open('token.json')
    data = json.load(f)
    return data['token']