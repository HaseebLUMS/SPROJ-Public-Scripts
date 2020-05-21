from urls import urls

print(len(urls))

import os

def make_command(url, count, extension):
	comm = "browsertime --android --browser firefox -n 1 --resultDir ./res"+str(count)+"/ --prettyPrint "
	if extension != 0:
		comm = comm + "--extension plugin@imc.com.xpi "
	comm = comm + " --firefox.preference browser.cache.disk.enable:false "
	comm = comm + " --timeouts.pageCompleteCheck 60000 "
	comm = comm + url + " --preURL " 
	comm = comm + url
	return comm

for count, url in enumerate(urls):
	try:
		comm = make_command(url, count+501, 1)
		print(comm)
		os.system(comm)
		print(count, " completed.")
	except:
		print(count , " Failed")