
import tweepy

consumer_key = ""
consumer_secret = ""
access_token =""
access_token_secret =""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_tweets(user="perezreverte", count=50):
    if not (isinstance(user, str) and isinstance(count, int)):
        raise TypeError("First argument must be an instance of str and second argument must be an instance of int.")

    tweets = api.user_timeline(user, count=count)

    if tweets == tweepy.TweepError:
        raise RuntimeError("API stopped working")
    tweet_list = [tweet.text for tweet in tweets]
    #getting the tweets into a list from a status object
    return ' '.join(tweet_list)
