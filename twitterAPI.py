import twitter
api = twitter.Api(consumer_key='XLfgWE4ZqTpW0fToKTxR4jS1W',consumer_secret='7wMtcgUTl1WSUsWpT5L8rtJKNkeLOBjvTU9ef1FvQTNr7YyEQ3',access_token_key='2451495793-Od8i2RbABlbQA6OUQ1ljP2LbTlRJTL1uRMGvDO3',access_token_secret='Gl56ztlJXzCkgvc7AsDDlbPFVcLWIIFphDNkAFDaZOGPp')
users = api.GetFriends()
print([u.name for u in users])