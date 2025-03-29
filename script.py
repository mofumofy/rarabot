import tweepy
import pandas as pd
import time
import random
import schedule

url = 'Google Sheets'
df = pd.read_csv(url)


def tweet_now(msg):
    msg = msg[0:280]
    try:

        auth = tweepy.OAuthHandler("now deleted", 
            "for privacy")
        auth.set_access_token("deleted", 
            "for privacy!")
        api = tweepy.API(auth)
        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        
        api.update_status(msg)
        print(msg)

        print("Tweeted")
    
    except tweepy.TweepyException as e:
        print (e)
        idx = random.randrange(0, len(df.index))
        tweet_now(df.iloc[idx, 0])

def job():
    idx = random.randrange(0, len(df.index))
    tweet_now(df.iloc[idx, 0])



#schedule.every().day.at("00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
