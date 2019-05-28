
import tweepy
from datetime import *
import os
consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_tweets(time_interval=7, user="perezreverte"):
    if not (isinstance(user, str) and isinstance(time_interval, int)):
        raise TypeError("First argument must be an instance of str and second argument must be an instance of int.")
    page=1
    end=False
    tweet_list=[]
    date=datetime.now()
    max_time=timedelta(days=time_interval, seconds=0, microseconds=0)
    while not end:
        tweets = api.user_timeline(user, tweet_mode='extended', page=page)
        if tweets == tweepy.TweepError:
            raise RuntimeError("API stopped working")

        for tweet in tweets:
            time_passed=date - tweet.created_at
            if time_passed <=  max_time:
                tweet_list.append(tweet.full_text)
            else:
                end = True
                break

        if not end:
            page+=1

    return ' '.join(tweet_list), tweet_list
