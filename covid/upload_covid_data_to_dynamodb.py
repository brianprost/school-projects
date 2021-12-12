import boto3
import json

joke_table_dynamodb = boto3.resource('dynamodb').Table('NytCovidDataDec10')

with open('covid/nyt_us_states.csv', 'r') as f:
    next(f)
    for line in f:
        state, cases, deaths = line.rstrip().split(',')
        upload_to_dynamodb(state, cases, deaths)


def upload_to_dynamodb(state, cases, deaths):
    joke_table_dynamodb.put_item(
        Item={
            'state': state,
            'cases': int(cases),
            'deaths': int(deaths)
        }
    )
