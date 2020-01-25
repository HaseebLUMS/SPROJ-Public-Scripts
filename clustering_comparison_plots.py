import json
import sys
filename = sys.argv[1]
gf = sys.argv[2]
with open(filename) as f: k_means_log = json.loads(f.read())
with open(gf) as f: rule_based_log = json.loads(f.read())
'''
Checking whether any files are present in one log and not in other (ground truth)
Ideally, following two prints should be []
'''
a = [key for key in k_means_log if key not in rule_based_log]
print(a) #[]

a = [key for key in rule_based_log if key not in k_means_log]
print(a) #[]

'''
Separating scripts by classes
'''
k_means_log_class_0 = [key for key in k_means_log if k_means_log[key] == 0]
k_means_log_class_1 = [key for key in k_means_log if k_means_log[key] == 1]
k_means_log_class_2 = [key for key in k_means_log if k_means_log[key] == 2]
rule_based_log_class_0 = [key for key in rule_based_log if rule_based_log[key] == 0]
rule_based_log_class_1 = [key for key in rule_based_log if rule_based_log[key] == 1]
rule_based_log_class_2 = [key for key in rule_based_log if rule_based_log[key] == 2]
print(len(k_means_log_class_0), len(k_means_log_class_1), len(k_means_log_class_2))
print(len(rule_based_log_class_0), len(rule_based_log_class_1), len(rule_based_log_class_2))
'''
Finding composition of k means class 0
k -> kmeans
r -> rule based
'''
k0_r0 = set(k_means_log_class_0).intersection(rule_based_log_class_0)
print(len(k0_r0)) 

k0_r1 = set(k_means_log_class_0).intersection(rule_based_log_class_1)
print(len(k0_r1)) 

k0_r2 = set(k_means_log_class_0).intersection(rule_based_log_class_2)
print(len(k0_r2)) 

'''
Finding composition of k means class 1
k -> kmeans
r -> rule based
'''
k1_r0 = set(k_means_log_class_1).intersection(rule_based_log_class_0)
print(len(k1_r0)) 

k1_r1 = set(k_means_log_class_1).intersection(rule_based_log_class_1)
print(len(k1_r1)) 

k1_r2 = set(k_means_log_class_1).intersection(rule_based_log_class_2)
print(len(k1_r2)) 

'''
Finding composition of k means class 2
k -> kmeans
r -> rule based
'''
k2_r0 = set(k_means_log_class_2).intersection(rule_based_log_class_0)
print(len(k2_r0)) 

k2_r1 = set(k_means_log_class_2).intersection(rule_based_log_class_1)
print(len(k2_r1)) 

k2_r2 = set(k_means_log_class_2).intersection(rule_based_log_class_2)
print(len(k2_r2)) 


import matplotlib.pyplot as plt

fig = plt.figure(figsize=(2,5))

fig.add_subplot(2,5,3)
plt.pie([len(k_means_log_class_0), len(k_means_log_class_2), len(k_means_log_class_1)], labels=("Class 0", "Class 2", "Class 1"), colors=["green", "yellow", "red"], autopct='%1.1f%%', startangle=180)
plt.title("Hierarchial Clusters (voc = apis+rules)")

fig.add_subplot(2,5,6)
plt.pie([len(k0_r0), len(k0_r1), len(k0_r2)], labels=("R-Class 0", "R-Class 1", "R-Class 2"), colors=["green", "red", "yellow"], autopct='%1.1f%%', startangle=120)
plt.title("Composition of Class 0")

fig.add_subplot(2,5,8)
plt.pie([len(k1_r0), len(k1_r1), len(k1_r2)], labels=("R-Class 0", "R-Class 1", "R-Class 2"), colors=["green", "red", "yellow"], autopct='%1.1f%%', startangle=120)
plt.title("Composition of Class 1")

fig.add_subplot(2,5,10)
plt.pie([len(k2_r0), len(k2_r2), len(k2_r1)], labels=("R-Class 0", "R-Class 2", "R-Class 1"), colors=["green", "red", "yellow"], autopct='%1.1f%%', startangle=180)
plt.title("Composition of Class 2")

plt.show()

# '''
# Making a log
# '''

# k0_r0 = k0_r0

# k0_r0_data = {}
# k0_r1_data = {}
# k0_r2_data = {}



# k1_r0_data = {}
# k1_r1_data = {}
# k1_r2_data = {}



# k2_r0_data = {}
# k2_r1_data = {}
# k2_r2_data = {}


# with open("voc4.json") as f: data = json.loads(f.read())

# for ele in k0_r0:
# 	k0_r0_data[ele] = data[ele]

# with open("analyze/k0_r0_data.json", "w") as f: f.write(json.dumps(k0_r0_data, indent=4))


# for ele in k0_r1:
# 	k0_r1_data[ele] = data[ele]

# with open("analyze/k0_r1_data.json", "w") as f: f.write(json.dumps(k0_r1_data, indent=4))


# for ele in k0_r2:
# 	k0_r2_data[ele] = data[ele]

# with open("analyze/k0_r2_data.json", "w") as f: f.write(json.dumps(k0_r2_data, indent=4))


# for ele in k1_r0:
# 	k1_r0_data[ele] = data[ele]

# with open("analyze/k1_r0_data.json", "w") as f: f.write(json.dumps(k1_r0_data, indent=4))


# for ele in k1_r1:
# 	k1_r1_data[ele] = data[ele]

# with open("analyze/k1_r1_data.json", "w") as f: f.write(json.dumps(k1_r1_data, indent=4))


# for ele in k1_r2:
# 	k1_r2_data[ele] = data[ele]

# with open("analyze/k1_r2_data.json", "w") as f: f.write(json.dumps(k1_r2_data, indent=4))

# for ele in k2_r0:
# 	k2_r0_data[ele] = data[ele]

# with open("analyze/k2_r0_data.json", "w") as f: f.write(json.dumps(k2_r0_data, indent=4))


# for ele in k2_r1:
# 	k2_r1_data[ele] = data[ele]

# with open("analyze/k2_r1_data.json", "w") as f: f.write(json.dumps(k2_r1_data, indent=4))


# for ele in k2_r2:
# 	k2_r2_data[ele] = data[ele]

# with open("analyze/k2_r2_data.json", "w") as f: f.write(json.dumps(k2_r2_data, indent=4))
