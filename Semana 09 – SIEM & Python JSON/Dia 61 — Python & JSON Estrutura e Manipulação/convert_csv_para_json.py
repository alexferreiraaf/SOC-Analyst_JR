import csv, json

with open('relatorio.csv') as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open('relatorio.json', 'w') as f:
    json.dump(data, f, indent=4)


