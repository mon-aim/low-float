import json

with open('../scrape.json') as f:
    data = json.load(f)

new_data = filter(lambda x: len(x) < 4, data)
print(list(new_data))