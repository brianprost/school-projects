import boto3
import json
import random

def lambda_handler(event, context):
    joke = get_dad_joke()
    return {
        'statusCode': 200,
        'body': json.dumps(joke)
    }


def get_dad_joke():
    dynamodb_r = boto3.resource('dynamodb')
    dad_jokes = dynamodb_r.Table('DadJokesDb')

    joke_id = random.randint(0,dad_jokes.item_count)

    joke_obj = dad_jokes.get_item(Key={'joke_id': joke_id})
    joke = joke_obj['Item']['joke']

    return joke
