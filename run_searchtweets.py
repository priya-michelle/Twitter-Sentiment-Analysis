# https://github.com/twitterdev/search-tweets-python
# tweets are tweet_parser.tweet.Tweet

from searchtweets import load_credentials, gen_rule_payload, collect_results


def get_search_rule(query_term='', since='2019-07-24', count=100, lang='en', result_type='mixed'):
    # pt_rule = f"{query_term} has:geo"
    pt_rule=query_term
    rule = gen_rule_payload(pt_rule, results_per_call=count)
    return rule


# test comment please remove
if __name__ == '__main__':
    # expects a yaml file at ~/.twitter_keys.yaml
    premium_search_args = load_credentials("~/.twitter_keys.yaml", yaml_key="search_tweets_premium")
    rule = get_search_rule(query_term='biden')
    tweets = collect_results(rule, result_stream_args=premium_search_args)
