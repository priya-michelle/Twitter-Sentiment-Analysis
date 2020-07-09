import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentence = 'I am not annoyed'

sid = SentimentIntensityAnalyzer()
score = sid.polarity_scores(sentence)
print('Polarity Score: ', score)