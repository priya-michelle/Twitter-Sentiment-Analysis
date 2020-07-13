from flair.models import TextClassifier
from flair.data import Sentence
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
        sentence = Sentence(tweet)
        classifier.predict(sentence) # classify the tweet
        sentiment_analysis = sentence.labels[0].value # label contains both value and score
        
        if (sentiment_analysis == 'POSITIVE'):
            tweetSentiment[i] = int(4)
        else:
            tweetSentiment[i] = int(0)
        i= i + 1
    return tweetSentiment

classifier = TextClassifier.load('en-sentiment')


tweets = sentiment.tweet.tolist()

sentiment.predicted_label = sentimentAnalysis(tweets)


print(sentiment.head())
print(sentiment.shape)


acc = accuracy_score(sentiment.actual_label, sentiment.predicted_label)

print('The accuracy is: ', acc)