from twitter import *
import json
import csv

#NEXT STEP: WHEN GET TO END OF THE WHILE LOOP, if the id == previous id then break, THEN STORE THE LAST ID 

#### REQUIRED CREDS FROM TWITTER API ####
c_key = ''
c_secret = ''
t_key = ''
t_secret = ''
#### SETS UP TWITTER API OBJECT FOR CALLS TO API ####
t = Twitter(
    auth=OAuth(
        consumer_key=c_key,
        consumer_secret=c_secret,  
        token=t_key,  
        token_secret=t_secret
    )
)

#### GLOBAL VARIABLES ####
query = '#abortion' #### CHANGE THIS TO THE HASHTAG OR USER YOU WANT TO MINE TWEETS FROM ####
filename = 'abortion' #### OUTPUT FILE NAME ####
language = 'en' #### UNLESS YOU DONT WANT ENGLISH TWEETS KEEP SAME ####
tweetType = 'recent' #### DO YOU WANT RECENT, POPULAR OR BOTH KINDS OF TWEETS ####
numTweets = 100 #### NUMBER OF TWEETS TO GRAB FROM EACH RUN, 100 IS MAX ####
Runs = 160 ### TWITTER ALLOWS YOU TO DO X CALLS TO API PER 15 MIN. SET HOW MANY RUNS YOU WANT HERE - ALTER DEPENDING ON HOW MANY RUNS YOU WANT####
tempData = [] #### GATHERS TWEETS ####


curTweets = t.search.tweets(
    q=query,  
    lang=language,  
    result_type=tweetType,  
    count=numTweets,  
    exclude="retweets",  
    include_entities=False
)

allData = curTweets['statuses']
num_tweets = len(curTweets['statuses'])
print ('... found', num_tweets, 'tweets')

if curTweets['search_metadata'].has_key('next_results'):
    length = len(curTweets['statuses'])
    current = curTweets['statuses'][length - 1]['id']
    more = True
    print ('... looking for more tweets after id ', current)
else:
    print ('... that\'s all!')
    more = False

while more is True:
    curTweets = t.search.tweets(
        q=query,
        lang=language,
        result_type=tweetType,
        count=numTweets,
        exclude="retweets",
        include_entities=False,
        max_id=current
    )
     
    num_tweets = len(curTweets['statuses'])
    print ('... found', num_tweets, 'tweets')

    allData.extend(curTweets['statuses'])
     
    if curTweets['search_metadata'].has_key('next_results'):
        length = len(curTweets['statuses'])
        current = curTweets['statuses'][length - 1]['id']
        more = True
        print ('... looking for more tweets after id ', current)
    else:
        print ('... that\'s all!')
        more = False


# # remove duplicates with numpy
# import numpy as np
# results = np.unique(allData).tolist()

# save results to file
	
	
    with open(filename+'.json', 'w') as outfile: #### OUTPUTS API CALL TO A JSON FILE ####
        json.dump(tempData, outfile)	
		
		
