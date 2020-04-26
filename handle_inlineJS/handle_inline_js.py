import urllib.request
from bs4 import BeautifulSoup
from get_decision import decision


class handle_inline_js():
	"""
	handle_inline_js handles inline JavaScript
	present in the webpages. 
	"""
	def __init__(self):
		pass

	'''
	takes a url and returns a BeautifulSoup object
	'''
	def fetch(self, url):
		req = urllib.request.Request(url)
		with urllib.request.urlopen(req) as response:
			the_page = response.read()
		soup = BeautifulSoup(the_page, features="lxml")
		return soup

	'''
	- takes a URL and output path
	- fetches the page from URL
	- simplifies
	- stores the result at output path
	'''
	def simplify(self, url, output_file_path="./output", verbose=1):
		page = self.fetch(url)
		
		scripts = page.findAll("script")
		count_inlinejs = 0
		count_blockedjs = 0
		for script in scripts:
			src = script.get("src")
			if (src is None) or (src == ""):
				count_inlinejs += 1
				retain = decision(script)
				if retain == 0:
					removed_script = script.extract()
					#can log the removed scripts from here
					count_blockedjs += 1
		if verbose:
			print(url)
			print("Total Scripts in page: ", len(scripts))
			print("Total Inline JS: ", count_inlinejs)
			print("Total Blocked Inline JS: ", count_blockedjs)
			print("Current # of Scripts in the page: ", len(page.findAll("script")))

		with open(output_file_path, "w") as f: f.write(page.prettify())
simplify_inline = handle_inline_js()
simplify_inline.simplify("http://yasirzaki.net/", "simplified.html")