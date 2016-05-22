from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getWebpage(url):
	"""
		Takes a wiki article url and appends it to the wikipedia domain
	"""
	try:
		#requests a web page from a directory and prints out the html
		fullUrl = "http://en.wikipedia.org"+url
		html = urlopen(fullUrl)
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
		return(html)
		

def readTag(html):
	"""
		Takes an html object and returns a beatuiful soup object
	"""
	try:
		bsObj = BeautifulSoup(html, "lxml")
	except AttributeError as e:
		print(e)
		sys.exit(1)
	else:
		return(bsObj)

		
		
def getLinks(bsObj):
	'''
		Takes a beatuiful soup object and a /wiki/article_name
		string to print the title, first paragraph of content and the
		linke to the edit page
	'''
	global pages
	try:
		print( bsObj.h1.get_text() )
		print( bsObj.find(id="mw-content-text").findAll("p")[0] )
		print( "http://en.wikipedia.org" + bsObj.find(id="ca-edit").find("span").find("a").attrs['href'] )
	except AttributeError as e:
		print("\nUnable to find header, paragraph 1 or edit page")
		print(e )
		

if __name__ == "__main__":
	webpage = getWebpage("/wiki/Toonami")
	bsObj = readTag(webpage)
	
	getLinks(bsObj)
	