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
		Takes a beatuiful soup object to find all championship winning 
		teams
	'''
	global pages
	#.find("div", {"id":"page-container"})
	try:
		links =( bsObj.find("div", {"id":"page_container"})
					.find("div", {"id":"page_content"})	
					.findAll("a", href = re.compile("\/teams\/*") ) )

		return(links)

	except AttributeError as e:
		print("Unable to find all Champions")
		print(e )
		
def getOpponents(link):
	'''
		Input: Is given a link to the team page of a championship winning team
		
		The function then gets a beatuifulSoup object for that page.
		It finds the internal links to the 4 team pages that the championship
		winning team beat in the playoffs
		
		The function then goes onto each of those 4 team pages and gets the 
		point differential and SRS for each team during the regular season.

		Returns: The average point differential and SRS of the championship 
		winning teams opponents in the playoffs
		
		Note: All Championship winning teams since 1984 have played four rounds
		to win the championship
	'''
	
	#gets the beatuifulSoup object for the championship team page
	#passed to the function
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
	try:
		#get each playoff opponents this loop gets their point differential and srs
		for round in playoffs:
		
			#crawl delay for basketball reference is 3 seconds
			time.sleep(3)
			print((round.attrs['href']))
			bsObj2 = readTag(getWebpage(round.attrs['href']))
			#print( bsObj2.find("div", {"id":"page_container"}).find("div", {"id":"info_box"}).findAll("p")[1] )
			
			#gets the table row which contains the teams Point Differential and SRS among other things
			team_stats =  ( bsObj2.find("div", {"id":"page_container"}).find("div", {"id":"page_content"})
							.find("div", {"id":"all_team_misc"}).find("div", {"id":"div_team_misc"})
							.find("table", {"id":"team_misc"}).find("tbody").findAll("tr", {"class":""})[0]
							.findAll("td", {"align":"right"}) ) 
							
			#keeps point differential and 
			important_stats =  [ team_stats[i] for i in keep ]
			
			#gives each opponents margin of victory and srs
			print(important_stats[0].get_text())
			print(important_stats[1].get_text())
			#casting SRS and point_differential as float and getting the cumulative sum for
			#all four playoff opponents
			point_differential = point_differential + float(important_stats[0].get_text())
			simple_rating = simple_rating + float(important_stats[1].get_text())
	except AttributeError as e:
		print("Unable to find Point Differentials OR SRSs for all opponents")
		print(e )
	else:
		print(point_differential/4)
		print(simple_rating/4)
		total = [point_differential / 4, simple_rating / 4]
		print("\n Point Differential and SRS of opponents for the playoffs")
		print(total)
		return(total)
	

'''
	runs when the following command is called in the working directory
	of this script:
	python basketballReference.py
	
	Calls functions in order needed to get necessary data
	
	1) Calls the getLinks() function to get all of the internal links of 
		championship winning team pages
	2) Initializes data frame that will hold the year of championship,
	team that won, and average of their playoff opponents regular season
	point differential and srs
	Note: The NBA switched to a a 4 round playoff in 1984, so that is the 
	first year included
'''
if __name__ == "__main__":

	#internal reference to basketball reference that has all championship 
	#winners
	webpage = getWebpage("/leagues/?lid=front_qi_leagues")
	bsObj = readTag(webpage)
	
	#links to championship winners team pages
	links = getLinks(bsObj)


	#initialize the data frame  
	index = range(0,33)
	columns =['Year','Championship_Team', 'Opp_Point_Differential', 'Opp_SRS']
	df = pd.DataFrame(index = index, columns = columns)
	
	#filling in the values if OKC were to potientially win championship
	#DAL SAS GSW CLE
	#point_differential = -.30  10.63  10.76  6.00
	#SRS 				= -.02  10.28  10.38  5.45
	df.ix[0,1] = "OKC*"
	df.ix[0,2] = 6.7725
	df.ix[0,3] = 6.5225
	print(df)

	
	for link in range(32):
		df.ix[link + 1,1] = links[link]['href'][7:9]
		print("Championship winning team:")
		print(df.ix[link + 1,1])
		print()
		
		#calls a function that returns the average point differential and SRS
		total = getOpponents(links[link]['href'])
		df.ix[link + 1,2]  = total[0]
		df.ix[link + 1,3] = total[1]
		
		#crawl delay for basketball reference is 3 seconds
		time.sleep(3)
		print("-----------------------------------------------------------------")
		print("\n\n")
		
	
	#fills in the year each championship was won
	df.ix[0,0] = 2016
	for year in range(1,33):
		df.ix[year,0] = df.ix[year -1 ,0] -1 
		
	#prints the championship team by highest playoff opponent point differential
	print( df.sort_values(by='Opp_Point_Differential', ascending= False)  )