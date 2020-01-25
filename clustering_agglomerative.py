from sklearn.cluster import AffinityPropagation 
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

import matplotlib.pyplot as plt
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

'''
Vectorizing the code
'''
print("vectorizing")
tfidf_vectorizer = TfidfVectorizer(token_pattern=r"(?u)\S\S+")
tfidf = tfidf_vectorizer.fit_transform(raw_data)
X = tfidf.toarray()
print(X.shape)
# np.savetxt("meta/9reduced_vocabulary_(rules+apis).tsv", X, delimiter="\t")

print("Clustering")

'''
KMEANS Clustering
'''
# kmeans = KMeans(n_clusters=3)
# cl = kmeans.fit(X)

'''
AgglomerativeClustering Parameters
Link: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering
'''
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
cl = cluster.fit(X)


print("Logging")

'''
Logging the results
'''
metadata = "filename\tlabel\n"
logAG = {}
for i in range(0, len(names)):
	logAG[names[i]] = int(cl.labels_[i])
	# metadata += (names[i]+"\t"+str(cl.labels_[i])+"\n")
mf = "AG_LOG_"+filename
with open(mf, "w") as f: f.write(json.dumps(logAG, indent=4))
# with open("meta/metadata"+"9reduced_vocabulary_(rules+apis).tsv", "w") as f: f.write(metadata)
logAG = {}
metadata = ""
print("Finishing")
# '''
# Making ground truth rows comparable to data
# '''
# with open(mf) as f: data = json.loads(f.read())
# with open("ground_truth.json") as f: gt = json.loads(f.read())
# keys = list(data.keys())
# new_gt = {}
# for ele in keys:
# 	new_gt[ele] = gt[ele]
# print(len(new_gt))
# with open("reduced_ground_truth.json", "w") as f: f.write(json.dumps(new_gt, indent=4))
# print(".")