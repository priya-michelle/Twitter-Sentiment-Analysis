from flair.models import TextClassifier
from flair.data import Sentence
classifier = TextClassifier.load('en-sentiment')  # a pre-trained LSTM model




tweets = ['I am so annoyed', 'I am so happy!', 'I love Joe Biden', 'I hate Donald Trump', 'I am neutral.']


def sentimentAnalysis(tweets):
    
    """
    ###Name: sentimentAnalysis()
    ###Input: List of tweets (strings)
    ###Function: Takes parses list of tweets to analyze the sentiment of each individual tweet
    ###Output: List of tuples (tweet, sentiment)
    """
    
    tweetSentiment = []
    for tweet in tweets:
        sentence = Sentence(tweet)
        classifier.predict(sentence) # classify the tweet
        sentiment = sentence.labels[0].value # label contains both value and score
        tweetSentiment.append((tweet, sentiment))
    return tweetSentiment 


def sentimentAnalysisScore(tweets):
    
    """
    ###Name: sentimentAnalysisScore()
    ###Input: List of tweets (strings)
    ###Function: Takes parses list of tweets to analyze the sentiment of each individual tweet
    ###Output: List of tuples (tweet, sentiment)  This includes confidence of the label
    """
    
    tweetSentiment = []
    for tweet in tweets:
        sentence = Sentence(tweet)
        classifier.predict(sentence) # classify the tweet
        sentiment = sentence.labels # label contains both value and score
        tweetSentiment.append((tweet, sentiment))
    return tweetSentiment 
    
print('Tweet with the positive or negative value assigned')
print(sentimentAnalysis(tweets))
print('====================================================')
print('====================================================')
print('Tweet with the positive or negative value assigned and confidence of that score')
print(sentimentAnalysisScore(tweets))
