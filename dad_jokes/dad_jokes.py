import json
import random

def get_dad_joke():
    # TODO: move to DynamoDB
    with open('dad_jokes/jokes.json') as f:
        joke_db = json.load(f)

    joke = random.choice(joke_db)
    return joke

if __name__ == "__main__":
    print("What did the ocean say to the beach? Nothing, it just waved.")