import tweepy
import pandas as pd
import time
import random
import schedule

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQJOUMvavjRrVV0uR_aYofU2WEJPDhxy9u8N_weO04hvKmtDbkrip85r2YIHwm6NOdqoCguer4WFy6J/pub?output=csv'
df = pd.read_csv(url)


def tweet_now(msg):
    msg = msg[0:280]
    try:

        auth = tweepy.OAuthHandler("Sd0LCUcTj4SojlAHUq27dssp2", 
            "yPx5yxZpENQOdTT5yjahJkSJofiClocgQRP6sl2errh7f4uBSq")
        auth.set_access_token("1174986605007798272-PyyaTe5BvMGAzd59KHstXUrSKcPQuW", 
            "2CEdDbdEU4PKsM0SjuI38tCmowFXyf5pL6uIvZMboRyt8")
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

schedule.every().day.at("12:00").do(job)
schedule.every().day.at("00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
