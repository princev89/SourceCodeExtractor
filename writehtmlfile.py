from bs4 import BeautifulSoup
import urllib.request
from getfilename import getfilename
def writefile(url):
	filename = getfilename(url)
	f = open(filename,"wb")
	parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
	resp = urllib.request.urlopen(url)
	content = resp.read()
	f.write(content)

