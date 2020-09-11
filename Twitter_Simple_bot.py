import tweepy
import time

#Use your keys from twitter here:
auth = tweepy.OAuthHandler("CONSUMER_KEY", "SECRET_CONSUMER_KEY") 
auth.set_access_token("ACCESS_TOKEN","ACCESS_SECRET_TOKEN")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

#You can anything you want in 'I love animes' place and the bot will search this words from random people for you"
search = 'I love anime'

TweetsCount = 20


for tweet in tweepy.Cursor(api.search, search).items(TweetsCount):
    try:
        print('Hey')
        tweet.retweet()
        tweet.favorite()
        time.sleep(60 * 60)   # This is the time (in Seconds that your bot will like and retweet another tweet with you write in 'search' , please don't use a short time, twitter can block your account "like spam")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
        
        #njoy!