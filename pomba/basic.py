from auth import auth
from pru import makepru
import tweepy

# Create API object
api = tweepy.API(auth)

# # Create a tweet
tweet_content = makepru()
api.update_status(tweet_content)
print('tweeted :', tweet_content)