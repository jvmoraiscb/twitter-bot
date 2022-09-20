import twitterBotKeys as twitterBot
import twitterBotMethods as methods
import tweepy
import time

auth = tweepy.OAuth1UserHandler(
    twitterBot.consumer_key,
    twitterBot.consumer_secret,
    twitterBot.access_token,
    twitterBot.access_token_secret
)

api = tweepy.API(auth)
botName = 'vascopuppy'

while True:
    tweets = api.search_tweets(q= '#' + botName + ':')
    for tweet in tweets:
        if tweet.user.screen_name != botName:
            service = methods.getService(tweet.text, botName)
            result = methods.startService(tweet, api, service)
            print(result)

    time.sleep(60*15)