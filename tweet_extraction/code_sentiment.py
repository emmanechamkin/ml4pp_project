import pandas as pd
import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import emoji
from emoji.unicode_codes import UNICODE_EMOJI
import re
import requests
import os
from creds import *


def parse(word):
    word = word.strip().lower().translate(TABLE)
    if word in UNICODE_EMOJI:
        word = re.sub("_", " ", UNICODE_EMOJI[word][1:-1]).lower()
    if (word.startswith("rt")
            or word.startswith("@")
            or "http" in word
            or word in STOP_WORDS):
        word = ""
    if word.startswith("#"):
        word = word[1:]
    return word


def ping_server(tweet_keep, server_url=SERVER_URL, parameters=PARAMS):
    tweet_keep = tweet_keep.encode(encoding='utf-8')
    r = requests.post(SERVER_URL, data=tweet_keep, params=PARAMS)
    sentiment = r.json()["sentences"][0]["sentiment"]
    return [tweet_keep, sentiment]

if __name__ == "__main__":
    STOP_WORDS = set(stopwords.words('english'))
    TABLE = str.maketrans({key: None for key in string.punctuation})

    with open(INPUT, "r") as csv_file, \
            open(CLEANED, "w", newline="") as out_file:
        reader = csv.reader(csv_file, delimiter=",")
        writer = csv.writer(out_file, delimiter=",")
        tweet_set = set()
        count = 0 
        for row in reader:
            if count % 1000 == 0:
                print(f"On unique tweet {count}")
            labeled = []
            tweet_keep = ""
            tweet = row[0]
            if tweet not in tweet_set:
                tweet_set.add(tweet)
                count += 1
                for word in tweet.split():
                    word = parse(word)
                    if word:
                        tweet_keep += " " + word
            if tweet_keep:
                try:
                    assert count < 100
                    labeled = ping_server(tweet_keep)
                except:
                    break
                writer.writerow(labeled)
                except: #add error here
                    print("Ping failed", tweet_keep)
                    # print("Terminating instances...")
                    # os.system(f"aws ec2 terminate-instances --instance-ids {EC2_ID} --profile ml4pp")

    print("Terminating instances...")
    os.system(f"aws ec2 terminate-instances --instance-ids {EC2_ID} --profile ml4pp")
    print("Complete!")