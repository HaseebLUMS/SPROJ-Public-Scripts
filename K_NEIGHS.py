from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib

import matplotlib.pyplot as plt
import numpy as np
import glob
import json
import sys
import random

from utilities import LABELS_MAP


'''
Preparing the data
'''
with open("Keywords.json") as f: Keywords = json.loads(f.read())

with open("categorizedScripts.json") as f: categorizedScripts = json.loads(f.read())
categories = list(categorizedScripts.keys())

SCRIPTNAMES_A = []
SCRIPTNAMES_B = []
SCRIPTS_A = []
SCRIPTS_B = []
LABELS_A = []
LABELS_B = []

for cat in categories:
	scriptNames = categorizedScripts[cat]

	mid = int(len(scriptNames)/1.3)
	scriptNames_A = scriptNames[:mid]
	scriptNames_B = scriptNames[mid:]
	for name in scriptNames_A:
		LABELS_A += [cat]
		SCRIPTNAMES_A += [name]
		SCRIPTS_A += [" ".join(Keywords[name])]

	for name in scriptNames_B:
		LABELS_B += [cat]
		SCRIPTNAMES_B += [name]
		SCRIPTS_B += [" ".join(Keywords[name])]


TRAINING_INDEX = len(SCRIPTS_A)
SCRIPTS = SCRIPTS_A + SCRIPTS_B
LABELS = LABELS_A + LABELS_B
SCRIPTNAMES = SCRIPTNAMES_A + SCRIPTNAMES_B


'''
Vectorizing by TFIDF Vectorizer
'''
print("Vectorizing.")
tfidf_vectorizer = TfidfVectorizer(token_pattern=r"(?u)\S\S+") #break words on white spaces only
tfidf = tfidf_vectorizer.fit_transform(SCRIPTS)
X = tfidf.toarray()
y = np.array(list(map(lambda x: LABELS_MAP[x], LABELS)))


'''
Splitting Training and Testing Data
'''
training_data = X[:TRAINING_INDEX]
training_labels = y[:TRAINING_INDEX]
testing_data = X[TRAINING_INDEX:]
testing_labels = y[TRAINING_INDEX:]

print("Training Data Size: ", training_data.shape)
print("Testing Data Size: ", testing_data.shape)


'''
Training K Nearest Neighbors Classifier
'''
print("Training Model.")
neigh = KNeighborsClassifier(n_neighbors=351)
neigh.fit(training_data, training_labels)


'''
Storing the Model
'''
# joblib.dump(neigh, "kneigh_model.sav")


'''
Testing the Model
'''
print("Testing Model.")
ans = neigh.predict(testing_data)
score = 0
total = 0
check = []
truth = []
for i in range(0, len(testing_labels)):
	total += 1
	check += [int(ans[i])]
	truth += [int(testing_labels[i])]
	if testing_labels[i] == ans[i]:
		score += 1
res = {
	"predictions": check,
	"truth": truth
}
with open("resKNN.json", "w") as f: f.write(json.dumps(res, indent=4))
print("Results:")
print("Correct Predictions: ", score)
print("Total Testing Data: ", total)
