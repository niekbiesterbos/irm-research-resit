import pandas as pd
from tabulate import tabulate


def calculate_proportion_data(df):
    ''' Calculate the proportion of retweets for tweets with and without hashtags '''
    total_tweets = df.shape[0]
    total_with_hashtags = len(df[df['Hashtags'] > 0])
    total_with_retweets = len(df[df['Contains Retweet'] == True])
    total_with_hashtags_and_retweets = len(
        df[(df['Hashtags'] > 0) & (df['Contains Retweet'] == True)])

    proportion_retweets_with_hashtags = total_with_hashtags_and_retweets / total_with_hashtags
    proportion_retweets_without_hashtags = (
        total_with_retweets - total_with_hashtags_and_retweets) / (total_tweets - total_with_hashtags)

    print("Total Proportion of Retweets with Hashtags:",
          proportion_retweets_with_hashtags)
    print("Total Proportion of Retweets without Hashtags:",
          proportion_retweets_without_hashtags)


def analyze_hashtags_and_retweets(df):
    hashtag_groups = df.groupby('Hashtags')
    hashtag_counts = hashtag_groups.size()
    proportion_data = hashtag_groups['Contains Retweet'].mean()

    result_df = pd.DataFrame({'Amount of Hastags': hashtag_counts.index,
                             'Amount of Tweets': hashtag_counts.values, 'Proportion of Retweets': proportion_data.values})

    table = tabulate(result_df, headers='keys',
                     tablefmt='pipe', showindex="never")

    print("|   Proportion of Retweets for Different Number of Hashtags:")
    print(table)


def main():
    csv_file = 'tweet_analysis.csv'
    df = pd.read_csv(csv_file)
    print("-----------------------------------------------------------------------")
    calculate_proportion_data(df)
    print("-----------------------------------------------------------------------")
    analyze_hashtags_and_retweets(df)
    print("-----------------------------------------------------------------------")


if __name__ == "__main__":
    main()
