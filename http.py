import json
import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'MmaN19kolXI40ZXmj13oOi4gz'
consumer_secret = 'rzJo6Uu7FsEEGOCtwuA0PenawOWPDju2Lox8RrWxaTTIpMdUru'
access_token = '75977508-70NFY9zJXCV2HPstR58mxzW6ihsUDRT8cpYZf3cvi'
access_secret = 'W8DQNSIO29QfOfKA7nM9QlFAwguQN1o4hnCFWGms1USTk'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text) 


