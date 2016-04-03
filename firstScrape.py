#in the python standard template library
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import sys

def getWebpage(website):
	try:
		#requests a web page from a directory and prints out the html
		html = urlopen(website)
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
	try:
		bsObj = BeautifulSoup(html.read())
		Paragraph = bsObj.di
	except AttributeError as e:
		print(e)
		sys.exit(1)
	else:
		return(Paragraph)
	
#kaggle leaderboard for bnp paribus
#html2 = urlopen("https://www.kaggle.com/c/bnp-paribas-cardif-claims-management/leaderboard")

html = getWebpage("http://pythonscraping.com/pages/page1.html")


#bsObj2 = BeautifulSoup(html.read())
#prints the header tag
print(readTag(html))

