import os
from urllib.parse import urlparse


def getfilename(url):
	a = urlparse(url)
	#print(a.path)
	return (os.path.basename(a.path))

url = "https://www.tutorialspoint.com/python/index.htm"
print(getfilename(url))