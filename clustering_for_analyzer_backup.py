import pickle
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

'''
for the saved models tf_model.sav
and cl_model.sav, 
cluster 0 => Rules-based 1
cluster 1 => Rule-based 0 
cluster 2 => Rule-based 2
'''
import numpy as np
import glob
import json
import sys
import copy

raw_data = []
names = []

filename = sys.argv[1]

with open(filename) as f: data = json.loads(f.read())
keys = data.keys()

for k in keys:
	names += [k]
	dd = list(copy.deepcopy(data[k]))
	raw_data += [" ".join(dd)]

print(len(raw_data), len(names))

class clustering:
	def __init__(self, tfidf_model, clustering_model):
		self.vectorizer = pickle.load(open(tfidf_model, "rb"))
		self.predictor = pickle.load(open(clustering_model, "rb"))
	def readable(self, x):
		'''
		changing clustering's label to 
		rule based label depending upon
		which rule-based class dominated the given cluster
		'''
		if x == 0: return 0
		if x == 1: return 1
		if x == 2: return 2
		return x
	def predict(self, scripts):
		X = self.vectorizer.transform(scripts).toarray()
		preds = self.predictor.predict(X)
		res = list(map(lambda x: self.readable(x), preds))
		return res

cl = clustering("tf_model.sav", "cl_model.sav")
res = cl.predict(raw_data)
logAG = {}
for i in range(0, len(names)):
	logAG[names[i]] = int(res[i])
	# metadata += (names[i]+"\t"+str(cl.labels_[i])+"\n")
mf = "al_"+filename
with open(mf, "w") as f: f.write(json.dumps(logAG, indent=4))