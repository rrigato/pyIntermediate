'''
Handling the json text file that tweets come in.
'''
import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_path = '../downloads/talkhoops3.txt'

#initialize a list and open a file for reading
tweets_data = []
with open(tweets_path, "r") as tweets_file:
	for line in tweets_file:
		try:
			tweet = json.loads(line)
			tweets_data.append(tweet)
		except:
			print('Error: Unable to read line')
			continue
			
print(len(tweets_data))
