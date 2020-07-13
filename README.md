# Twitter-Sentiment-Analysis
Sentiment Analysis of Tweets, aggregated by location, visualized


## Modules

### Gather tweets
  - input: 
    - filter (could be hardcoded): includes political keywords, location, time
  - returns:
    - list of tweets


### Run Sentiment Analysis
  - input:
    - list of tweets
  - returns:
    - list of tuples [(tweet, sentiment)]


### Map tweets to county of origin, group by county
  - input:
    - list of tuples [(tweet, sentiment)]
  - returns:
    - list of tuples [(tweet, sentiment, location)]


### Aggregate political scores of tweets
  - input:
    - list of tuples [(tweet, sentiment, location)]
  - returns:
    - map of county names to political scores

### Visualize it
  - input:
    - map of counties to scores
  - returns:
    - visual