import json

with open("ground_truth.json") as f: ground_truth = json.loads(f.read())
with open("Keywords.json") as f: Keywords = json.loads(f.read())

class0 = {}
class1 = {}
class2 = {}

for ele in ground_truth:
	if ground_truth[ele] == 0:
		class0[ele] = Keywords[ele]
	if ground_truth[ele] == 1:
		class1[ele] = Keywords[ele]
	if ground_truth[ele] == 2:
		class2[ele] = Keywords[ele]

print(len(class0), len(class1), len(class2))


'''
0 = non-critical
1 = critical
2 = replaceable
'''


with open("class0.json", "w") as f: f.write(json.dumps(class0, indent=4))
with open("class1.json", "w") as f: f.write(json.dumps(class1, indent=4))
with open("class2.json", "w") as f: f.write(json.dumps(class2, indent=4))