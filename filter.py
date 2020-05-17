import glob
import dpkt
from dpkt.ip import IP
import socket
import json
import sys


with open("ip_range") as f: ips = set(f.read().split("\n"))


data_folder = str(sys.argv[1])
all_files = glob.glob("./"+data_folder+"/*.pcap")
print("total pcaps: ", len(all_files))


count_files = 0
for f in all_files:
	result = []
	pcap = dpkt.pcap.Reader(open(f, 'rb'))
	for ts, buf in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			tmp = (".".join((src.split(".")[:3])))+"."
			if tmp not in ips: continue
			dst = socket.inet_ntoa(ip.dst)
			tmp = (".".join((dst.split(".")[:3])))+"."
			if tmp in ips: continue
			result += [(ts, src, dst)]
		except:
			pass
	
	count_files += 1
	print(count_files, " pcaps done.")
	#one pcap is processed
	fn = "results/" + (f.replace("/", "_").replace(".", "_") + "_processed.json")
	with open(fn, "w") as f: f.write(json.dumps(result, indent=4))