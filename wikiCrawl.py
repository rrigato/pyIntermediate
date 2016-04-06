"""
	This script does some basic web crawling on wikipedia
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import sys
import re


def getWebpage(url):
	"""
		Takes a url and requests the html from a remote server.
	"""
	try:
		#requests a web page from a directory and prints out the html
		html = urlopen(url)
	#catches page not found on server
	except HTTPError as e:
		print(e)
		sys.exit(1)
	#catches server errors not being found
	except URLError as e:
		print(e)
		print("The server could not be found")
		sys.exit(1)
	else:
		return (html)
		
def readTag(html):
	"""
		Takes an html object and returns a beautifulsoup object
	"""
	try:
		bsObj = BeautifulSoup(html)
		Paragraph = bsObj
	except AttributeError as e:
		print(e)
		sys.exit(1)
	else:
		return(Paragraph)
		
		
def Bacon():
	"""
		Gets all the links on the kevin bacon wikipedia page
	"""
	html = getWebpage("http://en.wikipedia.org/wiki/Kevin_Bacon")
	bsObj = readTag(html)
	
	for link in bsObj.find("div", {"id": "bodyContent"}).findAll(
							href=re.compile("^(/wiki/)((?!:).)*$")):
		if 'href' in link.attrs:
			print(link.attrs['href'])
			
			
Bacon()
