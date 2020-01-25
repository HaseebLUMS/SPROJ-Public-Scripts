'''
Rule-Based Classifier Implementation
Proposed in JSCleaner
'''
import json
from collections import OrderedDict

#Script classes
NON_CRITICAL = 0
CRITICAL = 1
TRANSTLATABLE = 2


JSFeaturesDict = OrderedDict()
with open("FinalFeatures.txt", 'r') as ref: 
	for line in ref:
		if '|' in line:
			words = line.strip().split('|')
			JSFeaturesDict[words[0]] = words[1]

def classifyScript (content):
	scriptClass = NON_CRITICAL
	for feature in content:
			if JSFeaturesDict[feature] == "E":
				scriptClass = CRITICAL
				return scriptClass
			elif JSFeaturesDict[feature] in ["W", "RW"]:
				scriptClass = TRANSTLATABLE
	return scriptClass

with open("Keywords.json") as f: data = json.loads(f.read())
res = {}

print("Processing...")
for script in data:
	res[script] = classifyScript(set(data[script]))
print("Writng File")

with open("RuleBasedClassification.json", "w") as f: f.write(json.dumps(res, indent=4))
