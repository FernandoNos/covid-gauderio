import tweepy
import os

consumer_key = 'fKF2YkRHvrPKDbAmvru8bguvY'
consumer_secret = 'XSiT0Vq8LLBca7rk7zjOoqZYMUgxsngy50nEC7pZBGKB9sT2PT'
access_token = '1262572521834057731-rRPa3tmJ8N75yj4iTeZwNtPrUWMfFW'
access_token_secret = 'SOD39dL4KAAVCKLjJtvCsV1m6mFTZ7MLn4ZUxOLppAPxQ'

print('Variables Set!')

def sendTweet(message):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)