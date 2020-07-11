

class SimpleTweet:

    def __init__(self, raw_text, known_label=None):
        self.raw_text = raw_text
        self.clean_text = self._sanitize(raw_text)
        self.known_label = known_label

    # TODO implement sanitize
    def _sanitize(self, value):
        return value


def create_simple_tweets_from_df(input_df):
    """Create a list of SimpleTweet from a df of labeled tweets
    input_df has columns 'tweet' and 'actual_label'
    """
    st_list = []
    for _, row in input_df.iterrows():
        st_list.append(SimpleTweet(row['tweet'], known_label=row['actual_label']))
    return st_list