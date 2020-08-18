import tweepy
from auth import auth

api = tweepy.API(auth)


def _is_tweet_valid(content):
    if ("pomba" in content):
        if not ("gira" in content) and not ("lesa" in content):
            return True

    return False

def _reply_option(tweet):
    question = input(f"Reply to {tweet.text} ?")
    if question == "Y":
        print("reply")
    else:
        return

for tweet in api.search(q="pomba", lang="pt", rpp=10):
    content = str(tweet.text.encode('ascii','ignore'),'utf-8')
    if _is_tweet_valid(content):
        _reply_option(tweet)
        print(tweet.id, content)


