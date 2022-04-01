# Brian Prost
# dad_jokes.py
import requests


def get_dad_joke():
    api_url = "https://zhb2ups653.execute-api.us-east-1.amazonaws.com/default/DadJokeBot"
    response = requests.get(api_url)
    print(response.json())


if __name__ == "__main__":
    # print(get_dad_joke())
    get_dad_joke()
