#in the python standard template library
from urllib.request import urlopen
from bs4 import BeautifulSoup
#requests a web page from a directory and prints out the html
html = urlopen("http://pythonscraping.com/pages/page1.html")

#kaggle leaderboard for bnp paribus
#html2 = urlopen("https://www.kaggle.com/c/bnp-paribas-cardif-claims-management/leaderboard")

bsObj = BeautifulSoup(html.read())

#bsObj2 = BeautifulSoup(html.read())
#prints the header tag
print(bsObj.h1)

