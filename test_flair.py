from flair.models import TextClassifier
from flair.data import Sentence
classifier = TextClassifier.load('en-sentiment')  # a pre-trained LSTM model
sentence = Sentence('I am so annoyed')
classifier.predict(sentence)# print sentence with predicted labels
print('Sentence above is: ', sentence.labels)
print(type(sentence.labels))

print(sentence.labels[0].to_dict())
