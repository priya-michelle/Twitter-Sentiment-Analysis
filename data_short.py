import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sent140 = pd.read_csv('sent140_short.csv')
print(sent140.head())

column_names = ["tweet", "actual_label", "predicted_label"]
sentiment = pd.DataFrame(columns = column_names)

sentiment.tweet = sent140.tweet
sentiment.actual_label = sent140.actual_label
print(sentiment.head())

print(sentiment.shape)

sentiment = sentiment[sentiment.actual_label != 2]

print(sentiment.head())
print(sentiment.shape)