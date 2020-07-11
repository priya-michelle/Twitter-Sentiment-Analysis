import pickle

import pandas as pd

from simple_tweet import create_simple_tweets_from_df

training_data_csv = 'trainingandtestdata/testdata.manual.2009.06.14.csv'
column_names = ['actual_label', 'id', 'timestamp', 'keyword', 'user', 'tweet']

out_pkl_file = 'labled_simple_tweets.pkl'

def get_training_df(csv_file):
    df = pd.read_csv(csv_file, names=column_names)
    return df

def get_st_list(input_df):
    return create_simple_tweets_from_df(input_df)


def write_pkl(st_list):
    with open(out_pkl_file, 'wb') as f:
        pickle.dump(st_list, f)


if __name__ == '__main__':
    df = get_training_df(training_data_csv)
    st_list = create_simple_tweets_from_df(df)
    write_pkl(st_list)
