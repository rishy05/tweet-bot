from googleapiclient.discovery import build
import os
import random
from pprint import pprint

API_KEY = os.getenv("API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

service = build("customsearch", "v1", developerKey=API_KEY)

import requests


# Send a HTTP request to the URL with headers
def down_img(url):
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Open a file to write the image data
        pathh = len(os.listdir("images"))
        with open(f"images\img_{pathh}.jpg", "wb") as file:
            file.write(response.content)
        print("File written succesfully")
        return True
    else:
        print(f"Failed to retrieve the image. Status code: {response.status_code}")
        print(f"Response content: {response.text}")
        return False


def get_image(q):

    img = []

    response = (
        service.cse()
        .list(q=q, cx=SEARCH_ENGINE_ID, searchType="image", start=1, num=10)
        .execute()
    )
    for i in response["items"]:
        img.append(i["link"])

    img_link = random.choice(img)
    if "wikipedia" in img_link:
        img.remove(img_link)
        img_link = random.choice(img)
    img.remove(img_link)

    if down_img(img_link) is False:
        img_link = random.choice(img)

        down_img(img_link)
