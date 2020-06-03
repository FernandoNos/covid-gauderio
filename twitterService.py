import tweepy

consumer_key = 'RgAe9IG9Wimi6T9lsY7BARGQG'
consumer_secret = 'uxYLXocChG0zJfu5BWJWDq32yFhN9cl7qWgy8SGAhsLpk5jFNz'
access_token = '3007843847-5oDfaubqPTMYoIlSpF4m9vBFZyg0Cym3aGAV1Jv'
access_token_secret = 'aSQDOXMrIVkla5y4lmGzy1Zw3q9241opXedRRTiMUDT56'

def sendTweet(message):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)