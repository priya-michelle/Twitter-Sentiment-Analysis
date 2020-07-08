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

def _get_geocode_param():
    """
    We're using the coordinates of Tampa, with a radius of 334mi (distance tampa-pensacola).
    This roughly corresponds to tweets from Florida.  More fine-grained filtering can be done downstream.
    """
    return "27.9506,-82.4572,334mi"

def get_tweets(query='', since='2019-07-24', count=100, lang='en', result_type='mixed'):
    """ Return tweets that match a given query

    Given a query string, and optionally other search criteria, get a list of relevant tweets
    Default to only returning tweets newer than July 24th 2019, in English.
    Only return tweets that are geo-tagged.  The geocode param has the form latitude,longitude,radius.

    See api docs for standard search: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets

    General twitter search documentation: https://developer.twitter.com/en/docs/tweets/search/overview
    
    TODO maybe use **kwargs instead of specifying each individually
    """
    api = _get_api()

    geo_param = _get_geocode_param()

    query_string = f"q={query}&result_type={result_type}&since={since}&count={count}&lang={lang}"
    results = api.GetSearch(raw_query=query_string)
    return results


# include this just to test the script
if __name__ == '__main__':
    biden_tweets = get_tweets(query='biden')
    print(biden_tweets)
