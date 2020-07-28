import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

#these can be got from the tweetdev
API_KEY='xxx'
API_SECRET='xxx'
ACCESS_TOKEN='xxx'
ACCESS_SECRET='xxx'

auth=tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

api=tweepy.API(auth)

user=api.get_user("jmills_gh")
print(user.screen_name)#display handle
print(user.followers_count)#display follower count
api.update_status(status="Hello there i am a bot this is my first tweet from a remote pc!")