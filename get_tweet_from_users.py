#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv

# Twitter API credentials
access_key ='580647653-kHPMSWQdib5xOiz69rhOfiTRK633tZtlT6T5lDCy'
access_secret = 'T5rXoCQGlfk2036iyyRqH9p9wkK5NJjhTsEyTlWRz7pgd'
consumer_key = 'mz4ztvvUpFrn0WxU3btaNiARj'
consumer_secret = 'diaZr26dSdBpHQW3JfsAzQqHCYTJKtnU08M8LzuFo6Gm05GLda'



def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text, tweet.retweet_count,
                   tweet.source_url ] for tweet in alltweets]


    # write the csv
    with open('%s_tweets.csv' % screen_name, mode='w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Tweet id", "Created Time", "Tweet Details",
                         "Retweet counts", "Source URL"])
        writer.writerows(outtweets)

    pass

    print('====== %s CSV generated ======' % screen_name)

#def read_screen_name():
#    with open('testdata2.csv', newline='') as f:
#        reader = csv.reader(f)
#       for row in reader:

#            screen_name_current = row
#           print(screen_name_current)



if __name__ == '__main__':
    # pass in the username of the account you want to download
    # read_screen_name()
    with open('testdata.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            screen_name_current = row [0]
            print('====== %s Begin ======\n' % screen_name_current)
            get_all_tweets(screen_name_current)

