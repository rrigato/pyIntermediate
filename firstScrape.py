"""
	Does some basic web scraping
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import sys

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
	
#kaggle leaderboard for bnp paribus
#html2 = urlopen("https://www.kaggle.com/c/bnp-paribas-cardif-claims-management/leaderboard")


def justSpan():
	'''
		prints all text from span tags with class=green
	'''
	html = getWebpage("http://pythonscraping.com/pages/warandpeace.html")


	#bsObj2 = BeautifulSoup(html.read())
	#prints the header tag
	bsObj = readTag(html)

	#retrieves all span html elments with class=green
	nameList = bsObj.findAll("span", {"class", "green"})

	#prints just the value of the span tag, not tag itself
	for name in nameList:
		print(name.get_text())


justSpan()
