import boto3
import random


def menu():
    dad_joke = get_dad_joke()


def get_dad_joke():
    dynamodb_r = boto3.resource('dynamodb')
    dad_jokes = dynamodb_r.Table('DadJokesDb')

    joke_id = random.randint(0,dad_jokes.item_count)

    joke_obj = dad_jokes.get_item(Key={'joke_id': joke_id})
    joke = joke_obj['Item']['joke']

    return joke


if __name__ == "__main__":
    # print(get_dad_joke())
    menu()