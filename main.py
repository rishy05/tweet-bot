from make_tweet import complete_tweet
from img_search import get_image
from content_llm import places, generate_tweet_caption

while True:
    ask = input(": ")

    if ask == "quit":
        print("BREAKING OUT OF LOOOP")
        break

    pl = places(ask)
    twt = generate_tweet_caption(ask)

    get_image(pl)

    complete_tweet(twt)
