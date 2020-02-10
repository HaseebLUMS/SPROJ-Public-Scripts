'''
Generates distinctive
association rules for 
all categories
'''
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
import json

DATA = {}
Keywords = {}

with open("Classes/class0.json") as f: data = json.loads(f.read())
DATA["non-critical"] = list(data.keys())
for ele in data: Keywords[ele] = data[ele]

with open("Classes/class1.json") as f: data = json.loads(f.read())
DATA["critical"] = list(data.keys())
for ele in data: Keywords[ele] = data[ele]

with open("Classes/class2.json") as f: data = json.loads(f.read())
DATA["replaceable"] = list(data.keys())
for ele in data: Keywords[ele] = data[ele]

cats = [
	"non-critical",
	"critical",
	"replaceable"
]

sups = {
	"non-critical": 0.00025,
	"critical":0.09,
	"replaceable":0.005
}


def gen(data, sup, exclude):
	dataset = data.values()
	te = TransactionEncoder()
	te_ary = te.fit(dataset).transform(dataset)
	df = pd.DataFrame(te_ary, columns=te.columns_)
	print("generating (2)")
	# print(df)
	rules = fpgrowth(df, min_support=sup, use_colnames=True)
	rules = rules["itemsets"]
	print(len(rules))
	res = []
	for rule in rules:
		tmp = []
		for ele in rule:
			tmp += [ele]
		if len(tmp) <= 1: continue 
		tmp = sorted(tmp)
		r = ""
		for ele in tmp:
			r = r + ele + "|"
		r = r[:-1]
		if r in exclude: continue
		res += [r]
	if len(res) > 300: res = res[0:300]
	return res
exclude = []
for c in cats:
	data = {}
	scriptNames = DATA[c]
	for name in scriptNames:
		data[name] = Keywords[name]
	print(c, len(data))
	print("generating")
	done = True
	ans = []
	sup = sups[c]

	ans = gen(data, sup, exclude)
	print(len(ans))
	exclude += ans


with open("crules.json", "w") as f: f.write(json.dumps(exclude, indent=4))