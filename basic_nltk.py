import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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
        sid = SentimentIntensityAnalyzer()
        sentiment = sid.polarity_scores(tweet)
        tweetSentiment.append((tweet, sentiment['compound']))
    return tweetSentiment

def sentimentAnalysisScore(tweets):
    
    """
    ###Name: sentimentAnalysis()
    ###Input: List of tweets (strings)
    ###Function: Takes parses list of tweets to analyze the sentiment of each individual tweet
    ###Output: List of tuples (tweet, sentiment) this includes other values
    """
    
    tweetSentiment = []
    for tweet in tweets:
        sid = SentimentIntensityAnalyzer()
        sentiment = sid.polarity_scores(tweet)
        tweetSentiment.append((tweet, sentiment))
    return tweetSentiment
    


print('Tweet with the compound score')
print(sentimentAnalysis(tweets))
print('====================================================')
print('====================================================')
print('Tweet with the compund score and values that aid in computation')
print(sentimentAnalysisScore(tweets))
