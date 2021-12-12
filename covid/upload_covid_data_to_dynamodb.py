import boto3
import json

COVID_TABLE_DYNAMODB = boto3.resource('dynamodb').Table('NytCovidDataDec10')

def main():


    with open('nyt_us_states.csv', 'r') as f:
        next(f)
        for line in f:
            state, cases, deaths = line.rstrip().split(',')
            upload_to_dynamodb(state, cases, deaths)


def upload_to_dynamodb(state, cases, deaths):
    COVID_TABLE_DYNAMODB.put_item(
        Item={
            'state': state,
            'cases': int(cases),
            'deaths': int(deaths)
        }
    )

if __name__ == "__main__":
    main()