import os
import sys
import glob
from collections import OrderedDict
import re
import json

JSFeaturesDict = OrderedDict()
with open("FinalFeatures.txt", 'r') as ref: 
	for line in ref:
		if '|' in line:
			words = line.strip().split('|')
			JSFeaturesDict[words[0]] = words[1]


folder = "./crawler/data/"
files = [f for f in glob.glob(folder + "**/*.js", recursive=True)]


def extractKeywords (content):
	content = re.sub(' +', ' ', content) #converts multiple contiguous spaces to a single space
	res = []
	for feature in JSFeaturesDict:
		count = content.count("."+feature+"(") + content.count("."+feature+" (")
		if count:
			res += ([feature]*count)
	return res


kws = {}
count = 0
sem = 500
fc = 1
for file in files:
	with open(file) as f: data = f.read()
	kws[file] = extractKeywords(data)


	count += 1
	if sem == 0:
		with open("tmp/1JanKeywords" + str(fc) + ".json", "w") as f: f.write(json.dumps(kws, indent=4))
		fc += 1
		sem = 500
		print(count, fc)
		kws = {}
	sem -=1
with open("tmp/1JanKeywords0.json", "w") as f: f.write(json.dumps(kws, indent=4))