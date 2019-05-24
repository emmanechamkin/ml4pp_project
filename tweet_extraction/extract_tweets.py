"""
extract raw tweets from twitter feeds

- Creds.py stores all credentials to access API
"""

import tweepy
import csv
import time
import random
import sys
import creds


def set_up_api():
    token = creds.access_token
    secret_token = creds.access_secret_token
    key = creds.API_key
    secret_key = creds.API_secret_key
    auth = tweepy.OAuthHandler(key, secret_key)
    auth.set_access_token(token, secret_token)
    api = tweepy.API(auth)
    return api


def run_queries(queries, api):
    tweets = []
    for q_ in queries:
        sleeper_min = random.randint(15, 25)
        time.sleep(sleeper_min * 60)
        try:
            for tweet in tweepy.Cursor(api.search,
                                    q=q_,
                                    count=100,
                                    result_type="recent",
                                    include_entities=True,
                                    lang="en").items():
             tweets.append(tweet.text)
        except tweepy.TweepError as e:
            print(e, q_)
            break
    return tweets


def write_file(file, tweets):
    with open(file, "w+") as csv_file:
        csv_writer = csv.writer(csv_file)
        for tweet in tweets:
            csv_writer.writerow([tweet])


if __name__ == "__main__":
    assert len(sys.argv) == 2, "Usage: python extract_tweets.py filename"
    file = sys.argv[1]
    queries = [
        "Chicago Police", "CPD", "chicago police department", 
        "second city cop", "chicago cop"]
    api = set_up_api()
    tweets = run_queries(queries, api)
    write_file(file, tweets)


