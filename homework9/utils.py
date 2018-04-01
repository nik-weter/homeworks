import requests
import json
def write_to_file(file, data):
    with open(file, 'w') as f:
        f.write(data)

def read_file_data(file):
    with open(file, 'r') as f:
        res = f.read()
    return res

def get_data():
    u = 'https://jsonplaceholder.typicode.com/comments'
    r = requests.get(u)
    return r