import sys
import json
import time
import logging
import twitter
import urllib.parse

from os import environ as e

t = twitter.Api(
    consumer_key=e["mz4ztvvUpFrn0WxU3btaNiARj"],
    consumer_secret=e["diaZr26dSdBpHQW3JfsAzQqHCYTJKtnU08M8LzuFo6Gm05GLda"],
    access_token_key=e["580647653-kHPMSWQdib5xOiz69rhOfiTRK633tZtlT6T5lDCy"],
    access_token_secret=e["T5rXoCQGlfk2036iyyRqH9p9wkK5NJjhTsEyTlWRz7pgd"],
    sleep_on_rate_limit=True
)

def tweet_url(t):
    return "https://twitter.com/%s/status/%s" % (t.user.screen_name, t.id)

def get_tweets(filename):
    for line in open(filename):
        yield twitter.Status.NewFromJsonDict(json.loads(line))

def get_replies(tweet):
    user = tweet.user.screen_name
    tweet_id = tweet.id
    max_id = None
    logging.info("looking for replies to: %s" % tweet_url(tweet))
    while True:
        q = urllib.parse.urlencode({"q": "to:%s" % user})
        try:
            replies = t.GetSearch(raw_query=q, since_id=tweet_id, max_id=max_id, count=100)
        except twitter.error.TwitterError as e:
            logging.error("caught twitter api error: %s", e)
            time.sleep(60)
            continue
        for reply in replies:
            logging.info("examining: %s" % tweet_url(reply))
            if reply.in_reply_to_status_id == tweet_id:
                logging.info("found reply: %s" % tweet_url(reply))
                yield reply
                # recursive magic to also get the replies to this reply
                for reply_to_reply in get_replies(reply):
                    yield reply_to_reply
            max_id = reply.id
        if len(replies) != 100:
            break

if __name__ == "__main__":
    logging.basicConfig(filename="replies.log", level=logging.INFO)
    tweets_file = sys.argv[1]
    for tweet in get_tweets(tweets_file):
        for reply in get_replies(tweet):
            print(reply.AsJsonString())