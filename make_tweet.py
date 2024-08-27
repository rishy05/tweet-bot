import tweepy
import os
import shutil


def clear_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return

    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        try:
            if os.path.isfile(entry_path) or os.path.islink(entry_path):
                os.unlink(entry_path)
            elif os.path.isdir(entry_path):
                shutil.rmtree(entry_path)
        except Exception as e:
            print(f"Failed to delete {entry_path}. Reason: {e}")

    print(f"All contents of {directory_path} have been removed.")


# Load credentials from environment variables
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


def complete_tweet(tweet_content):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    client = tweepy.Client(
        bearer_token,
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret,
        wait_on_rate_limit=True,
    )

    img = os.listdir("images")[-1]
    print(img)

    media_id = api.media_upload(filename=f"images/{img}").media_id_string
    print(media_id)

    text = tweet_content

    client.create_tweet(text=text, media_ids=[media_id])
    print("TWEET CREATED")

    clear_directory("images")
