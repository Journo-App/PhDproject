from twitter import *
import json
import csv

#NEXT STEP: WHEN GET TO END OF THE WHILE LOOP, if the id == previous id then break, THEN STORE THE LAST ID 

#### REQUIRED CREDS FROM TWITTER API ####
deleted for the public version

#### SETS UP TWITTER API OBJECT FOR CALLS TO API ####
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#### GLOBAL VARIABLES ####
query = '#abortion' #### CHANGE THIS TO THE HASHTAG OR USER YOU WANT TO MINE TWEETS FROM ####
filename = 'abortion' #### OUTPUT FILE NAME ####
language = 'en' #### UNLESS YOU DONT WANT ENGLISH TWEETS KEEP SAME ####
tweetType = 'recent' #### DO YOU WANT RECENT, POPULAR OR BOTH KINDS OF TWEETS ####
numTweets = 100 #### NUMBER OF TWEETS TO GRAB FROM EACH RUN, 100 IS MAX ####
current = 0 #### SINCE THERE IS A LIMIT TO API CALLS, THIS SAVES SPOT IF YOU NEED TO CONTINUE AFTER API LIMIT IT HIT ####
runs = 0 #### EVERY API CALL WILL ADD TO THIS VALUE. ONCE IT IS EQUAL TO MAXRUNS, WILL STOP CALLING FROM API - LEAVE IT BE ####
maxRuns = 160 ### TWITTER ALLOWS YOU TO DO X CALLS TO API PER 15 MIN. SET HOW MANY RUNS YOU WANT HERE - ALTER DEPENDING ON HOW MANY RUNS YOU WANT####
tempData = [] #### GATHERS TWEETS ####
tweet = 0 #### VAIRABLE IS FOR THE PROCESS OF GRABBING TWEETS THAT END UP IN JSON FILE - LEAVE IT BE ####

while runs != maxRuns: #### CONTINUE TO RUN THE FOLLOWING CODE UNTIL RUNS IS EQUAL TO MAXRUNS ####
	curTweets = t.search.tweets(q=query, lang=language, result_type=tweetType, count=numTweets, exclude="retweets", include_entities=False, max_id=current) #### API CALL ####
	length = len(curTweets['statuses']) #### FIND OUT HOW MANY TWEETS WERE GATHERED ####
	current = curTweets['statuses'][length-1]['id'] #### UPDATE TWITTER POSITION, USE IF API LIMIT IS HIT ####
	print current #### IF API LIMIT IS HIT, REPLACE CURRENT VARIABLE AT TOP WITH THE LAST NUMBER THAT IS PRINTED BEFORE ERROR APPEARS IN CONSOLE ####
		
	i = 0
	while i < len(curTweets['statuses']): #### THIS LOOP WILL ONLY GRAB THE STATUS DATA YOU WANT FROM API CALL FOR JSON FILE ####
		#### GRAB TWEET ####
		tempData.insert(tweet, curTweets['statuses'][i])
		i += 1
		tweet += 1
	runs += 1
	
	
	with open(filename+'.json', 'w') as outfile: #### OUTPUTS API CALL TO A JSON FILE ####
		json.dump(tempData, outfile)	
		
		
