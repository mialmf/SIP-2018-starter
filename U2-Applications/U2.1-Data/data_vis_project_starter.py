'''
In this program, we store the polarities and subjectivities of all the tweets.
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#Create a Sentiment List
data = '{tweet_small.json}'
json_string = json.dumps(data)
polarityLIst = []
subjectivityList = []
tweettext = []
tweetstring = ''

#Get Sentiment Data
for tweet in tweetData:
    tweetstring += tweet['text']
    #print(tweetstring)

for tweet in tweetData:
	tweetblob = TextBlob(tweet["text"])
	polarityLIst.append(tweetblob.polarity)

for tweet in tweetData:
    tweetblob = TextBlob(tweet['text'])
    subjectivityList.append(tweetblob.subjectivity)
tweetBlob = TextBlob(tweetstring)
word_dict = {}

for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]

print(word_dict)

my_list = polarityLIst
o_list = subjectivityList
#print(sum(my_list)/len(my_list))
#print(sum(o_list)/len(o_list))

#plt.hist(my_list, bins=[-1, -0.9, -0.8, -0.7, -0.6, -0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
#plt.xlabel('Values')
#plt.ylabel('Number of Items')
#plt.title('Histogram of Numbers')
#plt.axis([-1.0, 1.0, 0, 100])
#plt.grid(True)
#plt.show()