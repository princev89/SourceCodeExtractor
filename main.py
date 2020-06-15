from bs4 import BeautifulSoup
import urllib.request
from writehtmlfile import writefile


url = input("Enter the ulr of webpage Eg: https://www.tutorialspoint.com/python/index.htm")
pagedomain = input("Enter the page domain Eg: https://www.tutorialspoint.com ")
sourcedir = input("Enter the source dir of your url Eg: /python ")
parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
resp = urllib.request.urlopen(url)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
writefile(url)
for link in soup.find_all('a', href=True):
    pagelink = link['href']
    if(pagelink.find(sourcedir) >= 0):
    	pagelink = pagedomain + pagelink
    	print(pagelink)
    	writefile(pagelink)


