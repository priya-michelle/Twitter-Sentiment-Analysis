import os

import twitter

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

assert (consumer_key and consumer_secret and access_token and access_token_secret), "Must have key/secret env vars set!"

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

results = api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")
print(results)
