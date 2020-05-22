import json
with open("without_plugin_results_500.json") as f: without_plugin = json.load(f)
with open("500_with_plugin2_results.json") as f: with_plugin = json.load(f)

with_plugin_dict = {}
with_plugin_url = []
for ele in with_plugin:
	with_plugin_dict[ele["url"]] = ele
	with_plugin_url += [ele["url"]]


without_plugin_dict = {}
without_plugin_url = []
for ele in without_plugin:
	if ele["url"] not in with_plugin_url: continue
	without_plugin_dict[ele["url"]] = ele
	without_plugin_url += [ele["url"]]

urls = without_plugin_url
print(len(urls))

plt_without = [without_plugin_dict[url]["transferSize"] for url in urls]
plt_with = [with_plugin_dict[url]["transferSize"] for url in urls]

print(plt_with)