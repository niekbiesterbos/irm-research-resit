import os
import re
import csv


def process_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            fields = line.split()
            tweet_id = fields[0]
            hashtags = re.findall(r'#\w+', line)
            retweet_ids = re.findall(r'\d+', line)
            retweet = len(retweet_ids) > 1
            data.append([tweet_id, len(hashtags), retweet])
    return data


def process_files(directory):
    all_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            data = process_file(file_path)
            all_data.extend(data)
    return all_data


directory = './tweets'

data = process_files(directory)

output_file = 'tweet_analysis.csv'

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tweet ID', 'Hashtags', 'Contains Retweet'])
    writer.writerows(data)
