from django.shortcuts import render
from .read_tweets import get_tweets
from .word_counter_skeleton import WordCount
from . import forms
import tweepy
def form_name_view(request):
    form=forms.TwitterUserForm()
    if request.method == 'POST':
        form = forms.TwitterUserForm(request.POST)
        if form.is_valid():
            try:
                text, tweets=get_tweets(time_interval=7, user=form.cleaned_data["twitter_user"])
            except:
                return render(request, "word_counter/twitter-user-form.html", {"exception":"User not found try with another", "form":form})
            return render(request, "word_counter/twitter-user-form.html", {"word_tweets":get_tweets_with_words(text, tweets), "form":form})

    return render(request, "word_counter/twitter-user-form.html", {"form":form})

def get_tweets_with_words(text, tweets):
    k_repeated_words=WordCount(language="english").transform(text, 10)
    word_tweets_dict={}
    for word in k_repeated_words:
        word_tweets_dict[str(word)]=[]
        for tweet in tweets:
            if word[0] in tweet.lower():
                word_tweets_dict[str(word)].append(tweet)
    return word_tweets_dict
