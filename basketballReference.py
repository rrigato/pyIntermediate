from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

def getWebpage(url):
	"""
		Takes the basketball-reference playoff data url and returns it
	"""
	try:
		#requests a web page from a directory and prints out the html
		fullUrl = "http://www.basketball-reference.com" + url
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
	#.find("div", {"id":"page-container"})
	try:
		links =( bsObj.find("div", {"id":"page_container"})
					.find("div", {"id":"page_content"})	
					.findAll("a", href = re.compile("\/teams\/*") ) )
#		for link in links:
#			print(link['href'])
		return(links)
#		print( bsObj.find(id="mw-content-text").findAll("p")[0].get_text() )
#		print( "http://en.wikipedia.org" + bsObj.find(id="ca-edit").find("span").find("a").attrs['href'] )
	except AttributeError as e:
		print("Unable to find all Champions")
		print(e )
		
def getOpponents(link):
	webpage = getWebpage(link)
	bsObj = readTag(webpage)
	
	#gets each championship winning team opponents for each round
	playoffs = (bsObj.find("div", {"id":"page_container"})
					.find("div", {"id":"info_box"}).findAll("p")[4]
					.findAll("a", href = re.compile("\/teams\/*") ) ) 
	
	#variables to keep for team_stats which correspond to margin of victory and 
	#srs
	keep = [2,4]
	
	#keeps track of regular season point differential of all 4 playoff opponents
	point_differential = 0
	
	#keeps track of regualr season srs of all 4 playoff opponents
	simple_rating = 0
	
	#get each playoff opponents record, point differential and srs
	for round in playoffs:
		time.sleep(3)
		print((round.attrs['href']))
		bsObj2 = readTag(getWebpage(round.attrs['href']))
		#print( bsObj2.find("div", {"id":"page_container"}).find("div", {"id":"info_box"}).findAll("p")[1] )
		team_stats =  ( bsObj2.find("div", {"id":"page_container"}).find("div", {"id":"page_content"})
						.find("div", {"id":"all_team_misc"}).find("div", {"id":"div_team_misc"})
						.find("table", {"id":"team_misc"}).find("tbody").findAll("tr", {"class":""})[0]
						.findAll("td", {"align":"right"}) ) 
		important_stats =  [ team_stats[i] for i in keep ]
		
		#gives each opponents margin of victory and srs
		print(important_stats[0].get_text())
		print(important_stats[1].get_text())
		#casting SRS and point_differential as float and getting the cumulative sum for
		#all four playoff opponents
		point_differential = point_differential + float(important_stats[0].get_text())
		simple_rating = simple_rating + float(important_stats[1].get_text())
	print(point_differential/4)
	print(simple_rating/4)
	total = [point_differential / 4, simple_rating / 4]
	print("\n Point Differential and SRS of opponents for the playoffs")
	print(total)
	
#bsObj.find("div", {"id":"page_container"})
#					.find("div", {"id":"info_box"}).findAll("p")[4]	
if __name__ == "__main__":
	webpage = getWebpage("/leagues/?lid=front_qi_leagues")
	bsObj = readTag(webpage)
	
	links = getLinks(bsObj)
#	for link in range(32):
#		print(links[link]['href'])

	index = range(1,34)
	columns =['Year','Team', 'Opp_Point_Differential', 'Opp_SRS']
	df = pd.DataFrame(index = index, columns = columns)
	
	#filling in the values if OKC were to potientially win championship
	#DAL SAS GSW CLE
	#point_differential = -.30  10.63  10.76  6.00
	#SRS 				= -.02  10.28  10.38  5.45
	df.ix[0,1] = "OKC*"
	df.ix[0,2] = 6.7725
	df.ix[0,3] = 6.5225
	print(df)

	
	for link in range(10):
		df.ix[link + 1,1] = links[link]['href'][7:9]
		print("Championship winning team:")
		print(df.ix[link + 1,1])
		print()
		getOpponents(links[link]['href'])
		time.sleep(3)
		print("-----------------------------------------------------------------")
		print("\n\n")
		
	print(df)