import json
import os

PATH = os.path.join(os.path.dirname(__file__), 'user_data.json')

def load_users():
    with open(PATH, 'r', encoding='utf-8') as f:
        return json.load(f)
    
users = load_users()

print(users['user0']['name'])