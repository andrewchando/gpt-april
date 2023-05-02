# 4/7/23 - unroll tweet threads from cli 
# does threadreader type functionality but more compact

import sys
import tweepy
from tqdm import tqdm

# set up API keys
API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

def authenticate():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def find_reply(tweets, tweet_id):
    for tweet in tweets:
        if tweet.in_reply_to_status_id == tweet_id:
            return tweet
    return None

def clean_text(text):
    return ' '.join(line.strip() for line in text.strip().split('\n') if line.strip())

def unroll_thread(api, tweet_url):
    tweet_id = tweet_url.split('/')[-1]

    try:
        tweet = api.get_status(tweet_id, tweet_mode='extended')
        thread = [tweet]
        user_id = tweet.user.id

        with tqdm(total=None, desc="Fetching tweets", unit=" tweet", ncols=80) as pbar:
            while True:
                tweets = list(tweepy.Cursor(api.user_timeline,
                                            user_id=user_id,
                                            since_id=tweet.id,
                                            tweet_mode='extended',
                                            exclude_replies=False,
                                            include_rts=False).items(200))
                reply = find_reply(tweets, tweet.id)
                if reply:
                    thread.append(reply)
                    tweet = reply
                    pbar.update(1)
                else:
                    break

        print("\nUnrolled tweets:\n")
        for i, tweet in enumerate(thread):
            print(f"{i+1}. {clean_text(tweet.full_text)}")
            #print(f"{i+1}. {tweet.user.screen_name}: {clean_text(tweet.full_text)}")
            print("")

    except tweepy.errors.TweepError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py unroll.py <tweet_url>")
        sys.exit(1)

    tweet_url = sys.argv[1]
    api = authenticate()
    unroll_thread(api, tweet_url)