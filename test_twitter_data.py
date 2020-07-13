import pickle

from twitter.models import Status

from get_twitter_data import get_political_tweets

pickle_filename = "poli_tweets_fixture.pkl"

def pickle_fixture():
    twitter_results = get_political_tweets()
    with open(pickle_filename, 'wb') as f:
        pickle.dump(twitter_results, f)

def load_test_data():
    with open(pickle_filename, 'rb') as f:
        return pickle.load(f)

# run some basic tests on the test data fixture
# fixture is a dictionary with 2 keys, trump and biden
# each value is a list of tweets
# tweets have type twitter.models.Status
def test_test_data():
    test_data = load_test_data()
    assert 'biden' in test_data
    assert 'trump' in test_data

    biden_tweets = test_data['biden']
    trump_tweets = test_data['trump']
    assert len(biden_tweets) == 100
    assert len(trump_tweets) == 100

    example_tweet = biden_tweets[0]
    assert isinstance(example_tweet, Status)