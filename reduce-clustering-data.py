import json
with open("ground_truth.json") as f: gt = json.loads(f.read())

noncritical_names = []
critical_names = []
replaceable_names = []

for file_name in gt:
	if gt[file_name] == 0:
		noncritical_names += [file_name]
	elif gt[file_name] == 1:
		critical_names += [file_name]
	elif gt[file_name] == 2:
		replaceable_names += [file_name]
	else:
		print("Wot?")

import random
random.shuffle(noncritical_names)
random.shuffle(critical_names)
random.shuffle(replaceable_names)

random.shuffle(noncritical_names)
random.shuffle(critical_names)
random.shuffle(replaceable_names)

noncritical_names = (noncritical_names[:7000])
critical_names = (critical_names[:7000])
replaceable_names = (replaceable_names[:7000])

print(len(noncritical_names), len(critical_names), len(replaceable_names))

with open("Rules.json") as f: dataset = json.loads(f.read())
reduced_dataset = {}
reduced_groundtruth = {}
for ele in noncritical_names:
	reduced_dataset[ele] = dataset[ele]
	reduced_groundtruth[ele] = 0
for ele in critical_names:
	reduced_dataset[ele] = dataset[ele]
	reduced_groundtruth[ele] = 1
for ele in replaceable_names:
	reduced_dataset[ele] = dataset[ele]
	reduced_groundtruth[ele] = 2

print(len(reduced_dataset))
tf = "reduced4.json"
with open(tf, "w") as f: f.write(json.dumps(reduced_dataset, indent=4))
print("written target = ", tf)

with open("reducedGT4.json", "w") as f: f.write(json.dumps(reduced_groundtruth, indent=4))