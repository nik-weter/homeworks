from utils import write_to_file, read_file_data, get_data
import requests
import json
import re

#write_to_file('file.txt', "test")

#res = read_file_data('file.txt')
#print(res)
#r = get_data()
# for key, value in r.headers.items():
#     print(f'{key}: {value}')
#data = json.dumps(r.json(),  indent=1)
#write_to_file('dump.json', data)

habr = requests.get('https://habrahabr.ru/')
text = habr.text
links = []
pattern = r'(<a.*)(\bhref=)([\'\"])?((\w*:\/\/)?([A-z0-9][A-z0-9\.\-]*)(:[0-9]*)?(\/[\w\/-]*)?)([\'\"])(.*)?>'
for line in text.split('\n'):
    u = re.search(pattern, line)
    if u != None and u not in links:
        links.append(u.group(4))
for i in links:
    print(i)