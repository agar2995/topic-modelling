#!/usr/bin/env python
# encoding: utf-8
from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
from gensim.models import Word2Vec
import tweepy 
import csv
import pandas as pd
import re

#Twitter API credentials
consumer_key = "Dc2NOVqFvaBpuB43SKrmS9eEp"
consumer_secret = "4S1AZlHo54iE3J5WduEYstQKrsyU1NxB4cI9xZyg440G0syT5F"
access_key = "832210070092005376-lZ2XQgaCL2TMlzApGm19otkIkwn9g47"
access_secret = "xagdUsqyHQWH7FFXWwwfxiojMYUN1I3XOd2wMHxSvrxao"

@app.route("/")
def chart():
    
	return render_template('chart.html')

@app.route('/result', methods = ['POST', 'GET'])

def result():

	if request.method == 'POST':

		# labels = ["Sports","Politics","Films","blah","Porn","Tvseries","Education","Laundiyabazi","bb","dddd","ddddddd"]
		# values = [0,9,8,7,5.879,4,7,8,4,3,2]
		result = request.form
		# return render_template("chart.html",result = result, values=values, labels=labels)
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
		screen_name = request.form['Name']
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_key, access_secret)
		api = tweepy.API(auth)
		
		#initialize a list to hold all the tweepy Tweets
		alltweets = []	
		
		#make initial request for most recent tweets (200 is the maximum allowed count)
		new_tweets = api.user_timeline(screen_name = screen_name,count=200)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#save the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		#keep grabbing tweets until there are no tweets left to grab
		# while len(new_tweets) > 0:
		# 	print ("getting tweets before %s" % (oldest))
			
		# 	#all subsiquent requests use the max_id param to prevent duplicates
		# 	new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
			
		# 	#save most recent tweets
		# 	alltweets.extend(new_tweets)
			
		# 	#update the id of the oldest tweet less one
		# 	oldest = alltweets[-1].id - 1
			
		# 	print ("...%s tweets downloaded so far" % (len(alltweets)))
		
		#transform the tweepy tweets into a 2D array that will populate the csv	
		outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
		
		#write the csv	
		# with open('%s_tweets.csv' % screen_name, 'wb') as f:
		with open('userTweets/%s_tweets.csv' % screen_name, 'w') as f:
			writer = csv.writer(f)
			writer.writerow(["id","created_at","text"])
			writer.writerows(outtweets)
		
		pass

		df = pd.read_csv('userTweets/%s_tweets.csv' % screen_name)
		saved_column = df.text
		# print (saved_column)

		f = open('tweetText/%s_tweets.txt' % screen_name, 'w')
		for line in saved_column:
			f.write(" " + line)
		f.close()

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

		def getFeatureVector(tweet):

			def getStopWordList(stopWordListFileName):
			#read the stopwords file and build a list
				stopWords = []
				stopWords.append('AT_USER')
				stopWords.append('URL')

				fp = open(stopWordListFileName, 'r')
				line = fp.readline()
				while line:
					word = line.strip()
					stopWords.append(word)
					line = fp.readline()
				fp.close()
				return stopWords


			def replaceTwoOrMore(s):
			    #look for 2 or more repetitions of character and replace with the character itself
				pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
				return pattern.sub(r"\1\1", s)

			stopWords = []
			st = open('stop_words_list.txt', 'r')
			stopWords = getStopWordList('stop_words_list.txt')
	        
			featureVector = []
			#split tweet into words
			words = tweet.split()
			for w in words:
				#replace two or more with two occurrences
				w = replaceTwoOrMore(w)
				#strip punctuation
				w = w.strip('\'"?,.')
				#check if the word stats with an alphabet
				val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
				#ignore if it is a stop word
				if(w in stopWords or val is None):
					continue
				else:
					featureVector.append(w.lower())
			return featureVector

		f = open('tweetText/%s_tweets.txt' % screen_name, 'r')

		processedTweet = processTweet(f.readline())
		featureVector = getFeatureVector(processedTweet)
		# for item in featureVector:
		# 	print (item)
		sentence = (" ".join(featureVector))
		# print ([sentence.split()])
		# print (["minimization statistics classification deep software decreases stanfor".split()])
		model = []
		model.append(Word2Vec.load('model/bollywoodModel'))
		model.append(Word2Vec.load('model/hollywoodModel'))
		model.append(Word2Vec.load('model/musicModel'))
		model.append(Word2Vec.load('model/politicsModel'))
		model.append(Word2Vec.load('model/scienceModel'))
		model.append(Word2Vec.load('model/sportModel'))
		model.append(Word2Vec.load('model/travelModel'))

		topics = ['Bollywood', 'Hollywood', 'Music', 'Politics', 'Science', 'Sports', 'Travel']
		values = []
		for model in model:
			vocab = list(model.wv.vocab.keys())
			# print (vocab)
			# print ("\n\n")
		# 	# print (model)
			values.append(abs(model.score([sentence.split()]))/30)

		labels = ["Bollywood", "Hollywood", "Music", "Politics", "Science", "Sports", "Travel"]
		# values = [0,9,8,7,5.879,4,7,8,4,3,2]

		return render_template("chart.html", result=result, values_topics=zip(values, topics), values=values, labels=labels)

if __name__ == '__main__':
	#pass in the username of the account you want to download
	# get_all_tweets("@UniofOxford")
	app.debug = True
	app.run(host='0.0.0.0', port=5001)