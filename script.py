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
        auth.set_access_token("1174986605007798272-igLhTg6lRljkUf5ZCTEW5wK31zq4yg", 
            "B5LzdCD4JGxn1oGi2K26zVqLf1Ja7ZMKn7Djr6qqcXc0d")
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

schedule.every().hour.at(":00").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
