import json
import glob

files = glob.glob("./res*/**.json")

result_plugin = []
for file in files:
	with open(file) as f: data = json.loads(f.read())[0]
	url = data["info"]["url"]
	data = data["browserScripts"][0]
	try:
		transferSize = data["pageinfo"]["documentSize"]["transferSize"]
		resources = data["pageinfo"]["resources"]["count"]
		domContentLoadedTime = data["timings"]["pageTimings"]["domContentLoadedTime"]
		domInteractiveTime = data["timings"]["pageTimings"]["domInteractiveTime"]
		pageLoadTime = data["timings"]["pageTimings"]["pageLoadTime"]
		rumSpeedIndex = data["timings"]["rumSpeedIndex"]
		timeToContentfulPaint = -1
		if "timeToContentfulPaint" in data["timings"]:
			timeToContentfulPaint = data["timings"]["timeToContentfulPaint"]
		else: continue
		res = {
		"url":url,
		"transferSize": transferSize,
		"resources": resources,
		"domContentLoadedTime": domContentLoadedTime,
		"domInteractiveTime": domInteractiveTime,
		"pageLoadTime": pageLoadTime,
		"rumSpeedIndex": rumSpeedIndex,
		"timeToContentfulPaint": timeToContentfulPaint
		}
		# print(url)
		result_plugin += [res]
	except:
		# print(file)
		pass

with open("without_plugin_results_500.json", "w") as f: f.write(json.dumps(result_plugin, indent=4))