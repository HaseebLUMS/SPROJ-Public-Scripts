import json

with open("rules0.json") as f: rules0 = json.loads(f.read())
with open("rules1.json") as f: rules1 = json.loads(f.read())
with open("rules2.json") as f: rules2 = json.loads(f.read())

rules = rules0 + rules1 + rules2

with open("rules.json", "w") as f: f.write(json.dumps(rules, indent=4))