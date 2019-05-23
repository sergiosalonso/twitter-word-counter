from django.test import TestCase
from word_counter.read_tweets import get_tweets
from unittest.mock import patch, Mock
from datetime import datetime
from collections import namedtuple
import tweepy

class TestTweets(TestCase):
    Tweet = namedtuple('Status', ['id', 'full_text', 'created_at', 'author'])
    Author = namedtuple('User', ['name', 'screen_name'])

    tweet1 = Tweet(id=431356619243266048,
                   full_text='hola hola hola me llamo juan',
                   created_at=datetime.now(),
                   author=Author(name='perezreverte', screen_name='perezreverte'))

    tweet2 = Tweet(id=431356619243266048,
                   full_text='me me llamo juan juan',
                   created_at=datetime.now(),
                   author=Author(name='perezreverte', screen_name='perezreverte'))
    tweet3 = Tweet(id=431356619243266048,
                   full_text='pepe popo pipo',
                   created_at=datetime(2017, 1, 1),
                   author=Author(name='perezreverte', screen_name='perezreverte'))

    @patch.object(tweepy.API, 'user_timeline')
    def test_get_two_tweets(self, mock_user_timeline):
        mock_user_timeline.return_value=[self.tweet1, self.tweet3]
        #print(get_tweets(user="perezreverte"))
        self.assertEqual(get_tweets(user="perezreverte"), ('hola hola hola me llamo juan', ['hola hola hola me llamo juan']))

    @patch("tweepy.API.user_timeline")
    def test_get_three_tweets(self, mock_user_timeline):
        mock_user_timeline.return_value=[self.tweet1, self.tweet2, self.tweet3]
        self.assertEqual(get_tweets(user="perezreverte"), ('hola hola hola me llamo juan me me llamo juan juan', ['hola hola hola me llamo juan', 'me me llamo juan juan']))

    @patch.object(tweepy.API, 'user_timeline')
    def test_api_error(self, mock_user_timeline):
        mock_user_timeline.return_value= tweepy.error.TweepError
        with self.assertRaises(RuntimeError):
            get_tweets(user="perezreverte")

    @patch.object(tweepy.API, 'user_timeline')
    def test_wrong_parameters(self, mock_user_timeline):
        with self.assertRaises(TypeError):
            get_tweets("hola", 4)
