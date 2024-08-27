import os

from groq import Groq


from time import sleep

from pprint import pprint


mod = "llama-3.1-70b-versatile"


GROQ_KEY = os.getenv("GROQ_KEY")

client = Groq(
    api_key=GROQ_KEY,
)


def generate_tweet_caption(initial):

    chat_completion_content = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Generate a tweet which will be used in a twitter bot. Here is what the tweet should be about {initial}. just generate the content and nothing else. if i find it useful i will tip you 10$",
            }
        ],
        model=mod,
    )
    con = chat_completion_content.choices[0].message.content

    print(con)

    return con


def places(txt):
    chat_completion_places = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""You are an AI assistant designed to extract key search terms from news headlines or text descriptions. Your task is to identify the most relevant 2-3 words that capture the main subject and context of the given text. These terms will be used for image searches, so focus on concrete, visual elements rather than abstract concepts.

Rules:
1. Provide only the search terms, without any additional explanation.
2. Use 2-3 words maximum, separated by spaces.
3. Include location names when relevant.
4. Avoid common words like articles, prepositions, or linking verbs.
5. Prioritize nouns and proper nouns that represent the core subject.

Examples:
Input: "Rape case in Kolkata shatters everyone"
Output: rape Kolkata

Input: "War in Yemen destroys livelihoods of 300,000 people"
Output: war Yemen

Input: "New species of butterfly discovered in Amazon rainforest"
Output: butterfly Amazon

Now, generate search terms for the following text:{txt}""",
            }
        ],
        model=mod,
    )
    pl = chat_completion_places.choices[0].message.content
    print(pl)
    return pl
