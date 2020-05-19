import json
with open("results_without_plugin.json") as f: without_plugin = json.loads(f.read())
with open("results_with_plugin_1.json") as f: with_plugin2 = json.loads(f.read())


header = ["page", "PLT_without_plugin", "page_size_without_plugin", "num_resources_without_plugin", "PLT_with_plugin1", "page_size_with_plugin1", "num_resources_with_plugin1"]
main = []
for rec in without_plugin:
	tmp = [rec["url"], rec["plt"], rec["page_size"], rec["resources"]]
	for ele in with_plugin2:
		if ele["url"] == rec["url"]:
			tmp += [ele["plt"], ele["page_size"], ele["resources"]]
	main += [tmp]

print("making")
import pandas as pd
df = pd.DataFrame(main, columns=header)
print(df)

df.to_excel("small_dataset_results2.xlsx", index=False)