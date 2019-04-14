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
                tweets=get_tweets(form.cleaned_data["twitter_user"], 100)
            except:
                return render(request, "word_counter/twitter-user-form.html", {"exception":"User not found try with another", "form":form})
            return render(request, "word_counter/twitter-user-form.html", {"word_counter":WordCount().transform(tweets, 50), "form":form})

    return render(request, "word_counter/twitter-user-form.html", {"form":form})
