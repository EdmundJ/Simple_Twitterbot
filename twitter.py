import tweepy
import time


authentication = tweepy.OAuthHandler("API key","API secret key") #change the API and API Secret key with you own value
authentication.set_access_token("Access token", "Access token secret") #change the token and token secret key with you own value
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
User = api.me()

search = input("Input of a hastag (e.g:#python): ")
number_of_tweet = 20  # Limit how many tweet to go through

for tweet in tweepy.Cursor(api.search, search).items(number_of_tweet):
    try:
        print("Tweet has been liked")
        tweet.favorite()
        time.sleep(10)
        print("Tweet has been retweetet")
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as error:
        print(error.reason)
    except StopIteration:
        break



