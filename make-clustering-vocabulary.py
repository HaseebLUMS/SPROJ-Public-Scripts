import json
with open("rules.json") as f: rules = json.loads(f.read())
with open("Keywords.json") as f: Keywords = json.loads(f.read())

KeywordsAndRules = {}
Rules = {}
sem = 500
count = 0
for script in Keywords:
	if sem <= 0:
		print(count)
		count += 1
		sem = 500
	sem -= 1
	tmp0 = []
	tmp1 = []

	words = Keywords[script]
	tmp0 += words

	for rule in rules:
		prev = rule
		rule = rule.split("|")
		rule = list(filter(lambda x: len(x) >= 1, rule))
		found = True
		for r in rule:
			if r not in words: 
				found = False
				continue
		if found:
			tmp0 += [prev]
			tmp1 += [prev]

	KeywordsAndRules[script] = tmp0
	Rules[script] = tmp1
print("writing!")
with open("KeywordsAndRules.json", "w") as f: f.write(json.dumps(KeywordsAndRules, indent=4))
with open("Rules.json", "w") as f: f.write(json.dumps(Rules, indent=4))