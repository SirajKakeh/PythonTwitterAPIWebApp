from flask import Flask
from flask import request
from flask_cors import CORS
from tweepy.streaming import StreamListener
from tweepy import Stream
import tweepy
from twython import Twython
import time
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import json
app = Flask(__name__)
CORS(app)

# # api = twitter.Api(
# #     consumer_key='hwTgC9EPKDhOCfxG2HFPX5xkX',
# #     consumer_secret='J2ipi1skgYiiTDptFkPXW2PbMCw8XZ3pwyViaQAvTQbbOB54rM',
# #     access_token_key='122389961-QPSF5f9mDJ99mP1cl3zJtELhjmySK0g60P8j1RJf',
# #     access_token_secret='S6iIs9pp22owT6l6BH5TLY256PfOU4GtXetDqer8c0kIm')

# try:
#     import json
# except ImportError:
#     import simplejson as json

# # Import the necessary methods from "twitter" library
# from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# # Variables that contains the user credentials to access Twitter API 
#  ACCESS_TOKEN = '122389961-rt1AkthMjlAEb6RbDpUo8GvfopYYfDLCpQDchAFN'
# #  '122389961-QPSF5f9mDJ99mP1cl3zJtELhjmySK0g60P8j1RJf"'


# ACCESS_SECRET = 'PXI7KLYGy33WmrnaxHzFJmw79N9yH5PgAIFyD52IDNNUD'
# # 'S6iIs9pp22owT6l6BH5TLY256PfOU4GtXetDqer8c0kIm'

# CONSUMER_KEY = 'zlHSEOcRXszheIurATDbV2oUl'
# CONSUMER_SECRET = '8H7oIwJgfF5S8OMtvMn5VWITTIiYSmBCrv4g8HVWgV5pUGSpkd'

# oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# # Initiate the connection to Twitter Streaming API
# twitter_stream = TwitterStream(auth=oauth)

# # Get a sample of the public data following through Twitter
# iterator = twitter_stream.statuses.sample()

# # Print each tweet in the stream to the screen 
# # Here we set it to stop after getting 1000 tweets. 
# # You don't have to set it to stop, but can continue running 
# # the Twitter API to collect data for days or even longer. 
# tweet_count = 1000
# for tweet in iterator:
#     tweet_count -= 1
#     # Twitter Python Tool wraps the data returned by Twitter 
#     # as a TwitterDictResponse object.
#     # We convert it back to the JSON format to print/score
#     print json.dumps(tweet)  
    
#     # The command below will do pretty printing for JSON data, try it out
#     # print json.dumps(tweet, indent=4)
       
#     if tweet_count <= 0:
#         break 





# # @app.route('/')
# # def route():
# #     return 'Hello, World!'

# # @app.route('/gettweets', methods=['GET', 'OPTIONS'])
# # def returnTweets():
# #     return 'Nah!'

# # app.run(use_reloader=True)


# try 2
#!/usr/bin/python
#-----------------------------------------------------------------------
# twitter-user-timeline
#  - displays a user's current timeline.
#-----------------------------------------------------------------------

# from twitter import *

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
# twitter = Twitter(
# 		auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

#-----------------------------------------------------------------------
# this is the user we're going to query.
#-----------------------------------------------------------------------
# user = "ideoforms"

#-----------------------------------------------------------------------
# query the user timeline.
# twitter API docs:
# https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
# results = twitter.statuses.user_timeline(screen_name = user)

#-----------------------------------------------------------------------
# loop through each status item, and print its content.
#-----------------------------------------------------------------------
# for status in results:
# 	print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))

# results = twitter.oauth.access_token()

# for location in results:
# 	for trend in location["trends"]:
# 		print " - %s" % trend["name"]

# try3


auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_key"], config["access_secret"])

# api = tweepy.API(auth)
# statuses = range(0,19)
# public_tweets = api.home_timeline()
# i=0
# for tweet in public_tweets:
#     statuses[i]=tweet
#     i=i+1
#     print tweet.text
# string = str(public_tweets)
# print(string)

# #override tweepy.StreamListener to add logic to on_status



# class MyStreamListener(tweepy.StreamListener):
#     def on_status(self, status):
#         print status

# @app.route('/gettweets', methods=['GET', 'OPTIONS'])
# def returnTweets():
#     return string

# app.run(use_reloader=True)

#try 4

#Import the necessary methods from tweepy library


#Variables that contains the user credentials to access Twitter API 
access_token = "122389961-rt1AkthMjlAEb6RbDpUo8GvfopYYfDLCpQDchAFN"
access_token_secret = "PXI7KLYGy33WmrnaxHzFJmw79N9yH5PgAIFyD52IDNNUD"
consumer_key = "zlHSEOcRXszheIurATDbV2oUl"
consumer_secret = "8H7oIwJgfF5S8OMtvMn5VWITTIiYSmBCrv4g8HVWgV5pUGSpkd"

#This is a basic listener that just prints received tweets to stdout.
# class StdOutListener(StreamListener):    
#     def on_data(self, data):
#         print(data)
#         return True
    
#     def on_error(self, status):
#         print(status)
        
# # if __name__ == '__main__':
# #This handles Twitter authetification and the connection to Twitter Streaming API
# l = StdOutListener()
# stream = Stream(auth, l)

# #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
# stream.filter(track=['lovetwitter'])
# app.run(use_reloader=True)

# try 5

APP_KEY = 'zlHSEOcRXszheIurATDbV2oUl'
APP_SECRET = '8H7oIwJgfF5S8OMtvMn5VWITTIiYSmBCrv4g8HVWgV5pUGSpkd'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
print (ACCESS_TOKEN)

APP_KEY = 'zlHSEOcRXszheIurATDbV2oUl'             
ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAL%2Bk3AAAAAAA8i2II4YkkUxCj5PN05Jqo%2B2eY6c%3D0A5BTusdf25Amld5Z459ViApMh2flZv8PLm7FyCVskAvIXEgpC'   #COPY AND PASTE FROM OUTPUT FROM ABOVE COMMAND
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
twitter.get_application_rate_limit_status()['resources']['search']

#RETRIEVING REAL TIME STREAMING TWEETS ABOUT BLOCKCHAIN 
search = twitter.search(q='a', count=2000, result_type='mixed' )
tweets = search['statuses']
#for tweet in tweets:
#print (tweet['id_str'], '\n', tweet['text'], tweet['favorite_count'], tweet['retweet_count'] ), '\n\n\n'
ids = []
#for tweet in tweets:
#ids.append(tweet['id_str'])
# ids = [tweet['id_str'] for tweet in tweets]
texts = [tweet['text'] for tweet in tweets]
# times = [tweet['retweet_count'] for tweet in tweets]
# favtimes = [tweet['favorite_count'] for tweet in tweets]
# follower_count = [tweet['user']['followers_count'] for tweet in tweets]
# location = [tweet['user']['location'] for tweet in tweets]
screenNames = [tweet['user']['screen_name'] for tweet in tweets]
usernames = [tweet['user']['name'] for tweet in tweets]
userPics = [tweet['user']['profile_image_url'] for tweet in tweets]
lang = [tweet['lang'] for tweet in tweets]
#CORRELATION BETWEEN RETWEET AND FAVORITE COUNTS AND PLOT IT

# %matplotlib inline 

pl = {
    'screenNames': screenNames,
    'usernames': usernames,
    'text': texts,
    'userPics': userPics,
}

@app.route('/gettweets', methods=['GET', 'OPTIONS'])
def returnTweets():
    print(texts)
    return json.dumps(pl)

app.run(use_reloader=True)