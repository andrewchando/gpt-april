import sys
import tweepy
import openai
import re

# Set your API keys for Twitter and OpenAI
TWITTER_API_KEY = "-"
TWITTER_API_SECRET = "-"
TWITTER_ACCESS_TOKEN = "-"
TWITTER_ACCESS_SECRET = "-"
OPENAI_API_KEY = "-"

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

# Authenticate to OpenAI API
openai.api_key = OPENAI_API_KEY

def get_tweet_id(url):
    match = re.search(r"status/(\d+)", url)
    return match.group(1) if match else None

def get_tweet_thread(tweet_id):
    thread = []
    try:
        while True:
            tweet = api.get_status(tweet_id, tweet_mode="extended")
            thread.append(tweet)
            if not tweet.in_reply_to_status_id:
                break
            tweet_id = tweet.in_reply_to_status_id
    except tweepy.TweepError as e:
        print(f"Error fetching tweet thread: {e}")
        return None
    return thread[::-1]

def get_summary(text):
    prompt = f"Provide an executive summary of the following tweet thread in up to 5 paragraphs, including details and specifics:\n{text}\n\nDetails and specifics to include:\n- Key points and arguments\n- Supporting evidence\n- Context and background\n- Implications and conclusions\n\n"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=3,
        temperature=0.5,
        stop=None,
    )

    summaries = [choice.text.strip() for choice in response.choices]
    return "\n\n".join(summaries)

def main():
    if len(sys.argv) != 2:
        print("Usage: python summarize.py TWEET_THREAD_URL")
        return

    url = sys.argv[1]
    tweet_id = get_tweet_id(url)
    if not tweet_id:
        print("Invalid tweet URL")
        return

    thread = get_tweet_thread(tweet_id)
    if not thread:
        print("Couldn't fetch the tweet thread")
        return

    thread_text = "\n".join([f"{tweet.user.screen_name}: {tweet.full_text}" for tweet in thread])
    summary = get_summary(thread_text)
    if not summary:
        print("Couldn't generate a summary for the tweet thread")
        return

    print(f"Summary of the tweet thread:\n{summary}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error running the script: {e}")
