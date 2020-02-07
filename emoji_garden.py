# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *
import random

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q="#garden").items():
    try:
        res_str = "Tweet by: @" + tweet.user.screen_name + "\n"
        tweet_text = tweet.text
        flowers = "🌷🌹🥀🌺🌸🌼🌻🍀🌵🌳🌱🌴🎋🍄"

        while len(res_str) < 120:
            for letter in tweet_text:
                res_str += random.choice(flowers)
        print(res_str)
        api.update_status(res_str)
        sleep(3000)
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
