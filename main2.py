from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import time

access_token ='580647653-kHPMSWQdib5xOiz69rhOfiTRK633tZtlT6T5lDCy'
access_token_secret = 'T5rXoCQGlfk2036iyyRqH9p9wkK5NJjhTsEyTlWRz7pgd'
consumer_key = 'mz4ztvvUpFrn0WxU3btaNiARj'
consumer_secret = 'diaZr26dSdBpHQW3JfsAzQqHCYTJKtnU08M8LzuFo6Gm05GLda'

class Sl (StreamListener):

    def on_data(self,data):
        try:
            print (data)
            savefile = open("/Users/xuanfan/Desktop/twitter.txt","a")
            savefile.write(data)
            savefile.write('\n')
            savefile.close()
            return True
        except BaseException as e:
            print ('Failed on data', str(e))
            time.sleep(5)

        def on_error(self,status):
            print(status)

if __name__ == 'main':
    l = Sl()
    print('work')
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth,l)
    stream.filter(track = ['salesforce','javascript','python'])