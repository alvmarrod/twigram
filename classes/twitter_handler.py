import tweepy

def twitter_log(con_key, con_sec, acc_token, acc_sec):
  """Returns an API object logged into twitter
  """

  auth = tweepy.OAuthHandler(con_key, con_sec)
  auth.set_access_token(acc_token, acc_sec)

  api = tweepy.API(auth)

  return api

def get_account_tweets(api):
  """Get the own account tweets
  """

  public_tweets = api.home_timeline()

  for tweet in public_tweets:
    print(tweet.text)