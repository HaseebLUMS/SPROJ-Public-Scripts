'''
Generates distinctive
association rules for 
all categories
'''
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
import json

with open("trainingScripts3.json") as f: DATA = json.loads(f.read())
with open("Keywords.json") as f: Keywords = json.loads(f.read())

cats = [
	"analytics",
	"ads",
	"marketing",
	"social",
	"cdn",
	"utility",
	"tag-manager",
	"video",
	"hosting",
	"customer-success",
	"content",
	"other"
]
sups = {
	"ads": 0.35,
	"analytics": 0.45,
	"marketing": 0.25,
	"social": 0.6,
	"cdn": 0.55,
	"utility": 0.34,
	"tag-manager": 0.4,
	"video": 0.45,
	"hosting": 0.15,
	"customer-success": 0.3,
	"content": 0.15,
	"other": 0.2
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
	if len(res) > 200: res = res[0:200]
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