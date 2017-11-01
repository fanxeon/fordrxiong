#  -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler

access_token ='580647653-kHPMSWQdib5xOiz69rhOfiTRK633tZtlT6T5lDCy'
access_secret = 'T5rXoCQGlfk2036iyyRqH9p9wkK5NJjhTsEyTlWRz7pgd'
consumer_key = 'mz4ztvvUpFrn0WxU3btaNiARj'
consumer_secret = 'diaZr26dSdBpHQW3JfsAzQqHCYTJKtnU08M8LzuFo6Gm05GLda'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(100):
    print (status.text)