from django import forms

class TwitterUserForm(forms.Form):
    twitter_user = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Twitter user'}))
