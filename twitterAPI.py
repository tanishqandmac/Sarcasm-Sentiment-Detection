import twitter
import tweepy
consumer_key='XLfgWE4ZqTpW0fToKTxR4jS1W'
consumer_secret='7wMtcgUTl1WSUsWpT5L8rtJKNkeLOBjvTU9ef1FvQTNr7YyEQ3'
access_token_key='2451495793-Od8i2RbABlbQA6OUQ1ljP2LbTlRJTL1uRMGvDO3'
access_token_secret='Gl56ztlJXzCkgvc7AsDDlbPFVcLWIIFphDNkAFDaZOGPp'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

query = '#sarcasm'
max_tweets = 5
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

for k in searched_tweets:
    print k.text.encode('utf-8')