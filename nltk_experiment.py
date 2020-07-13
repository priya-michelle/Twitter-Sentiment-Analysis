import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from data_short import sentiment

##imports

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
#import seaborn as sns; sns.set()
#import scipy.stats as ss


def sentimentAnalysis(tweets):
    
    """
    ###Name: sentimentAnalysis()
    ###Input: List of tweets (strings)
    ###Function: Takes parses list of tweets to analyze the sentiment of each individual tweet
    ###Output: List of tuples (tweet, sentiment)
    """
    
    tweetSentiment = np.empty(len(tweets), np.int8)
    i = 0
    for tweet in tweets:
        sia = SentimentIntensityAnalyzer()
        sentiment_analysis = sia.polarity_scores(tweet)
        
        if (sentiment_analysis['compound'] > 0):
            tweetSentiment[i] = 4
        elif (sentiment_analysis['compound'] < 0):
            tweetSentiment[i] = 0
        i= i + 1
    return tweetSentiment


tweets = sentiment.tweet.tolist()

sentiment.predicted_label = sentimentAnalysis(tweets)


print(sentiment.head())
print(sentiment.shape)

print(type(sentiment.actual_label[1]))
print(type(sentiment.predicted_label[1]))

acc = accuracy_score(sentiment.actual_label, sentiment.predicted_label)

print('The accuracy is: ', acc)