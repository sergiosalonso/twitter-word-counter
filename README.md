Django Twitter Word Counter
============



Description
===========

Script for getting the 50 most repeated words (descending order), in the last 100 tweets of a person.

Set Up & Installation
===========
Install the requirements: <br />
`pip install -r requirements.txt` <br />
Get the server running: <br />
`python manage.py runserver` <br />
Add your twitter developer keys in read_tweets.py <br />

Test automation
===========

Execute the tests <br />

`python manage.py test word_counter/tests/`
`python manage.py behave`
