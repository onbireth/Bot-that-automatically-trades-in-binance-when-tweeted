import tweepy
import time
import api
from binance_bot import *

auth = tweepy.OAuth1UserHandler(
    api.Tapi_key, api.Tapi_secret, api.Tacces_key, api.Tacces_secret)

api = tweepy.API(auth)

search_words = ["ETH", "eth", "ethereum", "Ethereum", "ETHEREUM"]

last_tweet = api.user_timeline(screen_name="kebir000", count=1)[0].text

count = 0

def check():
    tweet = api.user_timeline(screen_name="kebir000", count=1)[0].text

    global last_tweet
    if tweet != last_tweet:
        last_tweet = tweet
        print(f"tweeted: {last_tweet}")
        time.sleep(1)

        print("**********")

        for word in search_words:
            if word in last_tweet:
                print("word found, purchase in process")
                buy_sell()
                global count
                count += 1
        if count == 0:
            print("word not found")

    else:
        print("not tweeted")

while True:
    check()
    if count != 0:
        break
    time.sleep(2)
