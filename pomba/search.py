import tweepy
from auth import auth

api = tweepy.API(auth)


def _is_tweet_valid(content):
    if ("pomba" in content):
        if not ("gira" in content) and not ("lesa" in content):
            return True

    return False

def _reply_option(tweet):
    question = input(f"Reply to {tweet.text} ? [y/n]")
    if question == "Y":
        print("reply")
    else:
        return

def _follow_option(tweet):
    author = tweet.author.screen_name
    question = input(f"Follow {author}? [y/n]")
    if question == "y":
        # api.create_friendship(author)
        print(f"followed {author}")


for tweet in api.search(q="pomba", lang="pt", rpp=15):
    content = str(tweet.text.encode('ascii','replace'),'utf-8')
    if _is_tweet_valid(content):
        print(('@' +tweet.author.screen_name),'said: ', content,
        '\n https://twitter.com/user/status/'+str(tweet.id)+'\n') # tweet.id


