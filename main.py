
import classes.twitter_handler as twh

if "__name__" == "__main__":
  
  api = twh.twitter_log()
  twh.get_account_tweets(api)