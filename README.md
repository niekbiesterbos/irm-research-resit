# The Effect of Hashtag Usage on Retweet Probability in Dutch Tweets

This project investigates the impact of hashtag usage on the likelihood of a tweet being retweeted, based on a dataset of Dutch tweets provided by Rijksuniversiteit Groningen. The main finding suggests that using 1, 4, or 6 hashtags is optimal for maximizing the chance of a tweet being retweeted.

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