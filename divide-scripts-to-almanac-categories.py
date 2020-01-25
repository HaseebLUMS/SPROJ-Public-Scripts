'''
Categories all external
scripts to respective
almanac categories based on
data in all_domains*.json
'''
import json
with open("all_domains2.json") as f: domains = json.loads(f.read())
with open("sourceToURLLog.json") as f: log = json.loads(f.read())
data = {
	"ads": [],
	"analytics": [],
	"marketing": [],
	"social": [],
	"cdn": [],
	"utility": [],
	"tag-manager": [],
	"video": [],
	"hosting": [],
	"customer-success": [],
	"content": [],
	"other": []
}
def process(script):
	url = log[script]
	for target in data:
		doms = domains[target]
		for dom in doms:
			if dom in url:
				data[target] += [script]
				break
for ele in log: process(ele)
with open("trainingScripts3.json", "w") as f: f.write(json.dumps(data, indent=4))


'''
older version
'''
# ads = []
# analytics = []
# marketing = []
# social = []
# cdn = []
# utility = []
# tagManager = []
# video = []
# hosting = []
# customerSuccess = []
# content = []
# other = []

# for ele in log:
# 	processed = False
# 	url = log[ele]

# 	ad_doms = domains["ads"]
# 	for dom in ad_doms:
# 		if dom in url:
# 			ads += [ele]
# 			processed = True
# 			break

# 	analytics_doms = domains["analytics"]
# 	for dom in analytics_doms:
# 		if dom in url:
# 			analytics += [ele]
# 			processed = True
# 			break

# 	mark_doms = domains["marketing"]
# 	for dom in mark_doms:
# 		if dom in url:
# 			marketing += [ele]
# 			processed = True
# 			break

# 	social_doms = domains["social"]
# 	for dom in social_doms:
# 		if dom in url:
# 			social += [ele]
# 			processed = True
# 			break

# 	cdn_doms = domains["cdn"]
# 	for dom in cdn_doms:
# 		if dom in url:
# 			cdn += [ele]
# 			processed = True
# 			break

# 	utility_doms = domains["utility"]
# 	for dom in utility_doms:
# 		if dom in url:
# 			utility += [ele]
# 			processed = True
# 			break

# 	tag_doms = domains["tag-manager"]
# 	for dom in tag_doms:
# 		if dom in url:
# 			tagManager += [ele]
# 			processed = True
# 			break

# 	vid_doms = domains["video"]
# 	for dom in vid_doms:
# 		if dom in url:
# 			video += [ele]
# 			processed = True
# 			break

# 	hos_doms = domains["hosting"]
# 	for dom in hos_doms:
# 		if dom in url:
# 			hosting += [ele]
# 			processed = True
# 			break

# 	cus_doms = domains["customer-success"]
# 	for dom in cus_doms:
# 		if dom in url:
# 			customerSuccess += [ele]
# 			processed = True
# 			break

# 	cont_doms = domains["content"]
# 	for dom in cont_doms:
# 		if dom in url:
# 			content += [ele]
# 			processed = True
# 			break

# 	oth_doms = domains["other"]
# 	for dom in oth_doms:
# 		if dom in url:
# 			other += [ele]
# 			processed = True
# 			break
# 	# if not processed: other += [ele]


# data = {
# 	"ads": ads,
# 	"analytics": analytics,
# 	"marketing": marketing,
# 	"social": social,
# 	"cdn": cdn,
# 	"utility": utility,
# 	"tag-manager": tagManager,
# 	"video": video,
# 	"hosting": hosting,
# 	"customer-success": customerSuccess,
# 	"content": content,
# 	"other": other
# }
