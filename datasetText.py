# -*- coding: utf-8 -*-
# suggested name: tweepyFlujoMonitor
import tweepy
from tweepy.api import API
import re

API_KEY = 'Dc2NOVqFvaBpuB43SKrmS9eEp'
API_SECRET = '4S1AZlHo54iE3J5WduEYstQKrsyU1NxB4cI9xZyg440G0syT5F'
ACCESS_TOKEN = '832210070092005376-lZ2XQgaCL2TMlzApGm19otkIkwn9g47'
ACCESS_TOKEN_SECRET = 'xagdUsqyHQWH7FFXWwwfxiojMYUN1I3XOd2wMHxSvrxao'
key = tweepy.OAuthHandler(API_KEY, API_SECRET)
key.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class Stream2File(tweepy.StreamListener):
    def __init__(self, api=None):
        self.api = api or API()
        self.n = 0
        self.m = 200
        self.output = open('text/travel_text.txt', 'w')

    def on_status(self, status):
        def processTweet(tweet):
        # process the tweets
        #Convert to lower case
            tweet = tweet.lower()
            #Convert www.* or https?://* to URL
            tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
            #Convert @username to AT_USER
            tweet = re.sub('@[^\s]+','AT_USER',tweet)
            #Remove additional white spaces
            tweet = re.sub('[\s]+', ' ', tweet)
            #Replace #word with word
            tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
            #trim
            tweet = tweet.strip('\'"')
            return tweet

        # self.output.write((status.text.encode('utf8') + b"\n").decode('utf-8'))
        # self.output.write(status.text.encode('utf8') + "\n")
        processedTweet = processTweet(status.text)
        self.output.write((processedTweet.encode('utf8') + b"\n").decode('utf-8'))
        self.n = self.n+1
        if self.n < self.m: return True
        else:
            self.output.close()
            print ('tweets = '+str(self.n))
            return False

stream = tweepy.streaming.Stream(key, Stream2File())
stream.filter(track=['travel'], languages=['en'])