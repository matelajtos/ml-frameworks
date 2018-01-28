import json
import pygsheets


gc = pygsheets.authorize(outh_file='client_secret.json', no_cache=True)

try:
    ws = gc.open('ml_frameworks').worksheet('index', 0)
except pygsheets.SpreadsheetNotFound:
    ss = gc.create('ml_frameworks').worksheet('index', 0)
    
with open('sorted.json', 'r') as data_f:
    data = json.load(data_f)

ws.update_row(1, list(data[0].keys()))

for i, row in enumerate(data):
    ws.update_row(i+2, list(row.values()))
