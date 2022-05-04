#
# Likely deprecated code, from python 2.7 or earlier
# requires pip install tweepy
#
import tweepy;
import time;

# The following are set from creating a dev account at developer.twitter.com
auth = tweepy.OAuthHandler('API_KEY','API_SECRET_KEY')
auth.set_access_token('ACCESS_TOKEN','ACCESS_TOKEN_SECRET')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = "100daysofcode" # This is the term that we want to search
numTweets = 1000 # this is the number of tweets that we want to aggregate through, you can only like 1000/day

for tweet in tweepy.Cursor(api.search, search).items(numTweets):
    try:
        print ('Tweet Liked')
        tweet.favorite()
        tweet.repeat
        time.sleep(87) # 1000 tweets liked / day, so 1 tweet liked every 87 seconds

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        stop