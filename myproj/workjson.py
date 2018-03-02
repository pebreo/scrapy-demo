import json

with open('words5.json','r') as f:
    datastore = json.load(f)

print(len(datastore['data']))