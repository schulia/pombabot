from auth import auth
import tweepy

# Create API object
api = tweepy.API(auth)

# # Create a tweet
api.update_status("Pru")