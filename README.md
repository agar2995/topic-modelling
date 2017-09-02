Synopsis:
This project aims at classifying tweets of a given user into a set of pre-defined topics, using machine learning techniques. 

Installations:
--tweepy
--pandas
--flask
--gensim
--word2vec
--wikipedia
Command: pip install *any of the above*

Platform: python 3.5

Steps:
--run datasetText.py with a filter query word to get the latest 200 tweets corresponding to that word.
--run modelTrain.py to create and save a model for the specific text file of tweets generated from the above script.
  This is the dataset and trained model
--run modelTest.py. This would start a local server to run flask that connects the script to the front end. Go to localhost:5001 in your web browser and enter the twitter handle of the user you wish to classify tweets of.
--this would generate a graphical and tabular representation of the user's tweets classification into various topics.

Directory Structure:
--model contains all the trained word2vec models.
--text contains all the retrieved text files corresponding to respective filter words.
--tweetText contains recent 200 tweets of the specific user in text format.
--userTweets contains recent 200 tweets of the specific user in pre-processed csv format.
--templates contains chart.html to edit the front end display of the application.

Contributors
Aman Agarwal (https://github.com/agar2995)
Nihal Gurjar
