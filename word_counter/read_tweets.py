
import tweepy
from datetime import *
consumer_key = "E9Z9R0YUb6MuoWQlInGqESQ9y"
consumer_secret = "muEAST4MncsPGFp7g6pJXeoOdURO9cIHquN9Yg6V7O78S16RF1"
access_token ="1092865494263181312-7FlipxBhpTcBTIFsCKXpn9ZKVBucJt"
access_token_secret ="slaAYc6CZTkSQwyUzuTxs5rZcFRdhzR188lOwCrnc8lcf"

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
