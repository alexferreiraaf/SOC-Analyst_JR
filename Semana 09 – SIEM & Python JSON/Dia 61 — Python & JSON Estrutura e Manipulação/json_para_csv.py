import json
import csv

with open('relatorio.json') as f:
    data = json.load(f)

with open('saida.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

