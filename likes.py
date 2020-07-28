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

#likes code
like_list=api.favorites(screen_name="jmills_gh",count=5) #list of last five favorite of jmills_gh

for tweets in like_list:
    print(tweets.id)
