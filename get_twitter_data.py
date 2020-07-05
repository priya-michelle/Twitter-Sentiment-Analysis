from twitter_utils import get_tweets

def get_biden_tweets():
    return get_tweets(query='biden')

def get_trump_tweets():
    return get_tweets(query='trump')

def get_political_tweets():
    query_tweet_map = {}
    query_tweet_map['biden'] = get_biden_tweets()
    query_tweet_map['trump'] = get_trump_tweets()
    return query_tweet_map

# only include this for testing purposes
if __name__ == '__main__':
    print(get_political_tweets())
