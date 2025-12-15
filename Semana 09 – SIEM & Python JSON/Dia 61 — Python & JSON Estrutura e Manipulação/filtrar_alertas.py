import json
from pprint import pprint

with open("logs.json") as f:
    logs = json.load(f)

alertas = [item for item in logs if int(item["falhas"]) > 3]

pprint(alertas)

with open("alertas.json", "w") as f:
    json.dump(alertas, f, indent=4)



