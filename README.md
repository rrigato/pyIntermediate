## pyIntermediate


####[Web Scraping Basketball Reference](https://github.com/rrigato/pyIntermediate/blob/master/basketballReference.py)
The purpose of this script is to get a list of every championship winning basketball team since 1984. The script will then crawl to the championship teams homepage and search for the webpage of each of their 4 opponents. The goal of this script is to find the point differential and simple rating system(SRS) for every championship team's opponents since 1984 

Functions:
* getWebage() = Takes the basketball-reference playoff data url and returns the html
* readTag() = takes html object and returns a beautifulSoup object
* getLinks() = 		Takes a beatuiful soup object to find all championship winning teams
* getOpponents() = Finds The average point differential and SRS of the championship winning teams opponents in the playoffs



####[Web Scraping using Python](https://github.com/rrigato/pyIntermediate/blob/master/firstScrape.py)
This script demonstrates how to web scrape some basic html sites. The functions also are robost due to the error handling that is provided with try catch blocks

* getWebage() = returns the html after making an http GET request from a remote web server
* readTag() = takes html object and returns a beautifulSoup object
* justSpan() = demonstrates scraping <span> tags from a webpage
* page3() = demonstrates scraping all of the table rows from a webpage


####[Basic User stream from twitter API] (https://github.com/rrigato/pyIntermediate/blob/master/twitterStream.py)
This script allows for making a call to the the twitter API to get a specific user tweet data, in this case the user is @talkhoops
The data is returned in JSON format.

Note: when using this script you must insert your own keys provided by the twitter development projects

You can add different parameters to the url by seperating them with &
When running from the command line, make sure to pipe your output to a text file as follows:

```Shell
python twitterstream.py > example.txt 
```
