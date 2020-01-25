import json, sys, os
from utilities import LABELS_MAP, REVERSE_MAP

filename = sys.argv[1]
with open(filename) as f: data = json.loads(f.read())

truth = data["truth"]
preds = data["predictions"]

def analyze(tar):
	TruthIndices = 0
	Preds = []
	for i in range(0, len(truth)):
		if truth[i] == tar:
			TruthIndices += 1
			Preds += [preds[i]]
	return TruthIndices, Preds

tmp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tmp = range(1, 13)

for ele in tmp:
	a, b = analyze(ele)
	print("For ", REVERSE_MAP[str(ele)])
	print("Total = ", a)
	cor = len(list(filter(lambda x: x == ele, b)))
	print("Correct = ", cor)
	print("Recall: ", cor/a)

def falsePositives(tar):
	count = 0
	for i in range(0, len(preds)):
		if (preds[i] == tar) and (truth[i] != tar):
			count += 1
	return count
def falseNegatives(tar):
	count = 0
	for i in range(0, len(preds)):
		if (preds[i] != tar) and (truth[i] == tar):
			count += 1
	return count
def truePositives(tar):
	count = 0
	for i in range(0, len(preds)):
		if (preds[i] == tar) and (truth[i] == tar):
			count += 1
	return count
def trueNegatives(tar):
	count = 0
	for i in range(0, len(preds)):
		if (preds[i] != tar) and (truth[i] != tar):
			count += 1
	return count

# for ele in range(1, 13):
# 	print("For ", REVERSE_MAP[str(ele)])
# 	print(falsePositives(ele))
# 	print(falseNegatives(ele))
# 	print(truePositives(ele))
# 	print(trueNegatives(ele))
