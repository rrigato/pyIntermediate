from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random 
import re


def getWebpage(url):
	"""
		Takes a wiki article url and appends it to the wikipedia domain
	"""
	try:
		#requests a web page from a directory and prints out the html
		fullUrl = "http://en.wikipedia.org" + url
		print(fullUrl)
		html = urlopen(fullUrl)
		print(html)
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
		Takes an html object and returns all wikipedia article links
	"""
	try:
		bsObj = BeautifulSoup(html, "lxml")
	except AttributeError as e:
		print(e)
		sys.exit(1)
	else:
		return bsObj.find("div", {"id": "bodycontent"}).findAll( "a",
		re.compile("^(/wiki/)((?!:).)*$") )
		
		
if __name__ == "__main__":
	webpage = getWebpage("/wiki/Kevin_Bacon")
	

	links = readTag(webpage)
	
	
	while len(links) >0 :
		newArticle = links[random.randint(0, len(links) -1)].attrs["href"]
		print(newArticle)
		links = getWebpage(newArticle)
		links = readTag(newArticle)
	