# The Effect of Hashtag Usage on Retweet Probability in Dutch Tweets


## General Information

This project examines the impact of hashtag usage on the probability of a tweet being retweeted, with the focus on Dutch tweets. The analysis uses a dataset from Rijksuniversiteit Groningen, and it was found that the optimal amount of hashtags for the highest chance of being retweeted are 1, 4, or 6.

## Background Information

Several studies have explored the topic of this project. The first one is by Suh et al. (2010) titled "Want to be retweeted? large scale analytics on factors impacting retweet in Twitter network". They found a strong relationship between the use of hashtags and retweetability.

The second one is "Credibility in Context: An Analysis of Feature Distributions in Twitter" by O'Donovan et al. (2012). This study delves into the topic of credibility in the context of Twitter features distributions.

## Research Question and Hypotheses

The primary research question of this project is: "Does the number of hashtags used in a Dutch tweet affect its probability of being retweeted?"

The hypothesis is:

- A higher number of hashtags in a tweet increases its probability of being retweeted.

## Method

The project uses the Dutch Tweet Corpus provided by Rijksuniversiteit Groningen. The dataset was selectively trimmed to include tweets from every 1st, 7th, 14th, and 21st day of each month, captured at 12:00 each day, which allows a randomized, reproducible sampling of the data. The main variables are the number of hashtags (independent variable) and the occurrence of retweets (dependent variable). The analysis involves computing the proportion of retweets for different numbers of hashtags used in the tweets. We have used the Tweet2tab tool from the RUG. 


## Prerequisites

The following Python libraries are required for this project:

- pandas
- tabulate

Install them using pip:

```
pip install pandas tabulate

```


## Data Collection

To collect the data, you need to run `extract_tweets.sh` on the Karora server:

```bash
./extract_tweets.sh

```

This script outputs a folder named 'tweets'.

## Data Preprocessing
After collecting the data, you need to run the Python script `tweets_to_csv.py` on the 'tweets' folder:
``` 
python3 tweets_to_csv.py tweets 

```

This script converts the tweet data into a CSV file, which is used in the next step.

## Data Analysis
Finally, run the `analyze_tweets.py` script on the generated .csv file to get the results:
```
python3 analyze_tweets.py data.csv

```

The results will be outputted to the console, showing the relationship between the number of hashtags used in a tweet and the proportion of such tweets that get retweeted.

## References

- Suh, B., Hong, L., Pirolli, P., & Chi, E. H. (2010, August). Want to be retweeted? large scale analytics on factors impacting retweet in Twitter network. In 2010 IEEE second international conference on social computing (pp. 177-184). IEEE.

- O'Donovan, J., Kang, B., Meyer, G., Höllerer, T., & Adalii, S. (2012). Credibility in Context: An Analysis of Feature Distributions in Twitter. In 2012 International Conference on Privacy, Security, Risk and Trust and 2012 International Confernece on Social Computing (pp. 293-301). IEEE.