import os

import twitter


def _get_api():
    consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
    consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)
    return api

def get_tweets(query='', since='2019-07-24', count=100, lang='en', result_type='mixed'):
    # TODO add filters
    # TODO maybe use **kwargs instead
    api = _get_api()
    query_string = f"q={query}&result_type={result_type}&since={since}&count={count}&lang={lang}"
    results = api.GetSearch(raw_query=query_string)
    return results


# include this just to test the script
if __name__ == '__main__':
    biden_tweets = get_tweets(query='biden')
    print(biden_tweets)
