import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
import json

with open("rules0.json") as f: exclude = json.loads(f.read())
with open("rules1.json") as f: exclude += json.loads(f.read())

with open("class2.json") as f: data = json.loads(f.read())

dataset = data.values()


te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)



rules = fpgrowth(df, min_support=0.004, use_colnames=True)

rules = rules["itemsets"]
print(rules)
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
print(len(res))
with open("rules2.json", "w") as f: f.write(json.dumps(res, indent=4))